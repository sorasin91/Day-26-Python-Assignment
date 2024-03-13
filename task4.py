# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 4 Error Handling
# done by Sora
# Write a Python function called divide_numbers that takes two numbers as input and returns the result of dividing the first number by the second number. Handle the ZeroDivisionError exception appropriately.

# divided_numbers function
def divide_numbers(num1, num2):
    try:
        result = num1/num2
        return result
    
    except ZeroDivisionError:
        print("Error: Divide by zero")

# result
result = divide_numbers(10,0)
print(result)