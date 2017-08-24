import turtle

def draw():
    window = turtle.Screen()
    #window.bgcolor("red")
    draw_flower()
    #draw_square()

    #draw_circle()

    #draw_triangle()
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)
    for i in range(1, 5):
        brad.forward(100)
        brad.right(90)
        i += 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("yellow")
    angie.speed(1)
    angie.circle(100)

def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("turtle")
    triangle.color("green")
    triangle.speed(1)
    for i in range(1, 50):
        triangle.forward(100)
        triangle.right(150)
        i += 1

def draw_flower():
    flower = turtle.Turtle()
    flower.color("blue")
    for i in range(1, 75):
        flower.forward(80)
        flower.right(30)
        flower.forward(25)
        flower.right(160)
        flower.forward(25)
        flower.right(25)
        i += 1

    flower.right(180)
    flower.forward(80)

draw()