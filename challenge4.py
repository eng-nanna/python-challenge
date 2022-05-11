'''this code aims to reach the final link in a chain of links that has the same pattern'''

import urllib.request

'''The first link in the chain'''

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

flag = True
while flag:
    '''openning the url and reading its contents'''
    f = urllib.request.urlopen(link)
    myfile = f.read()

    '''searching for the number and its position that will be replaced in the link'''
    pos = link.find("=")
    sliced_line = link[pos+1:]

    '''checking whether the content of the url has a number or not as this number will be used in the upcoming url'''
    new_num = [int(s) for s in myfile.split() if s.isdigit()]

    '''if the url content has no digit then the list will be empty 
    which leads to one the 2 cases:
    we reached to the page that asked for dividing the number by 2
    or the page that has the final page name'''
    if len(new_num)>0:
        num = new_num[0]
    else:
        '''looping over the url content to check if it asks for divide or has HTML page title'''
        for s in myfile.split():
            if s.decode('utf-8') == "Divide":
                num/=2
                break
            elif "html" in s.decode('utf-8'):
                '''changing the flag into false to break the loop as we reached to the final page name'''
                flag=False
                break
    
    '''replacing the number in current url with the number from the url content'''
    link = link.replace(sliced_line, str(num))

    print(link)
