import random

def spin_row():
    symbols = ['🍈',  '🍎',  '🍌',  '🍊']
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍈':
            return bet * 2
        elif row[0] == '🍎':
            return bet * 3
        elif row[0] == '🍌':
            return bet * 4
        elif row[0] == '🍊':
            return bet * 5
    return 0
    
def main():
    balance = 100
    
    print("<welcome to slots>")
    print("symbols: 🍈 🍎 🍌 🍊")
    
    while balance > 0:
        print(f"current blance: ${balance}")
        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue
        if bet <= 0:
            print("bet must be greater than 0")
            continue
        balance -= bet

        row = spin_row()
        print("spinning... \n")
        print_row(row)

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("sorry you lost this round")        
        
        balance += payout      

        play_again = input("do you want to spin again? (y/n): ").upper()
        if play_again != 'Y':
            break
    
    print(f"game over! your final balance is ${balance}")    

if __name__ == '__main__':
    main()
    
