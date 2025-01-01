# wikipedia-universe

**Visualize Wikipedia Relationships**
   Explore the tree-like structure representing the relationships between Wikipedia articles. The application updates in real time as it crawls through new links. It also stores the article titles in a text file for later reference.

# Demo

![wiki-universe-gif](https://github.com/user-attachments/assets/4a1be8f5-4b78-4af7-b178-7e5fa83ac18b)

## Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/visvig/wikipedia-universe.git
   cd wikipedia-universe

2. **Check and install dependencies**
   ```bash
   python check_deps.py

3. **Run the Application**
   ```bash
   python app.py

4. **Access the Application**
   Open your browser and navigate to
   ```bash
   http://127.0.0.1:8050/

## Customization

You can customize the crawling behavior or visualization by editing the following:

1. **Graph Layout**:  
   Customize the graph layout by modifying the `layout` property of the `Cytoscape` component in `app.py`.  

   Example:  
   ```python
   layout={'name': 'breadthfirst'}  # Change to 'cose', 'grid', etc., as per preference

2. **Starting Article**:  
   You can change the starting article that the crawler uses by modifying the `start_title` variable in the `background_crawler` function in `app.py`.  

   Example:  
   ```python
   start_title = "Artificial Intelligence"  # Replace with any Wikipedia article title


3. **Crawling Depth**:  
   Adjust the depth of the Wikipedia crawler in the `background_crawler` function in `app.py`.  
   ```python
   depth = 2  # Set the desired depth of the crawl

## License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute the code as per the terms of the license.  

See the [LICENSE](LICENSE) file for more details.




