dlist=[]
dlist = input("Enter the 6 numbers").split()
dhlist = [int(dh)for dh in dlist]
dhlist.sort(reverse=True)
print(dhlist)
print("mark scored from highest to lowest")
for x in dhlist:
    print(x)