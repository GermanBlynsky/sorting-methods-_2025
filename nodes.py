import random
import sys

def initialize_graph(nodes):
    graph = [[0] * nodes for _ in range(nodes)]
    
    for i in range(nodes):
        for j in range(i + 1, nodes):
            path = random.randint(0, 10)
            if path == 0:
                # 0 заменяем на 100 (аналог бесконечности)
                graph[i][j] = float('inf')
                graph[j][i] = float('inf')
            else:
                graph[i][j] = path
                graph[j][i] = path
    
    return graph

def optimize_path(graph):
    nodes = len(graph)
    
    for k in range(nodes):
        for i in range(nodes):
            for j in range(i, nodes):
                value = min(graph[i][j], graph[i][k] + graph[k][j])
                graph[i][j] = value
                graph[j][i] = value
    
    return graph

n = int(input("Введите количество вершин: "))
    
random.seed(1)
graph = initialize_graph(n)
    
print("\nИсходный граф (матрица смежности):")
for row in graph:
    print(' '.join(f'{val}' for val in row))
    
print("\nОптимизированные пути (кратчайшие расстояния):")
optimized_graph = optimize_path(graph)
for row in optimized_graph:
    print(' '.join(f'{val}' for val in row))
