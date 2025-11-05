a=int(input("enter any number:"))
for i in range(2,a+1,1):
    b=a/i
    c=a//i
    if b==c:
        print("it is not a prime number")
        break
    else:
        print("its a prime number")
        break
