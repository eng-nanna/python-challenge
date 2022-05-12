from fileinput import filename
''' this code is to read banner.p pickled file from the server then invistagte its content to get teh upcomming url of the challenge'''

import pickle
import urllib.request

new_lsts = pickle.load(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))

print(new_lsts) 
''' the content turns out to be list of list of tuples containing spaces and hashes paired with numbers
we can draw the ward we are seeking for by multiplying the number to its symbol in each line/list'''

'''for lsts in new_lsts:
    #an empty string to join characters form each single line/list
    str = ""
    for lst in lsts:
        res = 1
        for l in lst:
            #multiplying the character to its paired number
            res *= l
        str+=res
    print(str)'''


'''Recommended solution'''
for line in new_lsts:
    print ("".join(map(lambda pair: pair[0]*pair[1], line)))