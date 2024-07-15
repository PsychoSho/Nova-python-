from turtle import *
def new_func():
    speed(8)
    color('cyan')
    bgcolor('black')
    i = 200
    while i>0:
        left(i)
        forward(i*3)
        i = i-1

new_func()
    