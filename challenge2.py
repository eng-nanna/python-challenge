'''The code aims to find the rare characters in a given string, or text file
We define a rare character to be one whose number of occurrences is less than any other'''
fhand = open('mess.txt')
inp = fhand.read()

from collections import Counter
'''A Counter is a dict subclass for counting hashable objects'''

c = Counter(inp)
counts = 0
for key in c:
    if c[key] == 1:
        counts +=1

print(c.most_common()[-1*(counts):])

'''Another solution'''
'''
s = ''.join([line.rstrip() for line in open('mess.txt')])    
OCCURRENCES = {}
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
avgOC = len(s) // len(OCCURRENCES)
print ([c for c in s if OCCURRENCES[c] < avgOC])'''