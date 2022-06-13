from re import L
from PIL import Image
from collections import defaultdict

img = Image.open("oxygen.png") 

lst = []

for x in range(img.width):
    lst.append(img.getpixel((x, img.height / 2)))

nlst = lst[::7]
nstr = ""

for l in nlst:
    r,b,g,a = l
    if r == g == b:
        nstr += (chr(r))

print(nstr)

pos = nstr.find("[")
sliced_line = nstr[pos+1:-1]
sliced_line = sliced_line.split(", ")

for num in sliced_line:
    print((chr(int(num))),end='')