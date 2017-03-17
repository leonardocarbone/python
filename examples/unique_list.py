# Function that takes a list and returns a new list with unique elements of the first list.

def unique(list_values):    
    return list(set(list_values))

print unique([1,1,1,1,2,2,3,3,3,3,4,5])