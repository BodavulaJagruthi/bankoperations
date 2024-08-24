class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account number {self.account_number} - holder name {self.holder_name}: Balance {self.balance}"

def main():
    accounts = {}
    
    while True:
        print("\nSelect 1/2/3 to perform your respective operation")
        print("1. Create new account")
        print("2. Access existing account")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            accounts[account_number] = BankAccount(account_number, holder_name, initial_balance)#here accounts is the dictonary which only has keys in that keys it can store value
            print("Account created successfully!")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]#if account_number matches the key value that was in accounts then it store that whole information in account
                while True:
                    print(f"\n{account}")#as it is obj so it automatically get the data that was in "__str__"
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check balance")
                    print("4. Return to main menu")
                    
                    action = input("Enter your choice (1-4): ")
                    
                    if action == '1':
                        amount = float(input("Enter deposit amount: "))
                        if account.deposit(amount):
                            print("Deposit successful!")
                        else:
                            print("Invalid deposit amount.")
                    elif action == '2':
                        amount = float(input("Enter withdrawal amount: "))
                        if account.withdraw(amount):
                            print("Withdrawal successful!")
                        else:
                            print("Invalid withdrawal amount or insufficient funds.")
                    elif action == '3':
                        print(f"Current balance: ${account.get_balance()}")
                    elif action == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Account not found.")
        
        elif choice == '3':
            print("Thank you for using the Bank Account Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()