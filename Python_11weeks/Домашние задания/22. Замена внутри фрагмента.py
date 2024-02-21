# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
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
# In the hole in the ground there lived a hobbit
# 
# Вывод программы:
# In the Hole in tHe ground tHere lived a hobbit
# 
# 
# 
# Тест 2
# Входные данные:
# qwertyhahsdhfghzxcvb
# 
# Вывод программы:
# qwertyhaHsdHfghzxcvb
# 
# 
# 
# Тест 3
# Входные данные:
# asdfghhzxcvb
# 
# Вывод программы:
# asdfghhzxcvb
s = str(input())
x = s.find('h')
y = s.rfind('h')
z = s[x+1:y].replace('h','H')
print(s[:x+1] + z + s[y:])
