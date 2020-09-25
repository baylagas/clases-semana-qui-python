# sets

# un set es una coleccion que no es ordenada y no tiene indices.
# la estructura de un set es ocupando los curly brackets {}
# carSet = {"nissan", "ferrari", "audi"}
# print(carSet)
# print(type(carSet))

# un set no esta ordenado entonces no tenemos forma de saber como el set ordenara
# los elementos por dentro

# como acceder a los items de un set
# carSet = {"nissan", "ferrari", "audi"}
# for car in carSet:
#     print(car)

# como revisar si un elemento esta en el set
# carSet = {"nissan", "ferrari", "audi", "honda"}
# if "honda" in carSet:
#     print("honda es parte del car show")

# una vez que un set esta creado no se le pueden cambiar los elementos, pero si se le pueden agregar

# como agregar elementos en un set
# carSet = {"nissan", "ferrari", "audi", "honda"}
# carSet.add("toyota")
# print(carSet)

# carSet = {"nissan", "ferrari", "audi", "honda"}
# carSet.update(["toyota", "aston martin", "bmw"])
# print(carSet)

# como obtener el tamanio de un set
# carSet = {"nissan", "ferrari", "audi", "honda"}
# print(len(carSet))

# como remover elementos de un set
# remove()
# carSet = {"nissan", "ferrari", "audi", "honda"}
# carSet.remove("honda")
# print(carSet)
# # usando el metodo remove si el elemento no existe entonces genera un error
# # discard()
# carSet = {"nissan", "ferrari", "audi", "honda"}
# carSet.discard("aston martin")
# print(carSet)
# # usando el metodo discard si el elemento no existe entonces no genera un error
# # pop()
# # este metodo remueve el elemento final del set, pero como un set no es ordenado
# # entonces no tenemos forma de saber cual elemento sacara por esta razon
# # el metodo en su retorno nos entrega ese elemento
# carSet = {"nissan", "ferrari", "audi", "honda"}
# eliminado = carSet.pop()
# print(carSet)
# print(eliminado)
# # remover completo del set, todos sus elementos
# # clear()
# carSet = {"nissan", "ferrari", "audi", "honda"}
# carSet.clear()
# print(carSet)
# tambien se puede utilizar la palabra clave del
# carSet = {"nissan", "ferrari", "audi", "honda"}
# del carSet
# print(carSet)

# como hacer la union de dos sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# resultado = set1.union(set2)
# print(resultado)
# update
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3, "a"}
# set1.update(set2)
# print(set1)
# # tanto el metodo union como el update excluyen los elementos duplicados

# # constructor de un set
# set1 = set(("a", "b", "c"))
# print(set1)
