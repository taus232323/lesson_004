# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# point = sd.get_point(300, 300)
# angle = 45
# def triangle(point, angle, length):
#     t1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     t1.draw()
#
#     t2 = sd.get_vector(start_point=t1.end_point, angle=angle - 90, length=length, width=3)
#     t2.draw()
#
#     t3 = sd.get_vector(start_point=t2.end_point, angle=angle - 225, length=length * 1.4, width=3)
#     t3.draw()
#
#
# triangle(point=point, angle=angle, length=100)

# - квадрата


# def square(point, angle=0, size=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=size, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=size, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=size, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=size, width=3)
#     v4.draw()
#
#
# point_0 = sd.get_point(300, 300)
# angle = 0
# square(point=point_0, angle=angle, size=200)

# - пятиугольника
# def pentagon(point, angle=0, size=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=size, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=size, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=size, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=size, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=size, width=3)
#     v5.draw()
#
#
# point_0 = sd.get_point(200, 200)
# angle = 0
# pentagon(point=point_0, angle=angle, size=200)

# - шестиугольника

# def hexagon(point, angle=0, size=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=size, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=size, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=size, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=size, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=size, width=3)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=size, width=3)
#     v6.draw()
#
#
# point_0 = sd.get_point(200, 200)
# angle = 0
# hexagon(point=point_0, angle=angle, size=200)

# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def draw_figures(point, sides, angle, size):
    angle_step = 360 / sides    # Принимает количество сторон и автоматически высчитывает нужный угол, чтобы фигура была без разрывов
    start_vector = sd.get_vector(start_point=point, angle=angle, length=size, width=3)
    start_vector.draw()     # Рисуем первый вектор
    current_vector = start_vector     # Назначаем точку рисования второго вектора
    for i in range(sides - 1):    # Цикл рисования следующих векторов
        current_vector = sd.get_vector(start_point=current_vector.end_point, angle=angle + angle_step * (i + 1), length=size, width=3)
        current_vector.draw()
    if current_vector.end_point != point:
        sd.line(start_point=current_vector.end_point, end_point=point, width=3)



sides_list = [3, 4, 5, 6]
figure_coords = [(100, 100), (300, 100), (100, 300), (300, 300)]
for i in range(len(sides_list)):
    point = sd.get_point(figure_coords[i][0], figure_coords[i][1])
    draw_figures(point=point, sides=sides_list[i], angle=0, size=100)





# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
