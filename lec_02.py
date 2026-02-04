#Библиотека  Numpy. Слияние и разбиение массивов

import numpy as np
import timeit                                                                 

#Одномерные

x=np.array([1,2,3])
y=np.array([4,5])
z=np.array([6])

xyz=np.concatenate([x,y,z])
print(xyz)

#Двумерные массивы
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])
xy1=np.concatenate([x,y]) #vstack
print(xy1)

xy2=np.concatenate([x,y],axis=0) #столбцы измерение, вниз
print(xy2)

xy3=np.concatenate([x,y],axis=1) #строки измерение, направо

print(np.vstack([x,y]))
print(np.hstack([x,y]))
print(np.dstack([x,y]))

#Разбиение массивов


xy=np.vstack([x,y])
print(xy)

print(np.split(xy,[1],axis=1))#разъединение по столбикам
print(np.hsplit(xy,[2]))#разъединение по столбикам

#Универсальные функции
x=np.arange(1,10)
print(x)

def f(x):
    out=np.empty(len(x))
    for i in range(len(x)):
        out(i)=1.0/x[i]
    return out

print(f[x])
print(1.0/x)#универсальная функция, в 10 раз быстрее прошлой

print(timeit.timeit(stnt="f(x)", globals=globals()))
#виды уф. Арифмитические операции
x=np.arange(5)
print(x)

print(x+1)#add
print(x-1)#substract
print(x*2)
print(x/2)
print(x//2)
print(-x)
print(x**2)#power
print(x%2)
print(np.add(x,1))

x=np.arange(-5,5)
print(x)

print(abs(x))
print(np.abs(x))
print(np.absolute(x))

x=np.array([3+4],[4-3])
print(np.abs(x))
#виды уф. тригонометрические sin cos arctg arcctg

#виды уф. показательные exp, log10, log2, power,log
x=[0, 0.0001, 0.001, 0.01]
print("exp = ", np.exp(x))
print("exp-1 = ", np.expm1(x))
print("log(x)= ", np.log(x))
print("log(x+1)= ", np.log1p(x))
#виды уф. гиперболич
x=np.arange(5)
print(x)
y=10*x
print(y)
y=np.multiply(x,10)
print(y)

z=np.empty(len(x))
np.multiply(x,10,out=z)
print(z)

x=np.arange(5)
z=np.zeros(10)
print(x)
print(z)
z[::2]= x*10
#0 0 10 0 20 0 30 0 40 0
print(z)

z=np.zeros(10)
np.mulriply(x,10,z[::2])
print(z)

#Cводные показатели

x=np.arange(1,5)
print(x)
print(np.add.reduce(x))
print(np.add.accumulate(x))

print(np.multiply.reduce(x))
print(np.multiply.accumulate(x))

print(np.substract.reduce(x))
print(np.substract.accumulate(x))

print(np.prod(x))
print(np.cumprod(x))

x=np.arrange(1,10)
print(np.add(x,x))
print(np.add.outer(x,x))

print(np.multiply.outer(x,x))

#агрегирование

np.rendom.seed(1)
s=np.random.random(100)
print(sum(s))
print(np.sum(s))#для действительных и больших множеств

a=np.array([1,2,3,4,5],[6,7,8,9,10])
print(sum(a))#по столбцам
print(np.sum(s))#все элементы
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

peint(typr(a))
print(a.sum())
print(a.sum(0))
print(a.sum(1))

print(sum(a,2))

#Min/max
np.random.seed(1)
s=np.random.random(100)

print(min(s))
print(np.min(s))

print(max(s))
print(np.max(s))

#mean, std, var, median, argmin, argmax, percentile, any, all
#nan*

#not a number - NaN

#broadcasting

a=np.array([1,2,3])
b=np.array([5,5,5])
print(a+b)
#[6,7,8]
print(a+5)
#
