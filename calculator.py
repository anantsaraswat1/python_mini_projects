a=int(input("Enter yor first no.: "))
choice=input("\n* : Multiplication\n+ : Addition\n- : Subtraction\n/ : Division\n% : Remender\npow : Power\n\n")
b=int(input("Enter yor second no.: "))
if(choice=='*'):
    print(f"{a}*{b} = {a*b}")
elif(choice=='+'):
    print(f"{a}+{b} = {a+b}")
elif(choice=='-'):
    print(f"{a}-{b} = {a-b}")
elif(choice=='/'):
    print(f"{a}/{b} = {a/b}")
elif(choice=='%'):
    print(f"{a}%{b} = {a%b}")
elif(choice=='pow'):
    print(f"{a}^{b} = {a**b}")
else:
    print("Invalid Choice!")