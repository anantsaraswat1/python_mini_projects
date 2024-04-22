nme=input("Please enter your name: ")
age=int(input("Please enetr your age: "))
if age>=18:
    print("You are eligible for voting......")
    print("WHich party you want to be win the elections: ")
    print(" 1. BJP \n","2. CONGRESS \n","3. BSP \n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Thanks for giving your preciuos vote to BJP")
    elif choice==2:
        print("Thanks for giving your preciuos vote to CONGRESS")
    elif choice==3:
        print('Thanks for giving your preciuos vote to BSP')
    else:
        print("Invalid choice made")  
    
else:
    print("Not Eligible") 
    print('Your DOB must be before 2005')   
   