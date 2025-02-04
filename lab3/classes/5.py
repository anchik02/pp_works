class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Ошибка: недостаточно средств!")
        elif amount > 0:
            self.balance -= amount
            print(f"Снятие: -{amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма снятия должна быть положительной!")

# Пример использования
account = BankAccount("Алихан", 1000)

account.deposit(500)   # Пополнение: +500. Новый баланс: 1500
account.withdraw(200)  # Снятие: -200. Новый баланс: 1300
account.withdraw(2000) # Ошибка: недостаточно средств!
account.withdraw(-50)  # Сумма снятия должна быть положительной!