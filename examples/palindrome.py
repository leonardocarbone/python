# Function that checks whether a passed string is palindrome or not

def is_palindrome(str):
    str = str.replace(" ","")
    return str[::-1] == str

print is_palindrome("nurses run")