import networkx as nx
from pyvis.network import Network

# Create a new graph
g = nx.Graph()

# Add nodes (representing different pages of your website)
g.add_node('Bio', title='Bio', url='bio.html')
g.add_node('Research', title='Research', url='research.html')
g.add_node('Music', title='Music', url='music.html')
g.add_node('Awards', title='Awards', url='awards.html')
g.add_node('Contact', title='Contact', url='contact.html')

# Define the connections between nodes
# In this case, all nodes are connected to the central 'Home' node
g.add_edge('Bio', 'Home')
g.add_edge('Research', 'Home')
g.add_edge('Music', 'Home')
g.add_edge('Awards', 'Home')
g.add_edge('Contact', 'Home')

# Create a Pyvis network from the NetworkX graph
nt = Network('500px', '100%', notebook=True)
nt.from_nx(g)

# Set options for interactivity
nt.set_options("""
var options = {
  "nodes": {
    "borderWidth": 2,
    "borderWidthSelected": 4,
    "shape": "dot",
    "size": 30,
    "font": {
      "size": 32
    }
  },
  "edges": {
    "smooth": false
  },
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -100,
      "centralGravity": 0.01,
      "springLength": 100,
      "springConstant": 0.08
    },
    "maxVelocity": 50,
    "solver": "forceAtlas2Based",
    "timestep": 0.35,
    "stabilization": {
      "enabled": true,
      "iterations": 2000
    }
  }
}
""")

# Customize node interaction
for node in nt.nodes:
    node["title"] += "<br>Click to visit"
    node["value"] = 5  # Control the size of nodes
    if 'url' in node:
        node["url"] = node.pop("url")  # Assign the URL to the node

# Generate and save the network graph to an HTML file
nt.show('network.html')
