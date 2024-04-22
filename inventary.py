import pandas as pd
l={'Banana':50,'Apple':200,'Kiwi':300,'Papaya':150,'Orange':250,'Imli':400,'Guava':100,'maggi':14,'milk':20,'dahi':40}
print(pd.Series(l))
print('\n')
a={}
c=n=0
print('\n')
for i in l:
    print(i,l[i])
    k=int(input('enter weight in kg: '))
    a[i]=[l[i],k]
    c+=k
    n+=k*l[i]
print('\n\n',pd.DataFrame(a,index=['price','Qty']))
print('\ntotal weight= ',c)
print('total price= ',n)