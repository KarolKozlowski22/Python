#!/usr/bin/env python3
import datetime
import functions
import logging

logging.basicConfig(filename="test.log", filemode='w',format='%(asctime)s %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
#1

#help(functions.Luhn)

print("Testowanie poprawnosci numeru karty kredytowej")
try:
    functions.Luhn('924803')
except ValueError as e:
    logger.error(f'error - {e}')

except AttributeError as e:
    logger.error(f'error - {e}')

else:
    logger.info('card number is valid')


try:
    functions.Luhn('1234567898765437')
except ValueError as e:
    logger.error(f'error - {e}')

except AttributeError as e:
   logger.error(f'error - {e}')

else:
    logger.info('card number is valid')

try:
    functions.Luhn('1234567891234564')
except ValueError as e:
    logger.error(f'error - {e}')

except AttributeError as e:
    logger.error(f'error - {e}')

else:
    logger.info('card number is valid')

try:
    functions.Luhn('11234567891234563')
except ValueError as e:
   logger.error(f'error - {e}')

except AttributeError as e:
    logger.error(f'error - {e}')

else:
    logger.info('card number is valid')


print("Testowanie poprawnosci numeru pesel")

    
#2

#help(functions.pesel_valid)
try:
    functions.pesel_valid('02070803628',datetime.date(1902,7,8),'kobieta')

except ValueError as e:
    logger.error(f'error - {e}')

except AttributeError as e:
    logger.error(f'error - {e}')
else:
    logger.info('pesel number is valid')

try:
    functions.pesel_valid('02270803624',datetime.date(2002,7,8),'kobieta')
except ValueError as e:
   logger.error(f'error - {e}')

except AttributeError as e:
    logger.error(f'error - {e}')
else:
    logger.info('pesel number is valid')
   


try:
    functions.pesel_valid('02270812350',datetime.date(2002,7,8),'mezczyzna')
except ValueError as e:
    logger.error(f'error - {e}')
except AttributeError as e:
    logger.error(f'error - {e}')
else:
    logger.info('pesel number is valid')
    




#3

try:
    wynik=functions.average_age("daty.in", 'restrykcyjny')
except ValueError as e:
    logger.error(f'error - {e}')
except ZeroDivisionError as e:
    logger.error(f'error - {e}')
else:
    logger.info(f'wynik - {wynik}')


try:
    wynik=functions.average_age("daty.in", 'liberalny')
except ValueError as e:
    logger.error(f'error - {e}')
except ZeroDivisionError as e:
    logger.error(f'error - {e}')
else:
    logger.info(f'wynik - {wynik}')





