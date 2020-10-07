# ejercicio 01
clientList = []
nextClient = 0
totalCost = 0

while True:
    clientName = input("\nclient name: ")
    productName = input("product name: ")
    productCost = float(input("cost($0.00): $"))

    currentClient = (clientName, productName, productCost)
    totalCost += productCost
    print(f"\ncurrent client: {currentClient} -- totalCost: ${totalCost:.2f}")
    clientList.append(currentClient)

    nextClient = int(input("\npress 1 to add another client -- press 0 to exit: "))
    if nextClient == 0:
        break

print("\nfinal report...\n")
for client in clientList:
    print(client)
print(f"\ntotal cost: ${totalCost:.2f}")
