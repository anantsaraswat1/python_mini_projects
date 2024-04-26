import pandas as pd

def search(a,l):
    for i in l:
        if i==a:
            return f'{a} is available in our inventary with price={l[i]}'
    return f'Sorry! {a} is not Present'

print('----------Welcome to Inventry system-----------\n')
l={'Banana':[50,3],'Apple':[200,4],'Kiwi':[300,2],'Papaya':[150,4],'Orange':[250,5],'Imli':[400,4],'Guava':[100,1],'Pineapple':[100,8],'Milk':[20,2],'Dahi':[40,5]}

while(True):
    print('''
        1. View Items With Prices
        2. Search for an specific item
        3. Book Items
        4. Generate Reciept\n''')

    choice=int(input('Enetr Your choice from above menu: '))

    if choice==1:
        print(pd.DataFrame(l,index=['Price','Available']).T)
        
    elif choice==2:
        i=input('enter item name: ').capitalize()
        print(search(i,l))

    elif choice==3:
        a={}
        c=n=0
        for i in l:
            print('\n',i,l[i][0])
            k=int(input('enter weight in kg: '))
            if k<=l[i][1]: 
                a[i]=[l[i][0],k]
                c+=k
                n+=k*l[i][0]
            else:
                print(f'Sorry! {i} are present only {l[i][1]}Kg')
            
    elif choice==4:
        try:
            reciept=pd.DataFrame(a,index=['price','Qty']).T
            reciept['Total']=reciept['price']*reciept['Qty']
            print('\n\n',reciept)
            print(f'\ntotal weight= {c}kg')
            print(f'total Price= {n}')
            break
        except:
            print('\nSorry your Cart is empty\nTo generate Reciept Firstly add some items to your cart')
    else:
        print('invalid choice!!!')
