
def check_range(func):
    def wrapper(self, other):
        if abs(func(self,other).x) > 100 or abs(func(self, other).y) > 100:
            raise ValueError("Variable out of range")
        return func(self,other)
    return wrapper



# Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie. Obie współrzędne proszę zdefiniować 
# jako własności (metoda inicjalizacyjna bezparametrowa)
# Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć 
# je dekoratorem (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie, jeżeli nie - proszę zgłosić wyjątek

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f'(X:{self.x},Y:{self.y})'
    
    @property
    def x(self):
        return self._x 
    @x.setter
    def x(self, value):
        self._x=value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        self._y=value

    @check_range
    def add(self, other):
        result=Point()
        result.x=self.x+other.x
        result.y=self.y+other.y
        return result
    
    @check_range
    def sub(self, other):
        result=Point()
        result.x=self.x-other.x
        result.y=self.y-other.y
        return result

# Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta 
# (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), zdefiniowanych poprzez współrzędne wierzchołków    

class Area_Circuit:

    @staticmethod
    def calculate_circuit(*args):
        side_list=[((args[i].x-args[i-1].x)**2+(args[i].y-args[i-1].y)**2)**0.5 for i in range(len(args))]
        return sum(side_list), side_list
     
    @staticmethod
    def calculate_area(*args):
        circuit, side_list=Area_Circuit.calculate_circuit(*args)
        area=1
        for i in range(len(side_list)):
            area*=(circuit/2-side_list[i])**0.5
        if len(args)==3:
            area*=(circuit/2)**0.5
        return area
    

# Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby wywołań poszczególnych 
# funkcji obłożonych dekoratorem, z metodą statyczną zwracającą wynik

class FunctionCounter:
    count={}
    def __init__(self,func):
        self.func=func
        FunctionCounter.count[self.func.__name__]=0
        
    def __call__(self, *args):
        FunctionCounter.count[self.func.__name__]+=1
        return self.func(*args)

    @staticmethod
    def get_count():
        return FunctionCounter.count

@FunctionCounter
def fun():
    pass

@FunctionCounter
def fun1():
    pass

@FunctionCounter
def fun2(a):
    pass

@FunctionCounter
def fun3(a,b,c):
    pass