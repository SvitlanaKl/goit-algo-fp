# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
# Написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
# Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

from turtle import Turtle, Screen, done
import math

def draw_pythagorean_tree(t, length, depth):
    """Функція для малювання дерева Піфагора."""
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return
    
    # Малювання основного стовбура
    t.forward(length)
    
    # Збереження поточної позиції та орієнтації Turtle
    x, y = t.position()
    angle = t.heading()
    
    # Малювання лівого квадрата
    t.left(45)
    draw_pythagorean_tree(t, length / math.sqrt(2), depth - 1)
    
    # Повернення до поточної позиції і орієнтації
    t.setposition(x, y)
    t.setheading(angle)
    
    # Малювання правого квадрата
    t.right(45)
    draw_pythagorean_tree(t, length / math.sqrt(2), depth - 1)
    
    # Повернення до початкового положення
    t.setposition(x, y)
    t.setheading(angle)
    t.backward(length)

if __name__ == '__main__':
    # Налаштування екрану та кольорів
    screen = Screen()
    screen.title("Pythagorean Tree Fractal")
    screen.setup(width=800, height=800)
    screen.tracer(0)  # Вимкнення автоматичного оновлення екрану
    
    # Зчитування рівня рекурсії з консолі
    try:
        level = int(input("Введіть рівень рекурсії: "))
        if level < 0:
            raise ValueError("Рівень рекурсії не може бути від'ємним.")
    except ValueError as e:
        print(f"Помилка вводу: {e}")
        done()
        exit()

    # Налаштування Turtle
    t = Turtle()
    t.color('red')
    t.speed(0)  # Найшвидша швидкість малювання
    t.penup()
    t.goto(0, -300)  # Переміщення в початкове положення
    t.pendown()
    t.left(90)  # Направлення Turtle вгору

    # Малювання дерева
    draw_pythagorean_tree(t, 200, level)
    
    # Оновлення екрану вручну
    screen.update()
    
    # Завершення малювання і закриття вікна
    done()

