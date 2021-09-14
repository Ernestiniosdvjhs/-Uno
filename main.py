import random
import math

b,arr=[],[]
for i in range(50):
    b.append(round(random.uniform(-100, 100)))
b.sort(reverse=True)
for i in b:
    if i>=0:
        arr.append(i)

for i in range(len(arr)-2):
    a,b,c=arr[i],arr[i+1],arr[i+2]
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        print(p)
        print( math.sqrt( (p*(p-a)*(p-b)*(p-c)) ) )
        break