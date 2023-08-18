# Задача 3: Вычисление факториала числа. Напишите программу, которая находит факториал заданного числа N с использованием рекурсии или встроенных функций.

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = 3
print(f"Факториал {number} = {factorial(number)}")