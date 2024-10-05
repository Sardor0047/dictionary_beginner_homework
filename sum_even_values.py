def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    res = 0
    for i in data.keys():
        if data[i] % 2 == 0:
            res+=data[i]
    return res
res = sum_even_values({
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  })
print(res)