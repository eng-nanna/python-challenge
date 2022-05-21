'''This challenge aims to collect comments from files of the downloaded zipped floder
    and to get the word used in next URL from them
'''

from zipfile import ZipInfo
import zipfile, zipfile

'''with zipfile.ZipFile('channel.zip') as z:
    filename = "90052.txt"
    txtfile = z.read(filename)
    print( txtfile)
    while filename in z.namelist():
        txtfile = z.read(filename)
        new_num = [int(s) for s in txtfile.split() if s.isdigit()]
        if len(new_num)>0:
            filename=str(new_num[0])+".txt"
            txtfile = z.read(filename)
            print(txtfile)
        else:
            break'''

with zipfile.ZipFile('channel.zip') as z:
    filename = "90052.txt"
    txtfile = z.read(filename)
    txt=z.getinfo(filename).comment.decode('utf-8')
    while filename in z.namelist():
        txtfile = z.read(filename)
        new_num = [int(s) for s in txtfile.split() if s.isdigit()]
        if len(new_num)>0:
            filename=str(new_num[0])+".txt"
            txtfile = z.read(filename)
            txt+=z.getinfo(filename).comment.decode('utf-8')
        else:
            break
    print(txt)
