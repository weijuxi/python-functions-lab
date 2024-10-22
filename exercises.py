# def do_nothing():
#     print("=======================")
#     print("Insert banner text here")
#     print("=======================")
    
# do_nothing()
    
# def print_banner(text):
#     print("=======================")
#     print(text)
#     print("=======================")
    
# print_banner("Insert banner text here")

# def sum(greeting, *args):
#     print(greeting)
#     # prints: Hello, friend
#     total = 0
    
#     for arg in args:
#         total += arg

#     return total

# print(sum("Hello, friend", 1, 5, 10))

# def make_employee(role):
#     print(role)
#     # prints: CEO

#     employee = {"role": role}
#     return employee

# print(make_employee("CEO"))
# # prints: { 'role': 'CEO' }

# def make_employee(role, **kwargs):
#     # print(kwargs)
#     # # prints: {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
#     # print(type(kwargs))
#     # prints: <class 'dict'>
#     # kwargs is a dictionary - you can use it anywhere you'd use one:
#     employee = {"role": role, "name": kwargs}
#     return employee

# print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))
# # prints: {
# #     'role': 'CEO',
# #     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# # }


# def make_employee(role, **kwargs):
#     username = ""
#     for name in kwargs.values():
#         username += name

#     employee = {"role": role, "username": username}
#     return employee

# print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))

# def arg_demo(pos1, pos2, *args, **kwargs):
#     print(f'Positional params: {pos1}, {pos2}')
#     print('*args:')
#     for arg in args:
#         print(' ', arg)
#     print('**kwargs:')
#     for keyword, value in kwargs.items():
#         print(f'  {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')


# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.
def calculate_area_triangle(base, height):
    return (base * height) / 2



print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print('Exercise 2:', simple_interest(1000, 5, 2))



# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.
def apply_discount(price, discount):
    return price - (price * discount / 100)


print('Exercise 3:', apply_discount(100, 25))



# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.
def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32
    elif unit == 'F':
        return (temp - 32) * 5/9
    else:
        return 'Invalid unit'


print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))



# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print('Exercise 5:', sum_to(6))



# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest(a, b, c):
    return max(a, b, c)


print('Exercise 6:', largest(1, 2, 3))



# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.
def calculate_tip(bill, tip_percent):
    return bill * (tip_percent*0.01)


print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.
def product(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.
def basicCalculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return 'Invalid operation'


print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))
