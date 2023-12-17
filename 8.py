import random
import matplotlib.pyplot as plt

def generate_random_bipartite_graph(nodes1, nodes2, probability):
    graph = {}

    for node1 in nodes1:
        graph[node1] = []
        for node2 in nodes2:
            if random.random() < probability:
                graph[node1].append(node2)

    return graph


nodes1 = ['A', 'B', 'C']
nodes2 = [1, 2, 3, 4]
probability = 0.5

bipartite_graph = generate_random_bipartite_graph(nodes1, nodes2, probability)


for node in bipartite_graph:
    print(node, '->', bipartite_graph[node])


for node1 in nodes1:
    for node2 in bipartite_graph[node1]:
        plt.plot([node1, node2], [0, 1], 'bo-')  # Plotting edges between nodes of different partitions
plt.yticks([0, 1], ['Partition 1', 'Partition 2'])
plt.show()
