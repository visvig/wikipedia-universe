dependencies = [
    "requests",
    "networkx",
    "dash",
    "dash_cytoscape",
    "tqdm",
    "threading", 
    "time",
    "logging",
    "datetime",
    "importlib",
    "bs4"
]

for lib in dependencies:
    try:
        import importlib
        importlib.import_module(lib)
    except ImportError:
        print(f"Error: {lib} is not installed. Please install it using 'pip install {lib}'")
        print(f"Error: {lib} is not installed. Please install it using 'pip install {lib}'")