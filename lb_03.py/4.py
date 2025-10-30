import turtle
import random

def draw_circle():
    turtle.circle(30)

def draw_square():
    for _ in range(4):
        turtle.forward(60)
        turtle.right(90)

def draw_triangle():
    for _ in range(3):
        turtle.forward(70)
        turtle.left(120)

shapes = [draw_circle, draw_square, draw_triangle]

n = int(input("Скільки фігур намалювати: "))

for _ in range(n):
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
    turtle.pendown()
    random.choice(shapes)()

turtle.done()