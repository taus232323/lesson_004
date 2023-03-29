# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_figures(point, sides, angle, color, size):
    angle_step = 360 / sides    # Принимает количество сторон и автоматически высчитывает нужный угол, чтобы фигура была без разрывов
    start_vector = sd.get_vector(start_point=point, angle=angle, length=size, width=3)
    start_vector.draw(color=color)     # Рисуем первый вектор
    current_vector = start_vector     # Назначаем точку рисования второго вектора
    for i in range(sides - 1):    # Цикл рисования следующих векторов
        current_vector = sd.get_vector(start_point=current_vector.end_point, angle=angle + angle_step * (i + 1),
                                   length=size, width=3)
        current_vector.draw(color=color)
    if current_vector.end_point != point:
        sd.line(start_point=current_vector.end_point, end_point=point, color=color, width=3)


colors_dict = {
    1: sd.COLOR_RED,
    2: sd.COLOR_ORANGE,
    3: sd.COLOR_YELLOW,
    4: sd.COLOR_GREEN,
    5: sd.COLOR_CYAN,
    6: sd.COLOR_BLUE,
    7: sd.COLOR_PURPLE
}

colors = {1: "Красный",
          2: "Оранжевый",
          3: "Жёлтый",
          4: "Зелёный",
          5: "Лиловый",
          6: "Голубой",
          7: "Фиолетовый"
}

print("Выберите цвет фигуры:")
for num, color in colors.items():
    print(f"{num}. {color}")

# запрашиваем у пользователя номер желаемого цвета
color_num = int(input())

# проверяем, что номер цвета в списке
if color_num not in colors_dict:
    print("Неверный номер цвета!")
else:
    # получаем название цвета
    color = colors_dict[color_num]
    sides_list = [3, 4, 5, 6]
    figure_coords = [(100, 100), (300, 100), (100, 300), (300, 300)]
    for i in range(len(sides_list)):
        point = sd.get_point(figure_coords[i][0], figure_coords[i][1])
        draw_figures(point=point, sides=sides_list[i], angle=0, color=color, size=100)


sd.pause()
