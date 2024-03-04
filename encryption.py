import string
import random
ran=''.join(random.choices(string.ascii_letters, k=3))
ran2=''.join(random.choices(string.ascii_letters, k=3))
print("To generate encrypted code press(1), for decoding press(2)")
n=int(input("enter you choise = "))
if(n==1):
    m=input("Enter your code here = ")
    if(len(m[0:])<=3):
        r=m[::-1]
        print(r)
    else:
        p=slice(3)
        q=m[3:]
        j=q+m[p]
        cd=ran+j+ran2
        print(cd)
elif(n==2):
   x= input("Enter the encrypted code here = ")
   if(len(x)<=3):
       y=x[::-1]
       print(y)
   else:
        s1=x[3:]
        s2=s1[:-3]
        s3=s2[-3:]
        s4=s2[:-3]
        s5=s3+s4
        print(s5)
       
