from collections import OrderedDict

# Normal dictionary is just a mapping, does not retain the order
normal_dict = {}
normal_dict['a'] = 1
normal_dict['b'] = 2
normal_dict['c'] = 3

# No order here
print normal_dict # {'a': 1, 'c': 3, 'b': 2} 
for k,v in normal_dict.items():
  print k, "=>", v
  
normal_dict = OrderedDict()
normal_dict['a'] = 1
normal_dict['b'] = 2
normal_dict['c'] = 3

# Ordered values
print normal_dict # {'a': 1, 'c': 3, 'b': 2} 
for k,v in normal_dict.items():
  print k, "=>", v
