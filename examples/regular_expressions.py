import re

def print_pattern(patterns, phrase):
  for pattern in patterns:
    print 'Searching the phrase using the %r' %pattern
    print re.findall(pattern, phrase)
    print '\n'
    
    
# Example 1
patterns = ['term1', 'term2']
print_pattern(patterns, 'This is a string with term1, but not the other term')

# Example 2 
match = re.search('term1', 'This is a string with term1, but not the other term')
print match.start()
print match.end()
print '\n'

# Example 3
split_term = "@"
phrase = "What is your email, is it hello@gmail.com?"
print re.split(split_term, phrase)
print '\n'

# Example 4
print re.findall('match', 'Here is one match, here is another match')
print '\n'

# Example 5 - Repetition Syntax

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]
                
print_pattern(test_patterns, test_phrase)
print '\n'  

# Example 6 - Character Sets
test_patterns = [ '[sd]',    # either s or d
                 's[sd]+']   # s followed by one or more s or d
                 
print_pattern(test_patterns, test_phrase)       
print '\n'

# Example 7 - Exclusion
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print re.findall('[^!.?]+', test_phrase)

# Example 8 - Character Ranges
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=[ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
print_pattern(test_patterns, test_phrase)
print '\n'
