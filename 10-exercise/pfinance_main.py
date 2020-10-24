"""
tendra el programa principal
"""
from finance_project import FinanceProject

project = FinanceProject()

print(f"balance: {project.balance}")

project.registerIncome(1, "salary", 1600.0)
print(f"balance: {project.balance}")

project.registerIncome(2, "classes", 250.0)
print(f"balance: {project.balance}")

project.registerExpense(1, "house payment", 930.0)
print(f"balance: {project.balance}")

project.registerExpense(1, "food", 12.0)
print(f"balance: {project.balance}")

project.registerIncome(2, "sales", 80.0)
print(f"balance: {project.balance}")


project.generateAllIncomeReport()
