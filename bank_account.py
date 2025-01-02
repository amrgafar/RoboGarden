import random
import datetime

class BankAccount:
    def __init__(self, holder_name, account_type):
        self.account_number = random.randint(1000000000, 9999999999)  # Random 10-digit account number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_history.append({
            'date': datetime.datetime.now(),
            'transaction': 'Deposit',
            'amount': amount,
            'balance': self.balance
        })
        print(f"Deposited {amount}. Current balance: {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transaction_history.append({
            'date': datetime.datetime.now(),
            'transaction': 'Withdrawal',
            'amount': amount,
            'balance': self.balance
        })
        print(f"Withdrew {amount}. Current balance: {self.balance}.")

    def check_balance(self):
        return f"Current balance: {self.balance}"

    def get_account_type(self):
        return self.account_type

    def get_account_number(self):
        return self.account_number

    def get_holder_name(self):
        return self.holder_name

    def get_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        history = ""
        for transaction in self.transaction_history:
            history += f"Date: {transaction['date']}, Type: {transaction['transaction']}, Amount: {transaction['amount']}, Balance: {transaction['balance']}\n"
        return history


# Testing the BankAccount class
if __name__ == "__main__":
    # Creating a bank account for a user
    account = BankAccount(holder_name="Alice", account_type="Checking")

    print(f"Account created for {account.get_holder_name()} with account number {account.get_account_number()}.")

    # Performing some operations
    account.deposit(500)
    account.withdraw(200)
    account.deposit(1000)
    
    # Checking balance
    print(account.check_balance())
    
    # Printing transaction history
    print("\nTransaction History:")
    print(account.get_transaction_history())
