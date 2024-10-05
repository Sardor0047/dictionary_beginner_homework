def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    res = []
    for i in data.keys():
        res.append(i)
    min = res[0]
    for i in res:
        if i > min:
            min = i
    return min
result = find_max_key({
    1: 'a', 
    2: 'b', 
    3: 'c'
  })
print(result)