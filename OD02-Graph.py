class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # Для направленного графа удалите эту строку.

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]

# Пример использования:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("A", "C")

print(graph.adjacency_list)  # {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}

# Задача: Найти кратчайший путь между двумя вершинами в ненаправленном графе

def bfs_shortest_path(graph, start, goal):
    """
    Реализует поиск кратчайшего пути в графе между двумя вершинами с помощью BFS (поиск в ширину).

    :param graph: Экземпляр класса Graph, представляющий граф.
    :param start: Вершина, с которой начинается поиск.
    :param goal: Вершина, до которой нужно найти путь.
    :return: Список вершин, представляющий кратчайший путь от start до goal, или None, если путь не найден.
    """
    visited = set()  # Множество для отслеживания уже посещённых вершин
    queue = [[start]]  # Очередь путей; начинаем с пути, содержащего только стартовую вершину

    # Если начальная и целевая вершины совпадают, возвращаем их как путь
    if start == goal:
        return [start]

    while queue:
        # Берём первый путь из очереди
        path = queue.pop(0)
        # Последняя вершина в текущем пути
        vertex = path[-1]

        # Если вершина ещё не была посещена
        if vertex not in visited:
            # Получаем соседей текущей вершины
            neighbors = graph.adjacency_list[vertex]

            for neighbor in neighbors:
                # Создаём новый путь, добавляя текущего соседа
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)  # Добавляем новый путь в очередь

                # Если сосед — целевая вершина, возвращаем путь
                if neighbor == goal:
                    return new_path

            # Помечаем текущую вершину как посещённую
            visited.add(vertex)

    # Если очередь пуста и путь не найден, возвращаем None
    return None

# Пример использования:
# Создаём граф
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Добавляем рёбра (связи между вершинами)
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("A", "D")

# Печатаем кратчайший путь между двумя вершинами
print(bfs_shortest_path(graph, "A", "C"))  # ['A', 'B', 'C']
print(bfs_shortest_path(graph, "A", "E"))  # None, так как вершина 'E' не существует в графе


