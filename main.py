import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
#looping thru every column, checking first symbol in the column to symbol next, breaks loop if symbols are match

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

#generates columns for the machine and picks random values for each row within all columns
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
#printing out slot machine. transposing horizontal row so it become vertical column
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number.")

    return amount

#asks user how many lines to bet with; checks to make sure that input number is between 1 and 3 and no string is entered
def GetNumOfLines():
    while True:
        lines = input("Enter the number of lines to bet on: (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: 
                break
            else:
                print("Enter a valid number.")

        else:
            print("Please enter a number.")
   
    return lines

#asks user for bet amount and stores it
def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET: 
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

        else:
            print("Please enter a number.")
    return bet

#ask for betting amount; checks to see if input amount is valid
def spin(balance):
    lines = GetNumOfLines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your balance is ${balance}")

        else:
            break
       
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines", *winning_lines)
    return winnings - total_bet



#will conintually ask to play unless user inputs q
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()