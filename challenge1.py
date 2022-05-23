''' The code aims to convert string to understood sentence by converting each character to next+2 character
ex: A is replaced by C, E is replaced by G, etc...'''

txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#txt = "map"
'''range(97,123) is the range of equivelant Ascii code for lowercase letters'''

'''new_txt = list(txt)

i = 0
while i < len(new_txt): 
    if ord(new_txt[i]) in range(97,123):
        if new_txt[i] == 'y':
            new_txt[i] = 'a'
        elif new_txt[i] == 'z':
            new_txt[i] = 'b'
        else:
            new_txt[i] = chr(ord(new_txt[i]) + 2)
    i += 1
'''


'''Another solution'''
ntxt = ""
for char in txt:
    if char.isalpha():
        if char == "y":
            ntxt += "a"
        elif char == "z":
            ntxt += "b"
        else:
            ntxt += chr(ord(char) + 2)
    else:
        ntxt += char

print(ntxt)


#print("".join(new_txt))


''' recommended solution '''

'''import string
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
table = text.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
newtxt = text.translate(table)
print(newtxt)'''