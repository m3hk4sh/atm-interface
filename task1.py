from datetime import datetime

class User:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def authenticate(self, pin):
        return self.pin == pin

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

class ATM:
    def __init__(self):
        self.user = None

    def display_menu(self):
        print("1. View Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Quit")

    def process_transaction(self, user, transaction_type, amount):
        if transaction_type == 1:
            self.view_balance(user)
        elif transaction_type == 2:
            self.withdraw(user, amount)
        elif transaction_type == 3:
            self.deposit(user, amount)
        elif transaction_type == 4:
            self.transfer(user, amount)
        elif transaction_type == 5:
            self.view_transaction_history(user)

    def view_balance(self, user):
        print(f"Your balance is: {user.balance}")

    def withdraw(self, user, amount):
        if amount > user.balance:
            print("Insufficient balance")
        else:
            user.balance -= amount
            user.add_transaction(Transaction("Withdrawal", amount))
            print(f"Withdrawal successful. New balance: {user.balance}")

    def deposit(self, user, amount):
        user.balance += amount
        user.add_transaction(Transaction("Deposit", amount))
        print(f"Deposit successful. New balance: {user.balance}")

    def transfer(self, user, amount):
        recipient_id = input("Enter recipient's user ID: ")
        # Logic for transferring amount to recipient
        print("Transfer successful")

    def view_transaction_history(self, user):
        print("Transaction History:")
        for transaction in user.transaction_history:
            print(f"{transaction.timestamp} - {transaction.transaction_type}: {transaction.amount}")

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

def main():
    atm = ATM()
    user = User("123456", "1234", 1000)  # Example user

    pin = input("Enter your PIN: ")
    if user.authenticate(pin):
        while True:
            atm.display_menu()
            choice = int(input("Enter your choice: "))
            if choice == 6:
                print("Exiting...")
                break
            amount = 0
            if choice in [2, 3, 4]:
                amount = float(input("Enter amount: "))
            atm.process_transaction(user, choice, amount)
    else:
        print("Authentication failed. Exiting...")

if __name__ == "__main__":
    main()
