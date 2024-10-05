def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    count = 0
    for i in data.keys():
        count += data[i]
    return count
result = sum_dict_values({
    'a': 1, 
    'b': 2, 
    'c': 3
  })
print(result)