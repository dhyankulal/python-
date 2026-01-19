def diamond2(name1):
    spaces="-"
    len1=len(name1)
    for i in range(1,len1+1,1):
        print(spaces*(len1-i)+name1[0:i])
    for i in range(1,len1,1):
        print(spaces*i+name1[0:len1-i])

diamond2("FunwithProgramming")
