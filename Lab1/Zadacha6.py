
# Считываем три целых числа
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

# Используем функцию min() и max() для нахождения минимального и максимального значения
min_value = min(a, b, c)
max_value = max(a, b, c)

# Вычисляем среднее значение (необходимое для нахождения числа, которое осталось)
middle_value = a + b + c - min_value - max_value

# Выводим числа в порядке неубывания
print(min_value)
print(middle_value)
print(max_value)