class account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
    def get_balance(self):
        return self._balance
    
    
class current_account(account):
    Overdraw = 1000
    def withdraw(self, amount):
        if 0 < amount <= self._balance + 1000:
            self._balance -= amount
            print(f"Withdrew: {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds or overdraw limit error.")

class saving_account(account):
    Interest_rate = 0.005
    def add_interest(self):
        interest = self._balance * self.Interest_rate
        self._balance += interest
        print(f"Interest added: {interest}. New balance: {self._balance}")
        

class bank:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self, account_type, account_number, account_holder, initial_deposit=0):
        if account_type == "current":
            acc = current_account(account_number, account_holder, initial_deposit)
        elif account_type == "saving":
            acc = saving_account(account_number, account_holder, initial_deposit)
        else:
            print("Invalid account type.")
            return
        self.accounts[account_number] = acc
        print(f"Account created: {account_number} for {account_holder}")
        
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    

# Example usage
my_bank = bank()
my_bank.create_account("current", "12345", "Alice", 1000)
my_bank.create_account("saving", "67890", "Bob", 5000)
account = my_bank.get_account("12345")
if account:
    account.deposit(200)
    account.withdraw(150)
    account = my_bank.get_account("67890")
if account:
    account.deposit(100)
    account.add_interest()