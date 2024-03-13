# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 2  List Operations
# done by Sora
# Write a Python function called find_average that takes a list of numbers as input and returns the average of those numbers.

# find_average function
def find_average(numbers):
    # check if list is empty
    if len(numbers) == 0:
        return 0
    # calculate average
    return sum(numbers) / len(numbers)

#result
print(find_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))