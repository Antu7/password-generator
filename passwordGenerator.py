import itertools

possibleCombo = input("How Many Password Combination You Want to Create? Exp(3): ")

combinationType = input("1) Combination Alphanumeric \n"
"2) Combination Numeric only \n"
"3) Combination Carecter only \n"
"4) Combination special Carecter only \n"
"5) Combination special Carecter & number only \n"
"6) Combination Alphanumeric Special Characters \n"
"==>  "
)

special = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
numeric = '0123456789'
carecter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if combinationType == '1':
    getCarecter = numeric + carecter
elif combinationType == '2':
    getCarecter = numeric
elif combinationType == '3':
    getCarecter = carecter
elif combinationType == '4':
    getCarecter = special
elif combinationType == '5':
    getCarecter = special + numeric
elif combinationType == '6':
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