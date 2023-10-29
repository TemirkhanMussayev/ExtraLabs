# Ввод номера урока
lesson_number = int(input())

# Рассчитываем общую продолжительность уроков и перемен
total_minutes = lesson_number * 45 + (lesson_number // 2) * 5 + ((lesson_number - 1) // 2) * 15

# Рассчитываем часы и минуты окончания урока
end_hour = 9 + total_minutes // 60
end_minute = total_minutes % 60

# Выводим результат
print(end_hour, end_minute)