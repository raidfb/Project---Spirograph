import turtle
from math import cos,sin
from time import sleep

# Добавление объекта окно
window = turtle.Screen()

# Изменение bgcolor у объекта окно
window.bgcolor("#FFFFFF")

# 0 - режим отладки отрисовки выключен
window.tracer(0)

# Создание объекта спирограф
spirograph = turtle.Turtle()
spirograph.hideturtle() # Скрытие объекта спирограф
spirograph.speed(0) # Скорость, от 0.5 до 10
spirograph.pensize(2) # Размер диаметра круглой точки

# Создание объекта ручка
myPen = turtle.Turtle()
myPen.hideturtle() # Скрытие объекта ручка
myPen.speed(0) # Скорость, от 0.5 до 10
myPen.pensize(3) # Размер диаметра ручки
myPen.color("#AA00AA") # Цвет точки

R = 125
r = -45
d = 125

angle = 0

myPen.penup() # Поднятие пера
myPen.goto(R-r+d,0) # Перемещение по координатам x, y
myPen.pendown() # Опускание пера

theta = 0.2
steps = 8 * int(6*3.14/theta)

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup() # Поднятие пера
    spirograph.setheading(0) # Установка ориентации черепахи на градус
    spirograph.goto(0,-R) # Перемещение по координатам x, y
    spirograph.color("#999999")
    spirograph.pendown() # Опускание пера
    
    spirograph.circle(R) # Окружность с радиусом R
    
    angle+=theta
    
    x = (R - r) * cos(angle)
    y = (R - r) * sin(angle)
    
    spirograph.penup() # Поднятие пера
    spirograph.goto(x,y-r) # Перемещение по координатам x, y
    spirograph.color("#222222") # Изменение цвета у фигуры
    spirograph.pendown() # Опускание пера
    spirograph.circle(r) # Окружность с радиусом r
    spirograph.penup() # Поднятие пера
    
    spirograph.goto(x,y) # Перемещение по координатам x, y
    spirograph.dot(5) # Рисует круглую точку с диаметром 
    
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    spirograph.pendown() # Опускание пера
    spirograph.goto(x,y) # Перемещение по координатам x, y
    
    # spirograph.setheading((R-r)*degrees(angle)/r)
    # spirograph.forward(d)
    
    spirograph.dot(5) # Рисует круглую точку с диаметром 
    myPen.goto(spirograph.pos()) # Перемещение по координатам x, y 
    
    spirograph.getscreen().update() 
    sleep(0.005)

sleep(0.002)
#Hide Spirograph
spirograph.clear()
spirograph.getscreen().update()

window.mainloop()