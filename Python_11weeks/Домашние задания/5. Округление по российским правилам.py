# По российский правилам числа округляются до ближайшего целого числа,а если дробная часть числа равна 0.5, то 
# число округляется вверх. Дано неотрицательное число x, округлите его по этим правилам. Обратите внимание, что 
# функция round не годится для этой задачи!
# 
# Формат ввода
# 
# Вводится неотрицательное число.
# 
# Формат вывода
# 
# Выведите ответ на задачу.
# 
# Примеры
# 
# Тест 1
# Входные данные:
# 2.3
# 
# Вывод программы:
# 2
# 
# 
# 
# Тест 2
# Входные данные:
# 2.5
# 
# Вывод программы:
# 3
# 
# 
# 
# Тест 3
# Входные данные:
# 2.7
# 
# Вывод программы:
# 3
n = float(input())
if n - int(n) >= 0.5:
    x = int(n) + 1
else:
    x = int(n)
print(x)