# funciones

# programacion procedural
"""
este paradigma lo que hace es que nos permite poder programar por medio de pasos logicos
y secuenciales de inicio a fin

"""
# programacion funcional
"""
este paradigma lo que hace es que nos permite programar por medio de funciones que hacen una
o varias acciones

"""
# programacion orientada a objetos
"""
este paradigma nos permite poder programar nuestros sistemas simulando objetos dentro de la vida
real, traducidos aun ambiente digital

    objeto en la vida real
        propiedades
            las variables (definen algo de un objeto)
        acciones
            funciones (realizar acciones)
"""

# funciones
# es un bloque de codigo que se puede mandar a llamar (con un nombre)
# y a este bloque se le puede enviar informacion en forma de parametros
# pero tambien este puede regresar valores por medio de su valor de retorno


# # es la definicion de una funcion
# def mifuncion():
#     print("hola mundo")


# # la llamada de una funcion
# mifuncion()

# parametros en una funcion
# def saludarMundo(nombre, edad):
#     print("hola mundo")
#     print("mi nombre es " + nombre + " y mi edad es " + str(edad))
#     salario = float(input("salario: "))
#     print("y mi salario es de $" + str(salario))


# # llamada de este nuevo metodo
# miNombre = "menganito"
# miEdad = int(input("edad: "))
# saludarMundo(miNombre, miEdad)
# print("thats all folks!")

# argumentos arbitrarios *args
# def listaEstudiantes(*estudiantes):
#     print(type(estudiantes))
#     print(estudiantes)
#     for estudiante in estudiantes:
#         print(estudiante)
#     print("el tercer estudiante es " + estudiantes[2])


# listaEstudiantes(
#     "balbino", "patricio", "keavy", "isabel", "dante", "rodrigo", "andres", "patricia"
# )

# argumentos palabra reservada (keywords)
# def sumaTresNumeros(numero3, numero2, numero1):
#     print(numero1 + numero2 + numero3)


# def inputUsuario():
#     listaValores = {}
#     listaValores["num1"] = 5
#     listaValores["num2"] = 6
#     listaValores["num3"] = int(input("num3: "))
#     return listaValores


# listaValor = inputUsuario()
# sumaTresNumeros(
#     numero1=listaValor["num1"], numero2=listaValor["num2"], numero3=listaValor["num3"]
# )

# argumentos arbitrarios con keywords
# def desplegarDatos(**datos):
#     print(type(datos))
#     print(datos)
#     print(
#         "nombre: "
#         + datos["nombre"]
#         + " | apellido: "
#         + datos["apellido"]
#         + " | dui: "
#         + datos["dui"]
#         + " | edad: "
#         + str(datos["edad"])
#         + " | doble edad: "
#         + str(datos["edad"] * 2)
#     )


# desplegarDatos(nombre="balbino", apellido="aylagas", dui="45456767", edad=23)

# valor de parametro por defecto
# def miPaisProcedencia(country="Noruega"):
#     print("yo naci en " + country)


# miPaisProcedencia("el salvador")
# miPaisProcedencia("alemania")
# miPaisProcedencia()
# miPaisProcedencia("narnia")
# print("hola", "que", "tal")
# print("hola", "que", "tal", sep="*")

# retornar valores
# def suma(num1, num2):
#     res = num1 + num2
#     return res


# resultado = suma(5, 6)
# print(resultado)

# pass statement
# def bienComplejoYFumado():
#     pass
