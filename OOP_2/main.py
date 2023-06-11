import functions as f
import random

#1

for num in f.primeNumbers(1,100):
    print(num, end=" ")

print()

for num in f.primes(1,100):
    print(num, end= " ")


#2
rng=f.randomNumber()
squares=[(0,0.1*(i+1)) for i in range(10)]
hits_1=[0]*10
for _ in range(10**5):
    x=next(rng)
    y=next(rng)
    for i in range(len(squares)):
        if squares[i][0] <= x <= squares[i][1] and squares[i][0] <= y <= squares[i][1]:
            hits_1[i]+=1
print()
for i in range(10):
    print(f'Bok kwadratu:{0.1*(i+1):.1f} Liczba trafien:{(hits_1[i]/10**3):.2f}%')

hits_2=[0]*10
for _ in range(10**5):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    for i in range(len(squares)):
        if squares[i][0] <= x <= squares[i][1] and squares[i][0] <= y <= squares[i][1]:
            hits_2[i]+=1
print()
for i in range(10):
    print(f'Bok kwadratu:{0.1*(i+1):.2f} Liczba trafien:{(hits_2[i]/10**3):.2f}%')

#3

calka_1=f.Simpson_method(lambda x : x**2, 0,1)
print(calka_1.calculate())
calka_2=f.Monte_Carlo_method(lambda x : x**2,0,2)
print(calka_2.calculate())