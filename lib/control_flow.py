#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    if temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    if temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    
    else:
        return num

def calculator(operation, num1, num2):
    dict_map = {
        "+": lambda num1,num2: num1 + num2,
        "-": lambda num1,num2: num1 - num2,
        "*": lambda num1,num2: num1 * num2,
        "/": lambda num1,num2: num1 / num2 if num2 != 0 else "Ragnorak"
    }
    if operation in dict_map:
        return dict_map[operation](num1,num2)
    else:
        print("Invalid operation!")
        return None
    pass
