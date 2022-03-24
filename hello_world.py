import turtle

screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Drawing a Pizza")

my_turtle = turtle.Turtle()
my_turtle.pensize(15)
my_turtle.shape("circle")


for x in range(0,72):
    my_turtle.forward(100)
    my_turtle.backward(100)
    my_turtle.right(5)


