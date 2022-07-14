from math import pi, sin, cos
import turtle

totalSteps = int(input('Steps: '))
modulo = int(input('Modulo '))
twopi = 2*pi

t = turtle.Turtle()
t.speed(0)
t.color('white')
t.hideturtle()

radius = 200
turtle.screensize(canvwidth = 2*radius, canvheight = 2*radius, bg='black')

for i in range(totalSteps):
  angles = (twopi*i / totalSteps, modulo * twopi*i / totalSteps)
  t.up()
  t.goto(radius*cos(angles[0]), radius*sin(angles[0]))
  t.down()
  t.goto(radius*cos(angles[1]), radius*sin(angles[1]))
