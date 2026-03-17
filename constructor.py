class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def show(self):
        print("Account:", self.acc_no)
        print("Balance:", self.balance)

a1 = BankAccount(101, 5000)
a2 = BankAccount(102, 8000)

a1.show()
a2.show()