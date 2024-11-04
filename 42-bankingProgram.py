def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("enter an amount to be deposited: "))
    
    if amount < 0:
        print("that's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to be withdrawn: "))
    
    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("-" * 20)
        print("banking program")
        print("-" * 20)
        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")
        print("-" * 20)
    
        choice = input("enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("that is not a valid choice")

    print("thank you! have a nice day!")

if __name__ == '__main__':
    main()

    