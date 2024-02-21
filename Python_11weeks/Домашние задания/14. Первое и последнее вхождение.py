# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. Если она встречается два 
# и более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается, ничего
# не выводите. При решении этой задачи нельзя использовать метод count и циклы.
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
# comfort
# 
# Вывод программы:
# 3
# 
# 
# 
# Тест 2
# Входные данные:
# office
# 
# Вывод программы:
# 1 2
# 
# 
# 
# Тест 3
# Входные данные:
# hello
# 
# Вывод программы:
#
s = str(input())
b = s[::-1]
if s.find('f') == -1:
    print()
elif s.find('f') == (len(s) - b.find('f') - 1):
    print(s.find('f'))
else:
    print(s.find('f'))
    print(len(s) - b.find('f') - 1)