"""
 реализовать класс BankAccount, описывающий банковский счёт простого вида. У счёта должны быть:
        владелец счёта (строка, имя);
        номер счёта (строка или число);
        текущий баланс (число, не может быть отрицательным);
При создании счёта баланс может задаваться, а если не задан — считается 0.

Класс BankAccount должен уметь:
    Создавать новый счёт в конструкторе init
    deposit(amount) — пополнение счёта на сумму amount.
    withdraw(amount) — снятие денег со счёта. Нельзя уйти в минус.
    transferto(otheraccount, amount) — перевод денег на другой счёт BankAccount.
    info() — возвращать строку с краткой информацией о счёте
    @classmethod def getaccountscreated(cls) — возвращает количество созданных счетов.
"""


class BankAccount:
    account_count:int = 0

    def __init__(self,name:str, account_number:int, current_balance: float):
        self.name = name
        self.account_number = account_number
        self.current_balance = current_balance
        
        BankAccount.account_count += 1


    def deposit(self, amount:float):
        self.current_balance += amount
        print(f"{self.current_balance}")

    def withdraw(self, amount:float):
        if self.current_balance < amount:
            print("No money for withdraw")
            return
        self.current_balance -= amount
        print(f"{self.current_balance} on {self.account_number}")

    def transferTo(self, BankAccount, amount:float):
        if self.current_balance < amount:
            return
        self.current_balance -= amount

        BankAccount.current_balance += amount

        print(f"to {BankAccount.account_number} transfer {amount}")

    def info(self):
        print(f"At {self.account_number} are {self.current_balance}")

    @classmethod
    def getaccountscreated(cls):
        print(f"Are created {cls.account_count}")

    # Создаем 5 аккаунтов
a1 = BankAccount("Алексей", 1001, 1000.0)
a2 = BankAccount("Мария", 1002, 500.0)
a3 = BankAccount("Иван", 1003, 200.0)
a4 = BankAccount("Елена", 1004, 1500.0)
a5 = BankAccount("Дмитрий", 1005, 50.0)

# Серия переводов с проверками
a1.transferTo(a2, 200.0)   # ✅ Успешно
a2.transferTo(a3, 300.0)   # ✅ Успешно
a4.transferTo(a5, 100.0)   # ✅ Успешно
a5.transferTo(a1, 200.0)   # ❌ Недостаточно (150 < 200)
a3.transferTo(a4, 400.0)   # ✅ Успешно (200 + 300 - 400 = 100)
a1.transferTo(a5, 500.0)   # ✅ Успешно (800 - 500 = 300)
a3.transferTo(a2, 150.0)   # ❌ Недостаточно (100 < 150)
a4.transferTo(a3, 600.0)   # ✅ Успешно
a5.transferTo(a1, 300.0)   # ✅ Успешно (650 - 300 = 350)
a2.transferTo(a4, 1000.0)  # ❌ Недостаточно (400 < 1000)

# Итог
print("\n" + "=" * 40)
for acc in [a1, a2, a3, a4, a5]:
    acc.info()
BankAccount.getaccountscreated()