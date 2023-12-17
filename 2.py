import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_connected_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(range(1, nodes + 1))
   
    for i in range(1, nodes):
        node1 = i
        node2 = random.randint(i + 1, nodes)
        G.add_edge(node1, node2)
        edges -= 1

    # случайное расставляем рёбра, пока не свяжем весь граф
    while edges > 0:
        node1 = random.randint(1, nodes)
        node2 = random.randint(1, nodes)
        if node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2)
            edges -= 1

    return G


num_nodes = 10
num_edges = 15

graph = generate_connected_graph(num_nodes, num_edges)

plt.title("Связный граф")
nx.draw(graph, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')

plt.show()
