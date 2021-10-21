from turtle import Turtle, Screen
from src.draw_sazae import  draw_sazae
screen = Screen()
screen.setup(700,700)
screen.tracer(100,0)
gamera = Turtle()
gamera.hideturtle()
gamera.speed(0)
gamera.left(90)
gamera.penup()
gamera.goto(0,-200)
max_depth = 2
draw_sazae(gamera, 0, max_depth,0)
screen.exitonclick()