import time
import matplotlib.pyplot as plt

def recur_fibo(n):
    if n <= 1:
        return n
    return (recur_fibo(n -1) + recur_fibo(n-2))

def iter_fibo(n):
    nMinus2 = 0
    nMinus1 = 0
    current = 1

    for i in range(n):
        nMinus2 = nMinus1
        nMinus1 = current
        current = nMinus1+nMinus2
    return current

def getFibonacciArray(n, size):
    """
    Uses 2 lists of length size and returns a list
    with size + 1 elements (due to the carry while adding)
    """
    arr1 = [0 for x in range(size)]
    arr2 = [0 for x in range(size)]
    returnArr = [0 for x in range(size+1)]

    if n == 0:
        return addArrays(arr1, arr1)
    if n == 1:
        return addArrays(arr1, arr2)

    arr2[size -1] = 1
    for i in range(n-1):
        returnArr = addArrays(arr1, arr2)
        print(returnArr)
        arr1 = arr2

        tmpArr = [0 for x in range(len(arr2))]
        for j in range(len(arr2)-1):
            arr2[j] = returnArr[j+1]
        arr2 = tmpArr
    return returnArr


    
    
def addArrays(arr1, arr2):
    size = len(arr1)
    result = [0 for x in range(size+1)]
    remainder = 0
    for i in reversed(range(size)):
        tmp = arr1[i] + arr2[i] + remainder
        print(tmp)
        result[i+1] = tmp % 10
        remainder = int(tmp /10)
    result[0] = remainder
    return result

n=1
x =[]
y= []
for i in range(n):
    x.append(i)
    s=time.time()
    recur_fibo(i)
    e=time.time()
    y.append(e-s)

plt.plot(x,y,'o')
plt.xlabel("N")
plt.ylabel("Time")
#plt.show()

a=[]
b=[]
n=1
for i in range(n):
    a.append(i)
    s=time.time()
    iter_fibo(i)
    e=time.time()
    b.append(e-s)

plt.plot(a,b,'x')
plt.xlabel("N")
plt.ylabel("Time")
plt.show()

print(getFibonacciArray(8,10))

def biggestFibWithNDigits(n):
    for i in range(10000):
        fib = str(iter_fibo(i))
        if len(fib) == n-1:
            return fib
        
print(biggestFibWithNDigits(100))
