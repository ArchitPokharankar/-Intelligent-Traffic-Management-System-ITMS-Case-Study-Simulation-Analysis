import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

    def add_connection(self, connected_node):
        if isinstance(connected_node, list):
            self.connections.extend(connected_node)
        else:
            self.connections.append(connected_node)

    def __repr__(self):
        connections_str = ', '.join([str(node.value) for node in self.connections])
        return f"Node({self.value}) is connected to: [{connections_str}]"

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

def traverse(startNode, targetNode):
    queue = [(startNode, 0)]
    visited = set()  # Use a set instead of a list for efficiency

    while queue:
        currentNode, distance = queue.pop(0)

        if currentNode == targetNode:
            return distance
        if currentNode not in visited:
            visited.add(currentNode)

            for neighbor in currentNode.connections:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    return -1

# Create nodes
Node1 = Node("1")
Node2 = Node("2")
Node3 = Node("3")
Node4 = Node("4")
Node5 = Node("5")

# Add connections (bidirectional)
Node1.add_connection([Node2, Node3, Node4])
Node2.add_connection([Node1, Node4])  # Ensure bidirectional link
Node3.add_connection([Node4, Node5])  # Added connection to Node5
Node4.add_connection([Node1, Node2, Node3, Node5])  # Complete bidirectional links
Node5.add_connection([Node3, Node4])  # Ensure Node5 has bidirectional links




def visualize_graph_with_path(edges, start, target, shortest_path):
    # Create an undirected graph
    G = nx.Graph()
    
    # Add edges to the graph
    G.add_edges_from(edges)

    # Generate positions for nodes
    pos = nx.spring_layout(G)

    # Draw the graph
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=2000, font_size=14, edge_color='gray')

    # Highlight the shortest path
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)
    
    # Highlight start and target nodes
    nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', node_size=2500, label="Start Node")
    nx.draw_networkx_nodes(G, pos, nodelist=[target], node_color='red', node_size=2500, label="Target Node")

    plt.title("Graph Representation with Shortest Path")
    plt.show()

# Define edges in the graph
edges = [("1", "2"), ("1", "3"), ("1", "4"), 
         ("2", "4"), ("3", "4"), ("3", "5"), 
         ("4", "5")]

# Define start and target nodes
start_node = "1"
target_node = "5"

# Find the shortest path using BFS
G = nx.Graph()
G.add_edges_from(edges)
shortest_path = nx.shortest_path(G, source=start_node, target=target_node)

# Visualize the graph with the path highlighted
visualize_graph_with_path(edges, start_node, target_node, shortest_path)