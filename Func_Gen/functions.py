import random
import math
# Proszę napisać generator zwracający kolejne wiersze 
# trójkąta Pascala wraz z sumą ich wartości

def pascal_triangle(n):
    row=[1]
    yield sum(row),row

    for _ in range(n-1):
        row = [1] +[row[i]+row[i+1] for i in range(len(row)-1)] + [1]
        yield sum(row),row

def print_pascal_triangle(n):
    for sum_row, row in pascal_triangle(n):
        print(sum_row,"".join(str(x).center(5) for x in row).center(n*15))


# Proszę wygenerować losowy ciąg zer i jedynek o długości N. Proszę napisać generator 
# zwracający liczbę zer oddzielających kolejne jedynki w sekwencji przekazanej jako 
# parametr. Korzystając z utworzonego generatora proszę obliczyć średnią odległość między kolejnymi 
# jedynkami w wygenerowanym wcześniej ciągu

def distance(seq):
    count=0
    for val in seq:
        if val ==1:
            yield count 
            count = 0
        else:
            count+=1

# Proszę napisać trzy funkcje generatorowe:
# zwracającą kolejne elementy ciągu Fibonacciego (nieskończony),
# zwracającą te wartości z przekazanej jako parametr sekwencji, które są parzyste/nieparzyste
# zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji
# Korzystając ze zdefiniowanych funkcji proszę obliczyć sumę parzystych/nieparzystych elementów ciągu Fibonacciego mniejszych od 100

def fibonacci_generator():
    value,next_value=0,1
    while True:
        yield value
        value, next_value=next_value,value+next_value

def even_generator(seq):
    for i in seq:
        if i % 2 == 0:
            yield i

def odd_generator(seq):
    for i in seq:
        if i % 2 == 1:
            yield i

def return_limit(seq,limit):
    for i in seq:
        if i > limit:
            break
        yield i

# Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych
# Do testów: range(7), range(-7), range(2,7), range(7,2), range(2,7,2), range(2,7,-2), range(7,2,2), range(7,2,-2)

def frange(start,stop=None,step=1):
    if stop == None:
        stop=start
        start=0
    
    if step > 0:
        while start < stop:
            yield float(start)
            start+=step
    else:
        while start > stop:
            yield float(start)
            start+=step

# Proszę utworzyć generator zwracający odległość od punktu początkowego po N krokach dN=n1−n2=2n1−N
#  (n1 - liczba kroków wykonanych w prawo, n2 liczba kroków wykonanych w lewo), dla błądzenia losowego w jednym wymiarze: wykonujemy N kroków o równej długości wzdłuż prostej, przyjmując jednakowe prawdopodobieństwo p wykonania kroku w prawo lub w lewo.
# Proszę sporządzić histogram odległości uzyskanej po N=20 krokach dla 10^6 powtórzeń i porównać z wartością oczekiwaną

def random_fade_generator():
    while True:
        N=20
        right=0
        left=0
        for _ in range(20):
            move=random.choice((-1,1))
            if move == -1:
                left+=1
            else:
                right+=1

        yield right-left

def P_n(d,N):
    return (math.factorial(N)/(math.factorial((d+N)//2)*math.factorial((N-d)//2)))/(2**N)
