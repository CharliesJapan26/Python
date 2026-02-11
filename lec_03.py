import numpy as np

#правила транслирования (broadcasting)

a= np.ones((2,3))
b= np.arange(3)

print(a)
print(b)

print(a.shape)
print(b.shape)

c=a+b
print(c)
print(c.shape)

#1. a=(2,3) -> 2, b=(3,)->1 =>a=(2,3),b=(1,3)
#2. a=(2,3), b=(1,3)=>b=(2,3)
#3. a=(2,3) b=(2,3)
#1 1 1
#1 1 1

#0 1 2
#0 1 2

#[[1. 2. 3.]
# [1. 2. 3.]]

a=np.arange(3).reshape((3,1))
b=np.arange(3)
print(a)
print(b)
print(a.shape)
print(b.shape)

#a-
#[0]
#[1]
#[2]

#b-
#[0 1 2]

#a-(3,1)
#b-(3) -1 b-(1,3)
#после 1 шага
a - (3,1)
b - (1,3)

#a-
#[0]
#[1]
#[2]

#b-
#[0 1 2]
#[0 1 2]
#[0 1 2]

##после 2
#a-(3,3)
#b-(3,3)
print(a+b)
print(a*b)

a=np.ones(3,2)
b=np.arange(3)
print(a)
print(b)
print(a.shape)
print(b.shape)

[1, 1]
[1, 1]
[1, 1]

[0 1 2]

a-(3,2)
b-(1,3) - (3,3)

#центрирование массивов
a=np.array(
    [
        [1,2,3,4,5,6,7,8,9]
        [9,8,7,6,5,4,3,2,1]
        ]
    )
print(a)

aMean=a.mean(0)
print(aMean)

print(a.shape)
print(aMean.shape)

aCentr=a-aMean
print(aCentr)

print(aCentr.mean(0))

a=np.array(
    [
        [1,2,3,4,5,6,7,8,9]
        [9,8,7,6,5,4,3,2,1]
        ]
    )
print(a)

aMean=a.mean(1)
print(aMean)

print(a.shape)
print(aMean.shape)

aMean=aMean[:]
print(aMean)

aMean=aMean[:]
print(aMean)
print(aMean.shape)

aMean=aMean[:,np.newaxis]
print(aMean)
print(aMean.shape)

aCentr=a-aMean
print(aCentr)
print(aCentr.mean(1))

#графики
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.linspace(0,10,100)
y=y[:,np.newaxis]

print(x.shape)
print(y.shape)

z=np.sin(x)*y

plt.imshow(z)
plt.colorbar()
plt.show()

#маскирование
x=np.arange(1,6)
print(x<3)
#[True True False False False]
print(np.less(x,3))

rng=np.random.default_rng(seed=1)
x=rng.integers(10,size=(3,4))

print(x)
print(x<6)
