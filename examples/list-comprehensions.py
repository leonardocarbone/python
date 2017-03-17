# Example 1 - Convert Celsius to Fahrenheit
celsius = [0, 10, 20.1,34.5]
fahr = [ (temp * (9/5.0) + 32) for temp in celsius]
print fahr

# Example 2 - Nested list comprehensions
lst = [x**2 for x in [x**2 for x in range(11)]]
print lst

# Example 3
str = 'Create a list of the first letters of every word in this string'
lst = [letter[0] for letter in str.split()]
print lst

# Example 4 - Print all even number for 0 to 10
lst = [number for number in range(11) if number % 2 == 0]
print lst

# Example 5 - List of all number between 1 and 50 that are divisible by 3
lst = [number for number in range(1,51) if number % 3 == 0]
print lst