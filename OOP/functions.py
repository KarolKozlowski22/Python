import math
import random
import matplotlib.pyplot as plt

# Proszę utworzyć klasę IFS (Iterated Function System), a w niej:

# metodę inicjalizującą przyjmującą jako parametr współczynniki przekształcenia oraz prawdopodobieństwa i określającą początkowe współrzędne punktu jako (0,0),

# metodę dokonującą przekształcenia; jako parametr proszę przekazać liczbę iteracji. W każdej iteracji przy obliczaniu nowych współrzędnych punktu należy wylosować z określonym prawdopodobieństwem inną szóstkę z danego zestawu współczynników.
# Współrzędne obliczamy wg wzorów:
# x(t+1)=a*x(t)+b*y(t)+c
# y(t+1)=d*x(t)+e*y(t)+f

# metodę rysującą otrzymany wynik


class IFS:
    """
    init method assigning tuple of tuples and probability
    """
    def __init__(self,coefficients,probabilities):
        self.coefficients=coefficients
        if len(probabilities)!=len(coefficients):
            self.probabilities=[1/len(coefficients) for _ in range(len(coefficients))]
        else:
            self.probabilities=probabilities
        self.x=[0]
        self.y=[0]

    """
    transform method creating fractal with a given number of iterations
    """
    def transform(self,iterations):
        for _ in range(iterations):
            new_tuple=random.choices(self.coefficients,self.probabilities,k=1)[0]
            x_new=new_tuple[0]*self.x[-1]+new_tuple[1]*self.y[-1]+new_tuple[2]
            y_new=new_tuple[3]*self.x[-1]+new_tuple[4]*self.y[-1]+new_tuple[5]
            self.x.append(x_new)
            self.y.append(y_new)

    """
    function drawing fractals
    """
    def draw(self):
        plt.scatter(self.x,self.y)
        plt.show()




# Proszę utworzyć klasę Wektor 3D, którego stan początkowy jest określony przez metodę inicjalizacyjna. 
# W klasie proszę zdefiniować metody przeciążające operatory dodawania, odejmowania, mnożenia (mnożenie wektora przez liczbę) 
# oraz metodę str. Proszę napisać także metody zwracające odpowiednio długość wektora, iloczyn skalarny, wektorowy i mieszany


class wektor3D:
    """
    Using python function to initialize values 
    """
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    """
    add operator overloaded
    """
    def __add__(self,other):
        return wektor3D(self.x+other.x,self.y+other.y,self.z+other.z)
    """
    substract operator overloaded
    """
    def __sub__(self,other):
        return wektor3D(self.x-other.x,self.y-other.y,self.z-other.z)
    """
    multiply by scalar operator overloaded
    """
    def __mul__(self,scalar):
        return wektor3D(self.x*scalar,self.y*scalar,self.z*scalar)
    __rmul__=__mul__
    """
    enables to print 
    """
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
    """
    function calculating vector length
    """
    def vector_length(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    """
    function calculating dot product
    """
    def dot_product(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    """
    function calculating cross product
    """
    def cross_product(self, other):
        x=self.y*other.z-self.z*other.y
        y=self.z*other.x-self.x*other.z
        z=self.x*other.y-self.y*other.x
        return wektor3D(x,y,z)
    """
    function calculating mixed product 
    """
    def mixed_product(self, other1, other2):
        return self.dot_product(other1.cross_product(other2))
    

# Proszę utworzyć funkcje obliczające odpowiednio (jako parametry przekazujemy obiekty wcześniej utworzonej klasy):
# strumień indukcji magnetycznej: Φ=B•S
# siłę Lorentza F=q(E+v × B)
# pracę siły Lorentza W=qE•v

def magnetic_flux(B,S):
    """
    This function calculates magnetic flux using class wektor3D
    """
    if all(isinstance(p,wektor3D) for p in (B,S)):
        return B.dot_product(S)
    else:
        return None

def lorentz_force(q,E,v,B):
    """
    This function calculates lorentz force using class wektor3D
    """
    if all(isinstance(p,wektor3D) for p in (E,v,B)):
        return q*E + q*(v.cross_product(B))
    else:
        return None 

def lorentz_force_work(q,E,v):
    """
    This function calculates lorentz_force_work using class wektor3D
    """
    if all(isinstance(p,wektor3D) for p in (E,v)):
        return q*(E.dot_product(v))
    else:
        return None