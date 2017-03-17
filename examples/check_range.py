# Function that checks whether a number is in a given range (Inclusive of high and low)

def check_range(value, low, high):
    return value in range(low, high+1)

print check_range(11,3,10)