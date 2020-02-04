"""Dictionary Views

This sample shows the creation of a small dictionary, how you iterate
though it and how you create views into it.  Views are not separate
copies of the data.
"""

dc = {'a': 5, 'b': 12, 'c': 1, 'd': 57}
print(dc)
for i in dc:
    print(i, dc[i])
print()
# Create three views into the dictionary
dc_keys = dc.keys(); dc_values = dc.values(); dc_items = dc.items()
print(list(dc_keys))  
print(list(dc_values))   
print(list(dc_items))   
print()
del dc['b']
print(list(dc_keys))  
print(list(dc_values))   
print(list(dc_items))   

for i, j in dc.items():  # A view is iterable
    print(i, j)
    

