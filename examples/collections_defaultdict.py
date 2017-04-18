from collections import defaultdict

d = {'key1' : "Leo"}

print d["key1"]
#print d["key2"] # Raises a KeyError

d = defaultdict(object)
d["key1"] = "Test"
print d["key1"]
print d["key2"]

d = defaultdict(lambda: "python is cool! but the key does not exist!")
d["key1"] = "Test"
print d["key1"]
print d["key2"]
