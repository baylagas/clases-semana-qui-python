# formato de cadenas
# price = 20.00
# texto = "el precio del peluche es $" + str(price)
# print(texto)

# metodo format()
# price = 20.00
# product = "peluche"
# texto = "el precio del {} es ${}".format(product, price)
# print(texto)

# price = 500000.00
# product = "lambo"
# texto = "el precio del {} es ${}".format(product, price)
# print(texto)

# price = 20.3
# product = "peluche"
# texto = "el precio del {} es ${:.2f}".format(product, price)
# print(texto)

# formato indexado
# price = 20.3
# product = "peluche"
# brand = "mattel"
# texto = "el precio del {0} marca {1} es ${2}".format(product, brand, price)
# print(texto)

# price = 20.3
# product = "peluche"
# brand = "mattel"

# texto = "el precio del {0} marca {1} es ${2:10.2f}".format(product, brand, price)
# print(texto)

# formato de indice por nombre
# texto = "el precio del {product} marca {brand} es ${price:12.2f}"
# print(texto.format(product="carro", brand="ferrari", price=600000.0))

# f string
# price = 20.3
# product = "peluche"
# brand = "mattel"

# texto = f"el precio del {product} " + f"marca {brand} es ${price:10.2f}"
# print(texto)
