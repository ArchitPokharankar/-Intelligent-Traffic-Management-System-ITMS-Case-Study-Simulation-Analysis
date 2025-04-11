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
      
      
      
def traverse(startNode, targetNode):
  
  queue = [(startNode,0)]
  visited = []
  
  while queue:
    
    currentNode, distance = queue.pop(0)
    
    if currentNode == targetNode:
      return distance
    if currentNode not in visited:
      visited.append(currentNode)
      
      for neighbor in currentNode.connections:
        if neighbor not in visited:
          queue.append((neighbor,distance+1))
    
  return -1
    
  
    
    
    
# Create nodes
Node1 = Node("1")
Node2 = Node("2")
Node3 = Node("3")
Node4 = Node("4")
Node5 = Node("5")

# Add connections
Node1.add_connection([Node2, Node3, Node4])
Node2.add_connection(Node1)
Node3.add_connection(Node4)
Node4.add_connection([Node1, Node2, Node5])
Node5.add_connection(Node3)

# Print Node1 details
print(Node1)

print(f"Distance between nodes: {traverse(Node1,Node5)}")