import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_oriented_graph(num_nodes, num_edges):
  
    graph = nx.DiGraph()
   
    for i in range(num_nodes):
        graph.add_node(i)

    edges_added = 0
    while edges_added < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        
        if node1 != node2 and not graph.has_edge(node1, node2):
            graph.add_edge(node1, node2)
            edges_added += 1

    return graph


num_nodes = 5
num_edges = 7
generated_graph = generate_oriented_graph(num_nodes, num_edges)


plt.figure(figsize=(8, 6))
pos = nx.spring_layout(generated_graph)  
plt.title("Слуайный ориентированный граф")
nx.draw(generated_graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', arrows=True)

plt.show()
