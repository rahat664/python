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


def myfnc(x):
    print("inside myfunc", x)
    x = 10
    print("inside myfunc", x)


x = 20
myfnc(x)
print(x)


def myfnc2(y):
    print("y = ", y)
    print("x = ", x)


x = 20
myfnc2(x)


def myfnc3(x, y=10, z=0):
    print("x = ", x, "y = ", y, "z = ", z)


x = 5
y = 6
z = 7
myfnc3(x, y, z)
myfnc3(x, y)
myfnc3(x)


def myfnc4(x, z, y=10):
    print("x = ", x, "y = ", y, "z = ", z)


myfnc4(x=1, y=2, z=5)
a = 5
b = 6
myfnc4(x=a, z=b)


def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


result = add_numbers([1, 2, 30, 4, 5, 9])
print(result)