import random as rd
number=rd.randint(1,9)
n=int(input('Enter a no. between 1 to 10:  '))
if n==number:
    print('correct')
else:
    print('Wrong')
    print('correct no. is',number)