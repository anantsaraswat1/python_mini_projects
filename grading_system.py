name=input('enter your name: ')
section=input('enter your section: ')
chem=int(input('enter your Chemistry marks out of 100: '))
phy=int(input('enter your Physics marks out of 100: '))
math=int(input('enter your Maths marks out of 100: '))
py=int(input('enter your Python marks out of 100: '))
eng=int(input('enter your English marks out of 100: '))
sum=chem+phy+math+py+eng
per=(sum/5)
if per<40:
    print(name.capitalize(),'! you are fail\nBetter luck next time')
elif 40<=per<=50:
    print('grade: D\nPercentage:',per)
elif 50<=per<=60:
    print('grade: C\nPercentage:',per)
elif 60<=per<=70:
    print('grade: B\nPercentage:',per)
elif 70<=per<=80:
    print('grade: A\nPercentage:',per)
elif 80<=per<=90:
    print('grade: A+\nPercentage:',per)
elif 90<=per<=100:
    print('grade: O\nPercentage:',per) 
