def show_balance(balance):
    print(f"Your balance is : {balance:.2f}")

def deposit():
    amount = float(input("Enter the deposit amount:"))
    if amount < 0:
        print("That's not a valid number")
        return 0
    else:
        return amount

def withdrawn(balance):
    amount = float(input("Enter the withdrawn amount:"))
    if amount > balance:
        print("Insufficient amount")
        return 0
    elif amount < 0:
        print("amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    balance = 50000
    is_running = True
    while is_running:
        print("1. show balance")
        print("2. deposit")
        print("3. withdrawn")
        print("4. exit")
        choice = input("Enter your choice (1-4):")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdrawn(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That's not a valid choice")
    print("Thank you! Have a nice day!!")

if __name__ == "__main__":
    main()
