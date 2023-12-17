import networkx as nx
import matplotlib.pyplot as plt

def generate_fully_connected_graph(num_vertices):
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    adjacency_list = {vertex: [] for vertex in range(num_vertices)}

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
           
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1
            
           
            adjacency_list[i].append(j)
            adjacency_list[j].append(i)

    return adjacency_list, adjacency_matrix

num_vertices = 4
adj_list, adj_matrix = generate_fully_connected_graph(num_vertices)


print("Список смежностей:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex} : {neighbors}")


print("Матрица смежностей:")
for row in adj_matrix:
    print(row)

# Визуализация
G = nx.Graph()


for vertex, neighbors in adj_list.items():
    for neighbor in neighbors:
        G.add_edge(vertex, neighbor)


plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
plt.title("Полносвязный граф: ")
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', font_size=12)

plt.show()
