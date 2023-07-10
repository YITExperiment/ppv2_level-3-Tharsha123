Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> 
>>> from itertools import cycle
>>> colors=cycle(['red','orange','yellow','green','blue',
... 'purple'])
>>> 
>>> 
>>> 
>>> def draw_circle(size,angle,shift):
...     turtle.bgcolor(next(colors))
...     turtle.pencolor(next(colors))
...     turtle.circle(size)
...     turtle.right(angle)
...     turtle.forward(shift)
...     draw_circle(size+5,angle+1,shift+1)
... 
...     
>>> turtle.bgcolor('black')
>>> turtle.speed('fast')
>>> turtle.pensize(40)
