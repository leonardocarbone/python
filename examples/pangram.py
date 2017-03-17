# Function that checks whether a passed string is a pangran or not.

import string

def is_pangram(str, alphabet=string.ascii_lowercase):
    str = list(set(str.lower().replace(" ","")))
    
    aux = [a for a in alphabet if a in str]
    return len(aux) == len(alphabet)

print is_pangram('The quick brown fox jumps over the lazy dog')