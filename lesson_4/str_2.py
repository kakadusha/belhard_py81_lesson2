"""
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое
"""

num_list = list(map(float, input("Введите несколько чисел через пробел:\n").split()))
print(f"Сумма чисел: {sum(num_list)}")
print(f"Максимальное число: {max(num_list)}")
print(f"Среднее арифметическое: {sum(num_list) / len(num_list)}")
