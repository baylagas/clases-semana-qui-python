import datetime

"""
fechas en python

una fecha en python no es un tipo de dato propio
pero si podemos importar un modulo llamado datetime para trabajar
con fechas como si fueran objetos de fecha
"""
# date = datetime.datetime.now()
# print(date)

"""
date output
la fechas contienen anio, mes, dia , hora, minutos, segundos y microsegundos
el modulo datetime tiene metodos que nos regresan informacion acerca de este objeto
"""

# date = datetime.datetime.now()
# print(date.year)
# print(date.strftime("%A"))


"""
tambien podemos crear nuestras propias fechas
podemos utilizar el constructor de datetime para enviarle el anio, mes y dia
"""

# mybirthday = datetime.datetime(1981, 6, 23)
# print(mybirthday)
# print(mybirthday.strftime("%A"))

"""
strftime()
string format time
este metodo nos permite formatear la forma de ver la fecha
"""
date = datetime.datetime.now()
print(date.strftime("%A"))
print(date.strftime("%A|%B"))
print(date.strftime("%Y"))
print(date.strftime("%A|%B::%Y"))

"""
https://www.w3schools.com/python/python_datetime.asp
"""