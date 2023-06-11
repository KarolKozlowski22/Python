import math 
import random
import abc 
import scipy.integrate as integrate

# Proszę napisać iterator zwracający kolejne liczby pierwsze z zadanego zakresu dwoma 
# sposobami i porównać ich wykorzystanie 

class primeNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self 
    
    def is_prime(self, num):
        if num < 2:
            return False
        
        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                return False 
        return True
        
    def __next__(self):
        while self.start<=self.stop:
            if self.is_prime(self.start):
                prime=self.start
                self.start+=1
                return prime
            else:
                self.start+=1
        raise StopIteration()
    
def primes(start, stop):
    for num in range(start,stop+1):
        if num < 2: 
            continue 
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                break
        else:
            yield num

# Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru:Xn+1 = (aXn + c) mod m, dla m = 231-1, a = 75, c = 0, x0 = 1.
# Korzystając z zaimplementowanego iteratora proszę wylosować 105 par liczb z przedziału [0,1). Proszę sprawdzić jaki procent wylosowanych par mieści się w
# kwadracie o boku 0.1*n, gdzie n∈[1,10]. Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python

class randomNumber:
    def __init__(self):
        self.m=2**31-1
        self.a=7**5
        self.c=0
        self.x=1
    def __iter__(self):
        return self
    def __next__(self):
        self.x=(self.a*self.x + self.c)%self.m
        return self.x/self.m
    

# Proszę napisać abstrakcyjną klasę Calka z metodą inicjalizacyjną określającą funkcję podcałkową (przy wywołaniu proszę użyć wyrażenia lambda) oraz granice całkowania i 
# metodą abstrakcyjną obliczającą wartość całki.
# Następnie proszę utworzyć klasy dziedziczące po klasie Calka z metodami obliczającymi wartość całki odpowiednio metodą:
# Simpsona
# Monte Carlo

class Calka(abc.ABC):
    def __init__(self, f, start, stop):
        self.f=f
        self.start=start
        self.stop=stop
        self.n=10**3

    @abc.abstractmethod
    def calculate(self):
        pass

class Simpson_method(Calka):
    def calculate(self):
        h=(self.stop-self.start)/2/self.n
        sum=self.f(self.start)
        step=self.stop/2/self.n
        for i in range(2*self.n):
            if i % 2 == 0:
                sum+=2*self.f(self.start+i*step)
            else:
                sum+=4*self.f(self.start+i*step)
        sum*=h/3
        return sum

class Monte_Carlo_method(Calka):
    def calculate(self):
        rng=randomNumber()
        t=0
        a=2
        b=4
        value = integrate.quad(self.f,self.start,self.stop)
        it=0
        while True:
            it+=1
            x=next(rng)*a
            y=next(rng)*b
            if 0 < y and y <= self.f(x):
                t+=1
            elif y < 0 and y >= self.f(x):
                t-=1
            if abs(a*b*t/it - value[0]) < 1e-5:
                break
        
        return a*b*t/it

