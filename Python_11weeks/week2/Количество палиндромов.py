k = int(input()) # считываем значение из условия
m = 0  # число - перевертыш
v = k  # копия к, которую мы будем резать на отдельные цифры, из которых составим число m
counter = 0  # кол-во палиндромов
while k != 0:  # перебираем числа от К до 0
    while v > 0:  # будем изменять число v, которое, как говорилось выше, является копией k
        m = m * 10 + v % 10  # по данной формуле составляем число - перевертыш
        v //= 10  # обрезаем одну цифру справа, чтобы перейти к следующему
    if m == k:  # проверяем, палиндром ли данное число
        counter += 1  # увеличиваем счетчик на 1 в случае успеха
    m = 0  # обнуляем значения
    v = k  # необходимо, чтобы начать проверять следующее число
    k -= 1  # переход к следующему числу
print(counter)
