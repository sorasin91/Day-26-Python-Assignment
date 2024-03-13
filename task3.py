# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 3 Dictionary Operations
# done by Sora
# Write a Python function called merge_dicts that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, combine their values into a list.

# merge_dicts function
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            # If the value in the merged dictionary is already a list, append the new value
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                 # If the value is not a list, convert it to a list and append the new value
                merged_dict[key] = [merged_dict[key], value]
        else:
             # If the key is not present in the merged dictionary, add it with its value
            merged_dict[key] = value
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result_dict = merge_dicts(dict1, dict2)
print(result_dict)
