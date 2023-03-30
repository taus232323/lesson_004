# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_figures(point, sides, angle, color, size):
    angle_step = 360 / sides    # Принимает количество сторон и автоматически высчитывает нужный угол, чтобы фигура была без разрывов
    start_vector = sd.get_vector(start_point=point, angle=angle, length=size, width=3)
    start_vector.draw()     # Рисуем первый вектор
    current_vector = start_vector     # Назначаем точку рисования второго вектора
    for i in range(sides - 1):    # Цикл рисования следующих векторов
        current_vector = sd.get_vector(start_point=current_vector.end_point, angle=angle + angle_step * (i + 1), length=size, width=3)
        current_vector.draw()
    if current_vector.end_point != point:
        sd.line(start_point=current_vector.end_point, end_point=point, width=3)


figures_dict = {1: "Треугольник",
          2: "Квадрат",
          3: "Пятиугольник",
          4: "Шестиугольник",
}

print("Выберите фигуру:")
for num, figure in figures_dict.items():
    print(f"{num}. {figure}")

# запрашиваем у пользователя номер фигуры
figure_num = int(input())

# проверяем, что фигура в списке
if figure_num not in figures_dict:
    print("Неверный номер фигуры!")
else:
    figure = figure_num - 1
    sides_list = [3, 4, 5, 6]
    point = sd.get_point(300, 300)
    draw_figures(point=point, sides=sides_list[figure], angle=0, color=sd.random_color(), size=100)

sd.pause()
