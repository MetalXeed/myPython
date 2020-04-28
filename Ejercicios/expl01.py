""" ***COMENTADO***
print(8/12.0)

NAME = input('ESCRIBE TU NOMBRE: ')
print('Tu nombre es: ' + NAME)

"""
ftax=1.20
sdeduc=10000.00
adepen=2000.00
gincome=input('Enter the gross income: ')
ndep=input('Enter the number of dependencies: ')
fndep=float(ndep)

itax=gincome*ftax
itax=itax-sdeduc
itax=itax-sdeduc*fndep
"""
itax=(gincome*ftax-sdeduc-sdeduc*fndep)
"""
print('The income tax is: '+ itax)
