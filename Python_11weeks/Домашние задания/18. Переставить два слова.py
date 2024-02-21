# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите
# в строку и выведите получившуюся строку. При решении этой задачи нельзя пользоваться циклами и инструкцией if.
# 
# Формат ввода
# 
# Вводится строка.
# 
# Формат вывода
# 
# Выведите ответ на задачу.
# 
# Примеры
# 
# Тест 1
# Входные данные:
# Hello, world!
# 
# Вывод программы:
# world! Hello,
# 
# 
# 
# Тест 2
# Входные данные:
# A B
# 
# Вывод программы:
# B A
# 
# 
# 
# Тест 3
# Входные данные:
# Q WERRTYUIOP
# 
# Вывод программы:
# WERRTYUIOP Q
s = str(input())
x = s.find(' ')
print(s[x+1:], s[:x])