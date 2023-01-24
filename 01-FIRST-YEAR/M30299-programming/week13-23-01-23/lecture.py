class BankAccount:
    def __init__(self, an, ah, b):
        """
        Constructor to initialise the BankAccount

        :param int an: account number
        :param str ah: account holder's name
        :param float b: balance
        """
        self.account_number = an
        self.account_holder = ah
        self.balance = b
    
    def deposit(self, toAdd):
        self.balance += toAdd
    
    def withdraw(self, toRemove):
        if self.balance < toRemove:
            print("Insufficient Funds")
        else:
            self.balance -= toRemove
    
    def get_balance(self):
        return self.balance

def main():
    account = BankAccount(123456789, "John Smith", 0.0)
    account.deposit(2.50)
    print(account.get_balance())
    

main()