import dash
import dash_cytoscape as cyto
from dash import html, dcc
from updater import WikipediaGraph
import threading
import time
import logging
import datetime

# Configure logging
log_filename = f"wikipedia_crawler_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
articles_filename = f"wikipedia_articles_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to terminal
        logging.FileHandler(log_filename, mode='w')  # Save logs to a file
    ]
)

# Initialize Dash app and WikipediaGraph
app = dash.Dash(__name__)
wiki_graph = WikipediaGraph()

# Log app initialization
logging.info("Dash app initialized. Starting with an empty graph.")

# Save article names to a file
def save_articles_to_file():
    """Save all current article names (nodes) to a file."""
    with open(articles_filename, 'w') as f:
        for node in wiki_graph.graph.nodes:
            f.write(node + '\n')
    logging.info(f"Article names saved to {articles_filename}")

# Layout of the app
app.layout = html.Div([
    html.H1("Wikipedia Graph Visualization"),
    html.P("This app visualizes the relationships between Wikipedia articles as a graph."),
    dcc.Interval(
        id='interval-component',
        interval=10000,  # Update every 10 seconds
        n_intervals=0
    ),
    cyto.Cytoscape(
        id='cytoscape-graph',
        layout={'name': 'cose'},  # Force-directed layout
        style={'width': '100%', 'height': '800px'},
        elements=[]  # Start with an empty graph
    )
])

# Update the graph elements in real time
@app.callback(
    dash.dependencies.Output('cytoscape-graph', 'elements'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_elements(n_intervals):
    logging.info("Updating graph elements for visualization.")
    elements = wiki_graph.get_elements()
    logging.info(f"Graph currently has {len(wiki_graph.graph.nodes)} nodes and {len(wiki_graph.graph.edges)} edges.")
    save_articles_to_file()  # Save articles to the file each time the graph updates
    return elements

# Background thread to crawl Wikipedia
def background_crawler():
    logging.info("Background crawler started.")
    start_title = "Artificial Intelligence"  # Initial article
    depth = 10  # Limit to a manageable depth for testing

    while True:
        # Find an unvisited node if one exists, otherwise use start_title
        unvisited_nodes = set(wiki_graph.graph.nodes) - wiki_graph.visited
        if unvisited_nodes:
            next_title = unvisited_nodes.pop()
        else:
            next_title = start_title

        logging.info(f"Starting crawl from '{next_title}' with depth {depth}.")
        try:
            wiki_graph.crawl_and_update(start_title=next_title, depth=depth)
        except Exception as e:
            logging.error(f"Error during crawling: {e}")
        logging.info(f"Crawl complete. Graph now has {len(wiki_graph.graph.nodes)} nodes and {len(wiki_graph.graph.edges)} edges.")
        time.sleep(10)

# Start the background crawler in a thread
threading.Thread(target=background_crawler, daemon=True).start()

if __name__ == '__main__':
    logging.info("Starting Dash server...")
    app.run_server(debug=True)