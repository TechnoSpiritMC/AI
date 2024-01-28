import turtle
from turtle import *
import random


def parseSeed(seed):
    _seed = []
    for char in str(seed):
        _seed.append(True if char == "1" else False)
    return _seed


def levelGenerator(size=1):
    tracer(False)
    penup()
    pensize(1 * size)
    hideturtle()
    goto(-160 * size, 110 * size)
    speed(0)
    _seed = ""

    color('purple')
    for i in range(32):
        for j in range(22):
            pendown() if random.choice([True, False]) else penup()

            if isdown():
                _seed = _seed + "1"
            else:
                _seed = _seed + "0"

            goto(-(160 * size) + (10 * size * i), 110 * size - (j * (10 * size)))
        penup()
        goto((-(160 * size) + (10 * size * i)) + 10 * size, 110 * size)

    penup()
    color('orange')
    for i in range(22):
        for j in range(32):
            pendown() if random.choice([True, False]) else penup()

            if isdown():
                _seed = _seed + "1"
            else:
                _seed = _seed + "0"
            goto(-(160 * size) + (j * 10 * size), 110 * size - (i * (10 * size)))

        penup()
        goto(-(160 * size), (110 * size - (10 * size * i)) + 10 * size)

    return _seed



print(parseSeed(levelGenerator(2)))
turtle.exitonclick()
