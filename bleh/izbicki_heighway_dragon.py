#Szymon Izbicki

import turtle

#turtle setup
turtle.speed(0)
turtle.pencolor("purple")
turtle.hideturtle()

route = [0,1]

#screen setup
screen = turtle.Screen()
screen.bgcolor("black")

def heighway_dragon(route):
    new_route = []
    new_route.extend(route)
    for i in range(len(route)):
        if route[i] == 0:
            turtle.forward(5)
            new_route.append(0)
        if route[i] == 1:
            turtle.right(90)
            new_route.append(1)
    new_route.append(1)
    return heighway_dragon(new_route)


heighway_dragon(route)
