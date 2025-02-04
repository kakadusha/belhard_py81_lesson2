"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

# переменные
a1 = 1.1
a2 = 2
a3 = "3.3"
a4 = 4

# тесты
print(
    "Все переменные дробные числа: ",
    all(map(lambda x: isinstance(x, float), [a1, a2, a3, a4])),
)

print(
    "Одна из переменных это строка: ",
    any(map(lambda x: isinstance(x, str), [a1, a2, a3, a4])),
)
pairs = [(a1, a3), (a2, a4), (a3, a4)]
print(
    "Одна пара переменных является целочисленным_и тип_ами: ",
    any(map(lambda x: isinstance(x[0], int) and isinstance(x[1], int), pairs)),
)
