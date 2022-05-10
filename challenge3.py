'''This code aims to find the lowercase character that's surrounded by exactly 3 uppercase letters from both sides (left and right) in a given string or text file'''
fhand = open('bodyguards.txt')
inp = fhand.read()

'''function to convert string into list'''
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

new_txt = Convert(inp)
i = 0
upper_count = 0
final= []

while i < len(new_txt):
    if new_txt[i].isupper():
        upper_count +=1
    elif new_txt[i].islower():
        '''checking if lowercase character found and has 3 uppercase letters before it'''
        if upper_count == 3:
            j = i+1
            after_upper = 0
            '''check if the 4 upcoming letters are uppercase or not '''
            while j < i+5 and j < len(new_txt):
                if new_txt[j].isupper():
                    after_upper +=1
                else:
                    break
                j+=1
            if after_upper == 3 and upper_count == 3:
                #print(new_txt[i-4:i+4])
                
                final.append(new_txt[i])
            after_upper = 0
        upper_count = 0
    i += 1

final_txt = ""

'''convert list to a string'''
for x in final:
    final_txt += x
print(final_txt)


'''Recommended solution - simple using regex'''

'''
fhand = open('bodyguards.txt')
inp = fhand.read()
import re
"".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', inp))
'''

