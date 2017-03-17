# Function that accepts a string and calculate the number of upper case letters and lower case letters.
import string

def check_string(str):
    print str
    print "Upper Count: ", len([s for s in str if s in string.ascii_uppercase])
    print "Lower Count: ", len([s for s in str if s in string.ascii_lowercase])
    

check_string('Hello Mr. Rogers, how are you this fine Tuesday?')