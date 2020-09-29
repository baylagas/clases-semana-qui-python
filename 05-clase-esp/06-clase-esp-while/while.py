# while

"""
Python Loops
Python has two primitive loop commands:

while loops
for loops
"""

# contador = 1
# while contador < 6:
#     print(contador * 2)
#     contador += 1

# break statement
# contador = 1
# while contador < 10:
#     print(contador)
#     if contador == 5:
#         print("happy birthday!!")
#         break
#     contador += 1
# print("thats all folks")

# continue statement
# contador = 1
# while contador < 10:
#     print(contador)
#     if contador == 5:
#         print("happy birthday!!")
#         contador += 1
#         continue
#     contador += 1
# print("thats all folks")


# else statement
contador = 1
while contador < 10:
    print(contador)
    if contador == 5:
        print("happy birthday!!")
        contador += 1
        continue
    contador += 1
else:
    print("merry christmas!!")
print("thats all folks")
