a=int(input("Enter the First integer:"))
b=int(input("Enter the Second integer:"))
print("\tChoose An Operation")
print('''1.Addition
2.Subtraction
3.Division
4.Multiplication
5.Exponent''')
choice=int(input("Enter Your Choice:"))
if choice==1:
    c=a+b
elif choice==2:
    c=a-b
elif choice==3:
    c=a/b
elif choice==4:
    c=a*b
elif choice==5:
    c=a**b
else:
    print("Invalid Entry")
print("The result is:",c)

        

