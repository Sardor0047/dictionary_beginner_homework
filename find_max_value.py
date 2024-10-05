def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    x = []
    for i in data.keys():
        x.append(data[i])
    max = x[0]
    for i in x :
        if i > max :
            max = i 
        
    return max
reslut = find_max_value({
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  })
print(reslut)