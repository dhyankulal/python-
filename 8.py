a="funwithprogramming"
b=len(a)//2
for i in range(0,b,1):
    print(" "*(b-i),a[0:2*i+1])
for i in range(b,0,-1):
    print(" "*(b-i),a[0:2*i-1])
    

