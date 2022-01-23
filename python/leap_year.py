year = input("Please input the year: ")
year = int(year)
if year % 4 != 0:
    print("No")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
