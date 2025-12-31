expenses = []

def add_expense():
    print()
    name = input("Enter your expense name:")
    amount = float(input(f"Enter the {name} amount: ₹"))
    expenses.append({'name':name, 'amount':amount})
    print(f"Your {name} added with amount ₹{amount} 💰")
    print()

def view_expense():
    print()
    if not expenses:
        print("-------🤷🏻‍♂️ Nothing added to the expenses 🤷🏻‍♂️-------")
        print()
        return
    print("-------💸 Your Expenses 💸-------")
    total = 0

    for exp in expenses:
        print(f" - {exp['name']}: ₹{exp['amount']}")
        total += exp['amount']
    print(f"Your total spent: ₹{total} 💰")
    print()

def main():
    while True:
        print("-------📊 My Personal Expenses 📊------")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")

        choice = input("Enter choices among (1, 2, 3):")

        match choice:
            case '1':
                add_expense()
            case '2':
                view_expense()
            case '3':
                print("Thanks for checking! 👋🏻 👋🏻 Keep Saving!!")
                break
            case _:
                print("\nInvalid choices! Try again")
            
if __name__ == "__main__":
    main()






        



    
