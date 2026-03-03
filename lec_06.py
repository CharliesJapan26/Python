import numpy as np
import pandas as np

#Отсутствующие данные

a=np.nan
a=-9999

#Pandas: 1)NaN, None 2) pd.NA
a=None
print(type(a))

a=np.array([1,2,3])
b=np.array([1,None,3])
print(b.sum()) - не будет проходить

c=np.array([1,np.nan,3])
print(c)-все значения будут с плавающей точкой из-за нан, получатся действия но везде будет нан

print(np.nansum(c))-игнорирует нан

x=pd.Series([1,2,3,4,5],dtype=int)

print(x)
x[0]=none
x[1]=np.nan
print(x)

x=pd.Series(['1','2','3','4','5'],dtype=int)-будут как объекты
print(x)
x[0]=none
x[1]=np.nan
print(x)

x=pd.series([true, false, false, true])
print(x)
x[0]=none
x[1]=np.nan
print(x)

x=pd.series([1, np.nan, None, 5])-тип float64
x=pd.series([1, np.nan, None, 5, pd.NA])-тип object
x=pd.series([1, np.nan, None, 5, pd.NA], dtype="int32")- пандавские объекты считаются как <NA>

x=pd.series([1, np.nan, None, 5, "hello"])
print(x.isnull())-2 and 3 is true, else false
print(x.notnull())-1,4,5 is true
print(x[x.isnul()])-print all not null answers

x=pd.dataframe([1, np.nan, None, 5, pd.NA],[1,2,3],[2,np.nan,3])
print(x.dropna(axis=0))

print(x.dropna(axis=1))

print(x.dropna(axis=0,how='any'))-как отбрасывать строки или столбцы

x=pd.dataframe([None, np.nan, None],[1,2,3],[2,np.nan,3])
print(x)
#how=all-брать, если все знач отсут
#how=all-брать, если одно значение знач отсут
print(x.dropna(axis=0,tresh=2)) #must be min N not nan

x=pd.dataframe([None, np.nan, None, 1,2,3], dtype="Int32")
print(x)
print(x.fillna(4))
print(x.ffill())#to fill what was before
print(x.bfill())#to fill what was after

#Иерархическая индексация

index = [
("A1",2025)
("A1",2026)
("A2",2025)
("A2",2026)
("A3",2025)
("A3",2026)
    ]
data=[1,2,3,4,5,6]

s=pd.Series(data,index=index)
print(s)

print(S[[0,2,4]])

#print(s[[i for i in s.index if i[1]==2026]])
mi=pd.MultiIndex.from_tuples(index)
print(mi)

s=s.reindex(mi)
print(s)

s1=pd.Series(data, index=mi)
print(s1)


print(s["A1",2025])

df=s.unstack()
print(df)

print(df.stack())

#одномерный сериес может хранить данные с большим числом измерений
index = [
("A1",2025,1)
("A1",2026,1)
("A2",2025,2)
("A2",2026,2)
("A3",2025,1)
("A3",2026,1)
    ]
data=[1,2,3,4,5,6]

s=pd.Series(data, index=mi)
print(s)

mi=pd.MultiIndex.from_tuples(index)
s=s.reindex(mi)
print(s)

print(s[:,2025,1])

df=s.unstack()
print(df)

df1=pd.DataFrame(
{"jan":s[:,:,1]
 "feb":s[:,:,2]
 "mar":s[:,:,1]+s[:,:,2]}
    )
print(df1)
print(df1["mar"])
print(df1.loc[["A1","A2"],["feb", "jan"]])
print(df1.iloc[[1,1],[0,1]])


rng=np.random.default_rng(1)

df=pd.DataFrame(
    rng.random((4,2)),
index=["A1","A1","A2","A2"], [2025,2026,2025,2026]
columns=["jan","feb"]
    )

print(df)

index = [
("A1",2025,1): 1,
("A1",2026,1): 2,
("A2",2025,2): 3,
("A2",2026,2): 4,
("A3",2025,1): 5,
("A3",2026,1): 6,
    ]

s=pd.Series(data)
print(s)

index = [
("A1",2025,1): 1,
("A1",2026,1): 2,
("A2",2025,2): 3,
("A2",2026,2): 4,
("A3",2025,1): 5,
("A3",2026,1): 6,
    ]

mi=pd.MultiIndex.from_arrays(index)([["A1","A2","A1","A2"],[2025,2026,2025,2026]])
print(index)

mi=pd.MultiIndex.from_product(index)([["A1","A2"],[2025,2026]])
print(index)

mi=pd.MultiIndex(
levels=[["A1","A2"],[2025,2026]]
code=[[0,0,1],[0,1,0]]
    )
print(index)

df=pd.DataFrame(
    rng.random((4,2)),
index=["A1","A1","A2","A2"], [2025,2026,2025,2026]
columns=["jan","feb"]
    )

df.index.name=["property","year"]

print(df)

mi=pd.MultiIndex.from_product(index)([["B1","B2","B3"],["jan","feb"]],names=["shop","year"])
print(index)

data=rng.random((4,6))

print(data)

df=pd.DataFrame(data,index=mi1,columns=mi2)
print(df)
