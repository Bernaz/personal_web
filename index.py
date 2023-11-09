import networkx as nx
from pyvis.network import Network

# Create a new graph
g = nx.Graph()

# Add nodes (representing different pages of your website)
g.add_node('Bio', size=20)
g.add_node('Research', size=20)

# Define the connections between nodes
g.add_edge('Bio', 'Research')  # Assuming you want a direct link between 'Bio' and 'Research'

# Initialize Pyvis network object; set notebook to False since this is for an HTML file
nt = Network('500px', '500px', notebook=False)

# Import the networkx graph
nt.from_nx(g)

# Set the physics options for stability (optional)
nt.options.physics.stabilization.iterations = 200

# Set the titles and URLs for the nodes
for node in nt.nodes:
    if node['id'] == 'Bio':
        node['title'] = 'Bio'
        node['url'] = 'bio.html'
    elif node['id'] == 'Research':
        node['title'] = 'Research'
        node['url'] = 'research.html'

# Make the nodes clickable by setting the navigation to True
nt.options.interaction.navigation = True

# Generate and save the network graph to an HTML file
nt.show('index.html')
