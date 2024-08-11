# Завдання 7. Використання методу Монте-Карло
# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків,
# обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_simulations):
    results = {sum_val: 0 for sum_val in range(2, 13)}

    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        result_sum = die1 + die2
        results[result_sum] += 1

    probabilities = {sum_val: results[sum_val] / num_simulations for sum_val in results}
    return probabilities

def plot_results(probabilities):
    sums = list(probabilities.keys())
    probs = [probabilities[sum_val] * 100 for sum_val in sums]
    
    # Аналітичні ймовірності
    analytical_probs = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, width=0.4, label='Монте-Карло', align='center')
    plt.plot(sums, analytical_probs, 'r-', marker='o', label='Аналітичні')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()

# Виконання симуляції
num_simulations = 1000000  # Наприклад, 1 мільйон симуляцій
probabilities = monte_carlo_simulation(num_simulations)

# Відображення результатів
plot_results(probabilities)
