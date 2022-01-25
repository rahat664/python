import turtle

# turtle.shape("turtle")
# turtle.speed(1)
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)
result = 0
for i in range(50):
    result += 1
print(result)
for i in range(1, 50, 5):
    print(i)
for num in range(1, 100):
    if num % 5 == 0:
        print(num)
        result += num
print("sum is ", result)
