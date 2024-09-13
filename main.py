from turtle import Turtle, Screen
tim = Turtle()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_leftward():
    tim.left(10)
def move_rightward():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="W".lower())
screen.onkey(fun=move_backward, key="S".lower())
screen.onkey(fun=move_leftward, key="A".lower())
screen.onkey(fun=move_rightward, key="D".lower())
screen.onkey(fun=clear, key="C".lower())
screen.exitonclick()