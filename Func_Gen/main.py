import random
import matplotlib.pyplot as plt
from functions import (
    print_pascal_triangle,
    distance,
    fibonacci_generator,
    even_generator,
    odd_generator,
    return_limit,
    frange,
    random_fade_generator,
    P_n
)
print("Zadanie 1")
print_pascal_triangle(8)

print("Zadanie 2")
N=1000
sequence = [random.randint(0,1) for _ in range(N)]
print(sum(distance(sequence))/sum(sequence))

print("Zadanie 3")
sequence = [random.randint(0,20) for _ in range(10)]
print(sequence)
print(sum(even_generator(return_limit(fibonacci_generator(),100))))
print(sum(odd_generator(return_limit(fibonacci_generator(),100))))

print("Zadanie 4")

print("Range(7)")
for value in frange(7):
    print(value)
print("Range(-7)")
for value in frange(-7):
    print(value)
print("Range(2,7)")
for value in frange(2,7):
    print(value)
print("Range(7,2)")
for value in frange(7,2):
    print(value)
print("Range(2,7,2)")
for value in frange(2,7,2):
    print(value)
print("Range(2,7,-2)")
for value in frange(2,7,-2):
    print(value)   
print("Range(7,2,2)")
for value in frange(7,2,2):
    print(value) 
print("Range(7,2,-2)")
for value in frange(7,2,-2):
    print(value)  

print("Zadanie 5")
g=random_fade_generator()
s=dict.fromkeys(range(-20,21),0)

for _ in range(10**6):
    s[next(g)]+=1
print(s)

su=sum(s.values())
plt.plot(s.keys(),[v/su for v in s.values()],'o')


plt.plot(s.keys(),[P_n(d,N) for d in s.keys()],'*')
plt.show()