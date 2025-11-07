a=input("enter :")
count1=[]
for i in range(0,len(a),1):
    b=i
    c=i+1
    if a[b:c]==a[b+1:c+1]:
        print(a[b]+a[c])
        count1.append(a[b])
    elif count1==[]:
        print("not repeated")
        break
print(count1)
