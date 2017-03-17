# Example 1 - Iterate through a string
string = raw_input("Enter a word: ")
for char in string:
    print(char* 2)    

# Example 2 - Iterate through dictionary
dic = {"name" : "Leonardo", "age" : 35, "surname" : "Carbone"}

# Python 2
for (k,v) in dic.iteritems(): 
    print k,"=>",v

# Python 3
for (k,v) in dic.items():
    print(k,"=>",v)

# Example 3 - Odd/Even    
number = input('Enter a range value: ')
for n in range(number):
    if n % 2 == 0:
        print 'Number %s is even' %(n)
    else:
        print 'Number %s is odd' %(n)

# Example 4 - Tuples
tup = [(2,3), (10,21), (12,1)]
print tup
for t in tup:
    print t

for (t1,t2) in tup:
    print "{0} => {1}".format(t1,t2)        

# Example 5
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print word


