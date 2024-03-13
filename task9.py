# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 9
# done by Sora
# Write a Python function called find_duplicates that takes a list of numbers as input and returns a list of all the duplicate numbers in the list.

def find_duplicates(numbers):
    # create an empty set to keep track of numbers inputs
    inputs = set()

    # create an empty set to store duplicate numbers
    duplicates = set()

    # loop through each number in the list
    for number in numbers:
        # check if the number is already in the 'inputs' set
        if number in inputs:
            # if yes, add it to the 'duplicates' set
            duplicates.add(number)
        else:
            # if not, add it to the 'inputs' set
            inputs.add(number)
    
    # convert the 'duplicates' set to a list and return it
    return list(duplicates)            

# data
numbers_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 5]  

# call the function
duplicates_numbers = find_duplicates(numbers_list)

# print the list of duplicate numbers
print(f'Duplicate numbers: {duplicates_numbers}')

