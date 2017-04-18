from collections import Counter

# Example 1 - Count how many times a number appear on the list
list = [1,2,3,1,3,2,1]
print Counter(list) # results Counter({1: 3, 2: 2, 3: 2})

# Example 2 - Count how many times does each word show up in this sentence
text = "How many times does each word show up in this sentence. Word show up"
words = text.split()
print Counter(words) # results Counter({'show': 2, 'up': 2, 'word': 1, 'this': 1, 'many': 1, 'sentence.': 1, 'in': 1, 'times': 1, 'How': 1, 'does': 1, 'each': 1, 'Word': 1})

# Example 3 - Show commom Word
words = Counter(words)
print words.most_common(1) # results [('show', 2)]

# Example 4 - Count the words on the sentence
print sum(words.values())


# Example 5 - List unique elements
lst = [1,2,3,1,4]
print list(Counter(lst))

