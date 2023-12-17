import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, num_edges):
    G = nx.Graph()

    for i in range(num_nodes):
        G.add_node(i)

    edges_added = 0
    while edges_added < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        if node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2)
            edges_added += 1

    return G

def color_graph(graph):
    color_map = {}

    for node in graph.nodes():
        neighbor_colors = set()
        
        neighbors = graph.neighbors(node)
        
        for neighbor in neighbors:
            if neighbor in color_map:
                neighbor_color = color_map[neighbor]
                neighbor_colors.add(neighbor_color)
        
        for color in range(len(graph.nodes())):
            if color not in neighbor_colors:
                color_map[node] = color
                break

    return color_map

def visualize_graph(graph, color_map):
    unique_colors = set(color_map.values())

    color_list = plt.cm.tab20.colors  
    colors = random.sample(color_list, len(unique_colors))

    node_colors = [colors[color_map[node]] for node in graph.nodes()]


    pos = nx.spring_layout(graph)
    plt.title('Раскрашеный граф')
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=500, font_weight='bold')
    
    plt.show()


num_nodes = 10 
num_edges = 15  


random_graph = generate_random_graph(num_nodes, num_edges)

node_colors = color_graph(random_graph)

visualize_graph(random_graph, node_colors)
