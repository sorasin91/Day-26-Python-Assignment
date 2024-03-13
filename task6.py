# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 6 Algorithm Implementation
# done by Sora
# Implement the bubble sort algorithm in Python to sort a list of integers in ascending order.

def bubbleSort(arr):
    """
    Sort a list of integers in ascending order using the bubble sort algorithm.

    Parameters:
    - arr: The list of integers to be sorted

    Returns:
    - None (the input list is modified in place)
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j], arr[j]

# Example usage:
numbersToSort = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(numbersToSort)
print("Sorted list:", numbersToSort)