a = float(input('vvedite a: '))
b = float(input('vvedite b: '))
c = float(input('vvedite c: '))

# Вычисляем дискриминант
D = b ** 2 - 4 * a * c

# Проверяем дискриминант
if D > 0:
    # У уравнения два корня
    x1 = (-b + (D ** 0.5)) / (2*a)
    x2 = (-b - (D ** 0.5)) / (2*a)
    print('ravny', x1, x2)
elif D == 0:
    # У уравнения один корень
    x = -b / (2*a)
    print('raven ', x)
