from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Creating a ChainMap
chain = ChainMap(dict1, dict2)

print(chain['a'])  # Output: 1 (found in dict1)
print(chain['b'])  # Output: 2 (found in dict1, as it's searched first)
print(chain['c'])  # Output: 4 (found in dict2)

# Adding a new key to dict1
dict1['d'] = 5
print(chain['d'])  # Output: 5 (reflects change in dict1)
