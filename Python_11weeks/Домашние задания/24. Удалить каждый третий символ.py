# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.Символы строки нумеруются, начиная с нуля.
# 
# Формат ввода
# 
# Вводится строка.
# 
# Формат вывода
# 
# Выведите ответ на задачу.
# 
# Примечания
# 
# Ввод и вывод осуществлять с помощью файлов
# 
# Примеры
# 
# Тест 1
# Входные данные:
# Python
# 
# Вывод программы:
# yton
# 
# 
# 
# Тест 2
# Входные данные:
# Hello
# 
# Вывод программы:
# elo
# 
# 
# 
# Тест 3
# Входные данные:
# qwer
# 
# Вывод программы:
# we
s = str(input())
s = s[1:]
x = len(s)
y = 2
while x >= 1:
    s = s[:y] + s[y+1:]
    x = x-1
    y = y + 2
print(s)