import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_random_weighted_graph(num_nodes, num_edges):
    G = nx.Graph()
    
    for i in range(num_nodes):
        G.add_node(i)

    edges_added = 0
    while edges_added < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)

        if node1 != node2 and not G.has_edge(node1, node2):
            weight = random.uniform(0.1, 10.0) 
            G.add_edge(node1, node2, weight=weight)
            edges_added += 1

    return G


num_nodes = 5
num_edges = 7
random_weighted_graph = generate_random_weighted_graph(num_nodes, num_edges)


pos = nx.spring_layout(random_weighted_graph)  
plt.title('Взвешенный граф')
nx.draw(random_weighted_graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold')

edge_labels = nx.get_edge_attributes(random_weighted_graph, 'weight')

nx.draw_networkx_edge_labels(random_weighted_graph, pos, edge_labels=edge_labels)


plt.show()
