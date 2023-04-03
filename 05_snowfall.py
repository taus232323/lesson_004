# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (600, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# Список точек, в которых будут появляться снежинки
# Create empty dictionary for snowflakes' data
snowflakes = {}
# Add variable in range of snowflakes quantity
for i in range(N):
    # Assign key in dictionary with name of cicle's variable
    snowflakes[i] = {}
    # Assign range of os "x"
    snowflakes[i]['x'] = sd.random_number(50, 550)
    # Assign os "y"
    snowflakes[i]['y'] = 600
    # assign form of snowflakes
    snowflakes[i]['length'] = sd.random_number(10, 30)
    snowflakes[i]['factor_a'] = sd.random_number(2, 4)/5
    snowflakes[i]['factor_b'] = sd.random_number(3, 4)/10
    snowflakes[i]['factor_c'] = sd.random_number(45, 75)
    # assign speed of snowflakes
    snowflakes[i]['speed'] = sd.random_number(5, 10)
# ?
flag_of_stop = False

while True:     #draw snowflakes limitless
    sd.start_drawing()
    for i, snowflake_item in snowflakes.items():    # variables to work with snowflake dictionary
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])  #get point for center of snowflakes
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'],
                     color=sd.background_color)     #draw snowflake with background color
        snowflake_item['y'] -= snowflake_item['speed']  #substarction assigned quantity from "y"
        snowflake_item['x'] += sd.random_number(-15, 15)    #move snowflake in "x" with assigned range
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])      #new point for snowflake
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])      # new snowflake
        if snowflake_item['y'] < 50:    # if snowflake have flown to "y" = 50 - stop moving
            sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                         factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c']) # draw snowflake at the bottom of screen
            snowflake_item['y'] = 600 # start drawing new snowflake at the top of screen
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


