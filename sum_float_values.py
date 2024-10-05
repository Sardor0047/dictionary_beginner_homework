def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    res = 0
    for i in data.keys():
        res += data[i]
    return res
result = sum_float_values({
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  })
print(result)