name1="Funwithprogramming"
spaces="-"
len1=len(name1)
len2=len1//2
for i in range(0,len2+1,1):
    print(spaces*(len2-i)+name1[0:i*2+1])

