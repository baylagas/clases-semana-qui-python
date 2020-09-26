"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?
    

"""

# creando la lista vacia
listaRegistro = []
# cliente = input("nombre del cliente: ")
# producto = input("producto: ")
# costo = float(input("costo ($0.00): "))

cliente = "pepito"
producto = "brownie"
costo = 3.0

# punto de programa
# registro = {"cliente": cliente, "producto": producto, "costo": costo}
registro = dict(cliente=cliente, producto=producto, costo=costo)
# como agrego un elemento nuevo a una lista?
listaRegistro.append(registro)
# dejar de ocupar la variable registro
# registro = None
