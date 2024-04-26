import pandas as pd

def search(a,l):
    for i in l:
        if i==a:
            return f'{a} is available in our inventary with price={l[i]}'
    return f'Sorry! {a} is not Present'

print('----------Welcome to Inventry system-----------\n')
l={'Banana':50,'Apple':200,'Kiwi':300,'Papaya':150,'Orange':250,'Imli':400,'Guava':100,'Pineapple':100,'Milk':20,'Dahi':40}

while(True):
    print('''
        1. View Items With Prices
        2. Search for an specific item
        3. Book Items
        4. Generate Reciept\n''')

    choice=int(input('Enetr Your choice from above menu: '))

    if choice==1:
        print(pd.Series(l))
        
    elif choice==2:
        i=input('enter item name: ').capitalize()
        print(search(i,l))

    elif choice==3:
        a={}
        c=n=0
        for i in l:
            print('\n',i,l[i])
            k=int(input('enter weight in kg: '))
            a[i]=[l[i],k]
            c+=k
            n+=k*l[i]
            
    elif choice==4:
        reciept=pd.DataFrame(a,index=['price','Qty']).T
        reciept['Total']=reciept['price']*reciept['Qty']
        print('\n\n',reciept)
        print(f'\ntotal weight= {c}kg')
        print(f'total Price= {n}')
        break
        
    else:
        print('invalid choice!!!')
