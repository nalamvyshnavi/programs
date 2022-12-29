#panda two types series,data frames
#series
import pandas as pd
import numpy as np
a=[1,2,3]
series=pd.Series(a)
print(series)
dict={'names':["vysh","sravs"],'roll':[8,9]}
data=pd.DataFrame(dict)
print(data)
series=pd.Series(a,index=[10,20,30])
print(series)
#comma seperated files
df=pd.read_csv('text.txt')
print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())
s=pd.Series([1,3,5,6,8])
print(s)
print(s[0])
df2=pd.DataFrame({"A":1.0,
                  "B":pd.Timestamp("20130102"),
                  "c":pd.Series(1,index=list(range(4)),dtype="float32"),
                  "D":np.array([3]*4,dtype="int32"),
                  "E":pd.Categorical(["test","train","test","train"]),
                  "F":"fool",
                  }
                 )
print(df2)
print(df2.dtypes)
print(df2.tail(2))
print(df2.head(2))
print(df2.index)
print(df2.columns)
print(df2.describe)


#test