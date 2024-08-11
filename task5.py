# Завдання 5. Візуалізація обходу бінарного дерева
# Використовуючи код із завдання 4 для побудови бінарного дерева,
# необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, node_colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()  # Очищуємо попередній графік
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.draw()  # Оновлюємо графік
    plt.pause(1)  # Пауза для візуалізації

def bfs(root):
    queue = deque([root])
    order = 0
    node_colors = {}
    
    while queue:
        current_node = queue.popleft()
        # Визначення кольору на основі порядку відвідування
        color_intensity = hex(int((255 - (order * 255 / 15))))[2:].zfill(2)
        node_colors[current_node.id] = f"#{color_intensity}{color_intensity}FF"
        
        draw_tree(root, node_colors)
        
        order += 1
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    plt.show()

def dfs(root):
    stack = [root]
    order = 0
    node_colors = {}
    
    while stack:
        current_node = stack.pop()
        # Визначення кольору на основі порядку відвідування
        color_intensity = hex(int((255 - (order * 255 / 15))))[2:].zfill(2)
        node_colors[current_node.id] = f"#{color_intensity}{color_intensity}FF"
        
        draw_tree(root, node_colors)
        
        order += 1
        
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Вибір типу обходу: bfs або dfs
traversal_type = input("Оберіть тип обходу (bfs або dfs): ").strip().lower()
plt.figure(figsize=(8, 5))  # Створюємо один графік для оновлення
if traversal_type == "bfs":
    bfs(root)
elif traversal_type == "dfs":
    dfs(root)
else:
    print("Некоректний вибір типу обходу")
