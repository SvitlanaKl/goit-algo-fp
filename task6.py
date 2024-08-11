# Завдання 6. Жадібні алгоритми та динамічне програмування

# Частина 1: Реалізація жадібного алгоритму
def greedy_algorithm(items, budget):
    # Створюємо список страв, сортуємо за спаданням співвідношення "калорії/вартість"
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_cost, total_calories

# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Обрані страви: {greedy_result[0]}")
print(f"Загальна вартість: {greedy_result[1]}")
print(f"Загальна калорійність: {greedy_result[2]}")

# Частина 2: Реалізація алгоритму динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_names = list(items.keys())

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо вибір страв
    w = budget
    selected_items = []
    total_cost = 0
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_names[i - 1]
            selected_items.append(item)
            total_cost += items[item]['cost']
            w -= items[item]['cost']

    return selected_items, total_cost, total_calories

# Приклад використання:
dp_result = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print(f"Обрані страви: {dp_result[0]}")
print(f"Загальна вартість: {dp_result[1]}")
print(f"Загальна калорійність: {dp_result[2]}")
