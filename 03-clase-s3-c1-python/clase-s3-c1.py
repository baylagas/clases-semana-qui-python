# # Cadenas
# mensaje = "tengo suenio"
# print(mensaje)

# # es que toda cadena se transforma en un arreglo de caracteres
# mensaje = "este es el anio de dragon"
# print(mensaje[1])

# # slicing (pedacear)
# mensaje = "este es el anio de dragon"
# print(mensaje[19:26])
# print(mensaje[0:26:2])
# mensaje = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
# print(mensaje[::2])

# # https://www.lipsum.com/

# # negative indexing slicing (pedazos negativos)
# mensaje = "este es el anio de dragon"
# print(mensaje[-26:])

# # longitud de una cadena
# mensaje = "este es el anio de dragon"
# longitud = len(mensaje)
# print(longitud)
# print(mensaje[:longitud])

# # strip() nos ayuda a quitar los caracteres en blanco a los extremos de una cadena
# mensaje = "        este  es el anio de dragon         "
# print(mensaje.strip())

# # lower
# mensaje = "Este Es El Anio De Dragon"
# print(mensaje.lower())

# # upper
# mensaje = "Este Es El Anio De Dragon"
# print(mensaje.upper())

# # replace
# mensaje = "Este Es El Anio De Dragon"
# print(mensaje.replace("Dragon", "Conejito"))

# mensaje = "yo %nombre doy por confesado el crimen"
# nombre = "balbino"
# print(mensaje.replace("%nombre", nombre))

# # split()
# mensaje = "manzana|uva|fresa|sand|ia"
# print(mensaje.split("|"))
# listaFrutas = mensaje.split("|")
# print(listaFrutas[3])

# # revisar si existe una cadena en otra
# mensaje = "Este Es El Anio De Dragon"
# resultado = "Dragon" in mensaje
# if resultado:
#     print("yay")
# else:
#     print("sad")

# # revisar si no existe una cadena en otra
# mensaje = "Este Es El Anio De Dragon"
# resultado = "Dragon" not in mensaje
# if resultado:
#     print(mensaje.replace("Dragon", "Conejito"))
# else:
#     print(mensaje)

# # concatenacion
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# # formateo
# age = 36  # int
# txt = "a My name is John, I am " + str(age)  # cadena
# print(txt)
# txt = "b My name is John, I am {}".format(age)
# print(txt)
# cost = 23.54
# print(txt)
# isTodayMonday = False
# print(isTodayMonday)

# boolean values - booleano
number1 = 200
number2 = 33

result = number1 > number2
print("result: {}".format(result))

if result:
    print("number1 is greater than number2")
else:
    print("number1 is not greater than number2")
