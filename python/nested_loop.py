import turtle

turtle.color("black")
turtle.speed(5)
# for side_length in range(50, 100, 10):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1
turtle.exitonclick()
