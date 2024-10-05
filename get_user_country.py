def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    res = data[0]
    for i in data:
        if i['name'] == name:
            res = i
    return res['name']
result = get_user_country([
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
],'Dustin')
print(result)