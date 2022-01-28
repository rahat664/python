import turtle


def add(num1, num2):
    return num1 + num2


n = 10
m = 5
result = add(n, m)
print(result)

number1 = 10
number2 = 10
result = add(number1, number2)
print(result)

n1 = 20
n2 = 10
print(add(number1, number2))

print(add(2.5, 3.5))


def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


counter = 0

while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()


def myfnc(x):
    print("inside myfunc", x)
    x = 10
    print("inside myfunc", x)


x = 20
myfnc(x)
print(x)
