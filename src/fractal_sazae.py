from turtle import Turtle, Screen
from src.draw_sazae import  draw_sazae
screen = Screen()
screen.setup(1000,1000)
screen.tracer(50,0)
gamera = Turtle()
gamera.reset()
gamera.speed(0)
gamera.left(90)
max_depth = 3
draw_sazae(gamera, 0, max_depth)
screen.exitonclick()