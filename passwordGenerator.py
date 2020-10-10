import itertools
import argparse


_doc = """(REQUIRED) Possible options for password combination type:
1 :  Combination Alphnumeric .
2 :  Combination Character only .
3 :  Combination Special Character Only .
4 :  Combination Special Character and number only .
5 :  Combination Alphanumeric Special Character .
"""
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-p',action='store',dest='possibleCombo',help="Number of characters in password (DEFAULT = 3)",type=str,default=3)
parser.add_argument('-c',action='store',dest='combinationType',help=_doc,type=str,required=True)




special = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
numeric = '0123456789'
carecter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = parser.parse_args()

possibleCombo = password.possibleCombo

if password.combinationType == '1':
    getCarecter = numeric + carecter
elif password.combinationType == '2':
    getCarecter = numeric
elif password.combinationType == '3':
    getCarecter = carecter
elif password.combinationType == '4':
    getCarecter = special
elif password.combinationType == '5':
    getCarecter = special + numeric
elif password.combinationType == '6':
    getCarecter = special + numeric + carecter
else:
    exit("Bad Input")

def generatePass(l):
    yield from itertools.product(*([l] * int(possibleCombo))) 

count = 0
for x in generatePass(getCarecter):
    f = open("passwordList.txt", "a")
    f.write(''.join(x)+".")
    count = count + 1
    print(str(count) + " Possible Combination=> "+ ''.join(x))

f.close()
