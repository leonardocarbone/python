# Function to multiply all the numbers in a list.

def mult(list_values):
    result = 1
    for x in list_values:
        result*=x

    return result


print mult([2,3,-4])