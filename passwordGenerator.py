import itertools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p',action='store',dest='possibleCombo',help="Possible combination",type=str,default=3)
parser.add_argument('-c',action='store',dest='combinationType',help="Combination type",type=str)




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
    f.write(''.join(x)+"\n")
    count = count + 1
    print(str(count) + " Possible Combination=> "+ ''.join(x))

f.close()
