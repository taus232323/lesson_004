# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resoluton = (1200, 600)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

root_point = sd.get_point(300, 30)
def draw_brunches(start_point, angle, length):
    if length < 2:
        return
    branch1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    branch1.draw()
    next_point = branch1.end_point
    deviation_length = random.uniform(-0.2, 0.2) * 0.75 * length
    next_length = length * .75
    draw_brunches(start_point=next_point, angle=angle - sd.random_number(15, 45),
                  length=next_length + deviation_length)
    draw_brunches(start_point=next_point, angle=angle + sd.random_number(15, 45),
                  length=next_length + deviation_length)



draw_brunches(start_point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
sd.random_number()

sd.pause()


