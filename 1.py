a="TheCollegeBusDing"
for i in range(1,len(a)+1,1):
    print(" "*(len(a)-i),a[0:i]+a[0:i])
for j in range(1,len(a)+1,1):
    print(" "*(j-1),a[0:len(a)+1-j]+a[0:len(a)+1-j])