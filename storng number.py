n=int(input("enter the number"))
t=n
s=0
while(n>0):
    d=n%10 
    i=1
    f=1
    while(i<=d):
        f=f*i
        i=i+1
    s=s+f
    n=n//10
if(s==t):
    print("the is number ids storng number")
else:
    print("the is number is not a strng number")
    
