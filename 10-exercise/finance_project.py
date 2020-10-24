from income import Income
from expense import Expense
from prettytable import PrettyTable


class FinanceProject:
    # crear el metodo constructor
    def __init__(self):
        self.balance = 0.0  # variables de la clase
        self.incomeList = []
        self.expenseList = []

    def registerIncome(self, id, title, amount):
        # crear un objeto Ingreso
        income = Income(id, title, amount)
        # agregarlo a la lista de ingresos
        self.incomeList.append(income)
        self.calculateBalance()

    def registerExpense(self, id, title, amount):
        # crear un objeto Ingreso
        expense = Expense(id, title, amount)
        # agregarlo a la lista de ingresos
        self.expenseList.append(expense)
        self.calculateBalance()

    def calculateListTotal(self, transactionList):
        result = 0
        for item in transactionList:
            result += item.amount
        return result

    def calculateBalance(self):
        incomeTotal = self.calculateListTotal(self.incomeList)
        expenseTotal = self.calculateListTotal(self.expenseList)
        totalBalance = incomeTotal - expenseTotal
        self.balance = totalBalance

    def generateAllIncomeReport(self):
        # crear la pretty table
        table = PrettyTable()
        # llenar los titulos de columna
        table.field_names = ["Id", "Title", "Amount"]

        # iterar la lista de ingresos
        for income in self.incomeList:
            # agregar la informacion a la lista de la pretty table
            table.add_row([income.id, income.title, income.amount])

        # imprimir la pretty table
        print(table)
