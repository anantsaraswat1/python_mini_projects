import random as rd
a={'rock':'scisor','paper':'rock','scisor':'paper'}
while True:
    comp=rd.choice(list(a.keys()))
    print('''
    1. Rock
    2. Paper
    3. Scisor
    4. Exit''')
    user=int(input('enter choice from above:  '))
    if user==1:
        ch='rock'
    elif user==2:
        ch='paper'
    elif user==3:
        ch='scisor'
    elif user==4:
        print('Exiting....')
        break
    else:
        print('please choose a correct no.')
    if a[comp]==ch:
        print('won')
    else:
        print('lose')
        print('computer choose',comp)