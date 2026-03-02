name1="Dhyanghfvdsgbdo"
len1 =len(name1)//2
for i in range(0,len1+1,1):
    print(" "*(len1-i)+name1[0:2*i+1])
for i in range(1,len1+1,1):
    print(" "*i+name1[0:2*(len1-i)+1])

