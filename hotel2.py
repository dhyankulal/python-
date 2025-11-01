import pandas as pd
from datetime import datetime as dt

def hotel_menu(file):
    
    df1 = pd.read_excel(file, usecols=[1, 2, 3], nrows=7) 
    col1 = df1.iloc[1:7,0].tolist()
    col2 = df1.iloc[1:7,1].tolist()
    col3 = df1.iloc[1:7,2].tolist()
    
    b=0
    for i in range(0,len(col3),1):
        if col3[i]>0:
            a=int(col2[i]*col3[i])
            b=b+col2[i]*col3[i]
            
            c=print(f"{col1[i]}\t₹{a}\t{dt.now().strftime("%Y-%m-%d")}")
    d=print("total:₹",b)
    
    return c,d

hotel_menu("hotel menu.xlsx")
