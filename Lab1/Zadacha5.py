number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))

# Используем множество (set) для определения уникальных чисел
unique_numbers = set([number1, number2, number3])

# Определяем количество совпадающих чисел
count_unique = len(unique_numbers)

if count_unique == 3:
    print(0)
elif count_unique == 2:
    print(2)
else:
    print(3)