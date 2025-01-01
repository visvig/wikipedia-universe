import networkx as nx
import requests
from bs4 import BeautifulSoup

class WikipediaGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed graph for Wikipedia links
        self.visited = set()  # Keep track of visited nodes

    def crawl_and_update(self, start_title, depth):
        """Crawl Wikipedia starting from a given title."""
        if depth == 0 or start_title in self.visited:
            return
        
        self.visited.add(start_title)
        url = f"https://en.wikipedia.org/wiki/{start_title.replace(' ', '_')}"
        response = requests.get(url)
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", href=True)
        for link in links:
            href = link['href']
            if href.startswith("/wiki/") and ":" not in href:
                article_title = href.split("/wiki/")[1]
                self.graph.add_edge(start_title, article_title)
                if article_title not in self.visited and len(self.graph.nodes) < 1000:
                    self.crawl_and_update(article_title, depth - 1)

    def get_elements(self):
        """Convert graph nodes and edges to Cytoscape elements."""
        elements = []
        for node in self.graph.nodes:
            elements.append({'data': {'id': node, 'label': node}})
        for edge in self.graph.edges:
            elements.append({'data': {'source': edge[0], 'target': edge[1]}})
        return elements