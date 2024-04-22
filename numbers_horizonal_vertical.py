star=int(input("Enetr the starting number: "))
end=int(input("Enter the ending value: "))
upd=int(input("Enter the updataion/gaping value you want: "))
choice=int(input('''
    1. forward/Horizontal
    2. reverse
    3. vertical in reverse order
    4. vertical\n'''))
print('\n')
if choice==1:
    for i in range(star,end+1,upd):
        print(i,end=' ')
elif choice==2:
    for i in range(end,star-1,-upd):
        print(i,end=' ')
elif choice==3:
    for i in range(end,star-1,-upd):
        print(i)
elif choice==4:
    for i in range(star,end+1,upd):
        print(i)