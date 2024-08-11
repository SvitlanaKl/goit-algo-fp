# Завдання 3. Дерева, алгоритм Дейкстри
# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу.
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин
# та обчислення найкоротших шляхів від початкової вершини до всіх інших.


import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней до вершин (безкінечність) і батьківських вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # Користуємось heapq як чергою з пріоритетом
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Перевірка наявного шляху до вершини
        if current_distance > distances[current_vertex]:
            continue

        # Перебір сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад створення графа
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Вказуємо стартову вершину
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print("Найкоротші шляхи від вершини", start_vertex)
for vertex, distance in shortest_paths.items():
    print(f"До вершини {vertex}: {distance}")
