import math


def main():
    while True:
        print(" Choose task: "
              "\n1. Task 1\n2.Task2\n3.Task3\n4.Close")
        ch = int(input("Enter task "))

        if ch == 1:
            (task1())
        elif ch == 2:
            (task2())
        elif ch == 3:
            (task3())
        elif ch == 4:
            exit()


def task1():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if (num1 < num2 and num2 < num3):
        return num1 * 2, num2 * 2, num3 * 2
    else:
        return num1 * -1, num2 * -1, num3 * -1


def task2():
    try:
        x = float(input())
        y = float(input())
        r = float(input())

        sqrt = math.sqrt(2)

        if (y < 2 * r and x < 0 and x > -2 * r and y > 0 and pow(x - ((r * sqrt)/2), 2) + pow(
                (y - (r * sqrt/2)), 2) > pow(r, 2) and x + r * sqrt > y):
            return ("In")
        elif pow((x - ((r * sqrt) / 2)), 2) + pow((y - ((r *sqrt)/2)), 2) < pow(r,2) and x > 0 and y > 0 and x > y and x < (
                -y + ((2 * r * sqrt) / 2)):
            return ("In")
        else:
            return ("Out")
    except:
        print("Помилка")
        return 0

def task3():
    try:
        n = 1
        e = pow(10, 5)
        g = pow(10, -5)
        result = 0

        while result < e:
            result += factorial(n) / (5*n+2)
            print("Result is ")
            print(result)
            n += 1

        return result
    except:
        print("Помилка")
        return 0

def factorial(number):

    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


main()
