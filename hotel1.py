import pandas as pd
from datetime import datetime as dt

def hotel_menu(file):
    
    df1 = pd.read_excel(file, usecols=[1, 2, 3], nrows=7) 
    col1 = df1.iloc[1:7,0].tolist()
    col2 = df1.iloc[1:7,1].tolist()
    col3 = df1.iloc[1:7,2].tolist()
    
    return col1,col2,col3

a1,a2,a3 = hotel_menu("hotel menu.xlsx")
b=0
for i in range(0,len(a3),1):
    if a3[i]>0:
        a=int(a2[i]*a3[i])
        b=b+a2[i]*a3[i]
        
        print(f"{a1[i]}\t₹{a}\t{dt.now().strftime("%Y-%m-%d")}")
print("total:₹",b)