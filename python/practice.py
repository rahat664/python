import turtle


def draw_triangle(side_length):
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)


draw_triangle(100)
turtle.exitonclick()

str = "Hello Test!123 123, good."
cap_str = ""
low_str = ""
num_str = ""
special_str = ""
for c in str:
    if c.isupper():
        cap_str += c

    elif c.islower():
        low_str += c

    elif c.isnumeric():
        num_str += c

    else:
        special_str += c
print(special_str)
print(num_str)
print(low_str)
print(cap_str)

