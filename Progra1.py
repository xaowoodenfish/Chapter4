#Oct 26.2015
# guess game
import random
key = []
bb = []
KeyWord = 'abcdef'
n = 1
while n <5:
    index = random.randint(0,5)
    if index not in bb:
        bb.append(index)
        b = KeyWord[index]
        key.append(b)
        n +=1
print('= '*12+'STRAT THE GAME'+'= '*12)
i = 1
while i<13:
    while True:
        num = input("This is the %s member to guess,"%i+"the guess string is:")
        if len(num) ==4:
            break
    num = list(num)
    back = []
    for j in range(len(key)):
        if num[j] == key[j]:
            num.append('Black')
        elif (num[j] !=key[j]) & (num[j] in key):
            num.append('White')
        else:
            num.append(' ')
    print('The %i time guess result is:%s'%(i,num[4:]))
    num1 = num[4:]
    code = ['Black','Black','Black','Black']
    if num1 == code:
        print('you are the %i one guess the key!'%i)
        break
    i +=1
if i >12:
    print("Times limited 12!!!!")