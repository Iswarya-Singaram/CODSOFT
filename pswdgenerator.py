import string
import secrets

set1=string.ascii_lowercase
set2=string.ascii_uppercase
set3="!#@$%^&*()[]{}:;><,?|+=-_~"
set4=string.digits

upper,lower,numbers,symbols=True,True,True,True
all=""
if upper:
    all+=set2
if lower:
    all+=set1
if numbers:
    all+=set4
if symbols:
    all+=set3

l=int(input("enter the length of the password:"))
no_of_passwords=1

for i in range(no_of_passwords):
    password="".join(secrets.choice(all) for i in range(l))
    print(password)


