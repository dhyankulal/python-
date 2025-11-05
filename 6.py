a=input("enter the name: ")
count1,count2,count3,count4,count5=0,0,0,0,0
for i in range(0,len(a)+1,1):
    if a[i:i+1].lower()=="a":
        count1+=1
    elif a[i:i+1].lower()=="e":
        count2+=1
    elif a[i:i+1].lower()=="i":
        count3+=1
    elif a[i:i+1].lower()=="o":
        count4+=1
    elif a[i:i+1].lower()=="u":
        count5+=1
    else:
        c=''
print(c)
print("a=",count1)
print("e=",count2)
print("i=",count3)
print("o=",count4)
print("u=",count5)
