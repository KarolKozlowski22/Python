import datetime
# Proszę napisać funkcję sprawdzającą poprawność numeru karty kredytowej (2p)
# Algorytm Luhna - cyfry w numerze karty indeksujemy od 15 (skrajna lewa) do 0 (skrajna prawa), indeksom parzystym nadajemy wagę jeden, 
# a nieparzystym dwa, przy czym wartości na nieparzystych indeksach podwajamy, jeśli otrzymana liczba jest większa od 10 sumujemy jej cyfry. 
# W numerze karty zastępujemy odpowiednio cyfry i przemnażamy je przez wagi, a następnie sumujemy. Jeżeli otrzymana wartość jest podzielna bez 
# reszty przez 10 uznajemy numer karty za poprawny. Wyjątek zgłaszamy w przypadku kiedy parametr przekazany do funkcji nie składa się z samych cyfr, 
# ma niepoprawną długość lub otrzymana suma kontrolna jest niepoprawna. Przykłady do testów : 924803, 1234567898765437, 1234567891234564, 1234567891234563
def Luhn(credit_card):
    """
    Function implementing Luhn algorithm, returns true if card_number is valid. Otherwise it throws an exeception 
    """
    credit_card_copy = credit_card[::-1]

    if not credit_card_copy.isdigit() or len(credit_card_copy)!=16:
        raise AttributeError('wrong length or the string contains elements different than digits')
    
    sum=0
    for i in range(16):
        if i % 2 == 0:
            sum+=int(credit_card_copy[i])
        else:
            if 2*int(credit_card_copy[i]) > 10:
                sum+=2*int(credit_card_copy[i])-9
            else:
                sum+=2*int(credit_card_copy[i])
    
    if sum % 10 == 0:
        return True
    else:
        raise ValueError('Invalid card number')
    
# Funkcję sprawdzającą poprawność numeru PESEL (3p)
# Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
# Przykłady:
# 02070803628, 8 lipca 1902, kobieta
# 02270803624, 8 lipca 2002, kobieta
# 02270812350, 8 lipca 2002, mężczyzna

# PESEL
# cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
# cyfry 3-4 to dwie cyfry miesiąca urodzenia
# cyfry 5-6 to dwie cyfry dnia urodzenia
# cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
# cyfra 11 suma kontrolna

# Do numeru miesiąca dodawane są następujące wartości w zależności od roku:
# dla lat 1800 - 1899 - 80
# dla lat 1900 - 1999 - 0
# dla lat 2000 - 2099 - 20
# dla lat 2100 - 2199 - 40
# dla lat 2200 - 2299 - 60

# Suma kontrolna: każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3 i sumuje.
# Wynik dzieli się modulo 10 i otrzymaną wartość należy odjąć od 10 i znów podzielić modulo 10.
# Otrzymana wartość powinna być zgodna z ostatnią cyfrą numeru PESEL.
# Wyjątek zgłaszamy w przypadku kiedy parametr przekazany do funkcji nie składa się z samych cyfr, ma niepoprawną długość, cokolwiek innego się nie zgadza.

def pesel_valid(pesel,birthdate,gender):

    """
    This function checks if the pesel is valid. First of all it checks if the len is correct and if the string contains only digits.
    After that it calculates month, day and year and verifies it with the given parameteres. Moreover the function catches exception
    """
    if not pesel.isdigit() or len(pesel)!=11:
        raise AttributeError('wrong length or the string contains elements different than digits')
    
    year=int(pesel[0:2])
    month=int(pesel[2:4])
    day=int(pesel[4:6])
    sex=int(pesel[9])

    if sex % 2 ==0:
        check_gender='kobieta'
    else:
        check_gender='mezczyzna'

    if month > 80 and month < 93:
        year+=1800
        month-=80
    elif month > 0 and month < 13:
        year+=1900
    elif month > 20 and month < 33:
        year+=2000
        month-=20
    elif month > 40 and month < 53:
        year+=2100
        month-=40
    elif month > 60 and month < 73:
        year+=2200
        month-=60

    else:
        raise ValueError('wrong values')
    
    
    check_list = [1,3,7,9,1,3,7,9,1,3]

    control_sum=sum([int(pesel[i])*int(check_list[i]) for i in range(10)])

    if (10-control_sum%10)%10==int(pesel[10]) and datetime.date(year,month,day) == birthdate and check_gender==gender:
        return True
    else:
        raise ValueError('Invalid control sum - invalid pesel')
    


# Funkcję zwracającą średni wiek osób, który daty urodzenia zapisane są w plik daty.in. (3p)
# Funkcja powinna móc działać w trybie 'restrykcyjnym' - po napotkaniu niepoprawnej daty/wpisu zgłoszenie wyjątku i zakończenie działania, w trybie 'liberalnym' - niepoprawne wpisy są ignorowane.
# Linia w pliku jest poprawna, jeśli zawiera dzień, miesiąc i rok,  które tworzą poprawną datę - zgodność liczby dni w miesiącu, w tym odpowiednia długość lutego w zależności od tego czy rok jest przestępny czy nie.
# Rok przestępny: podzielny przez 4 i niepodzielny przez 100 lub podzielny przez 400.
def average_age(fileName, mode):
    """
    This is a main function which calculates age and catches exceptions
    """

    with open(fileName, 'r') as file:
        total_age=0
        num_valid_dates=0
        for line in file:
            try:
                day,month,year=map(int,line.strip().split('/'))
                if is_valid_date(day,month,year):
                    age=calculate_age(day,month,year)
                    total_age+=age
                    num_valid_dates+=1
                else:
                    if mode == 'restrykcyjny':
                        raise ValueError(f"Invalid date format in line: {line.strip()}")
                    
            except Exception as e:
                    raise e
                
            
        if num_valid_dates > 0:
            return total_age/num_valid_dates
        else:
            raise ZeroDivisionError


                    

def is_valid_date(day, month, year):
    """
    Auxilary function which checks if the date is correct 
    """
    if month < 1 and month > 12:
        return False
    if day < 1 and day > days_in_month(month,year):
        return False
    
    return True

def days_in_month(month,year):

    """
    Auxilary function which returns number of days in a given month
    """
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in {4,6,9,11}:
        return 30
    else:
        return 31

    

def is_leap_year(year):

    """
    Auxilary function which cheks if the year is leap
    """
    if (year % 4 == 0 and year % 100 !=0 ) or year % 400 == 0:
        return True
    else:
        return False
    

def calculate_age(day,month,year):
    """
    Auxilary function which calculates the age
    """
    today=datetime.date.today()
    birthdate=datetime.date(year,month,day)
    age=today.year-birthdate.year
    if(birthdate.month,birthdate.day)>(today.month,today.day):
        age-=1
    
    return age 