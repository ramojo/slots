import random


MAX_LINES = 3 # Caps lock makes it a constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3 # Rows of slot machine
COLS = 3 # Columns of slot machine

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
            winning_lines.append(line + 1)
    
    return winnings, winning_lines
        

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # Use underscore instead of i if you dont care about the count in python 
            all_symbols.append(symbol)
        
        
    # columns = [[], [], [] ]  # We are sstarting with the columns and the rows not how we usually atart with rows then columns
    columns = []
    for _ in range(cols):
        column = []
        # using : which is a slice operator makes a copy of all_symbols instead of referencing it if we had just done all_symbols[]
        current_symbols = all_symbols[:] 
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                # print(column[row], "|")
                # To make sure the line ends without the default \n of the print funtion we do this:
                print(column[row], end=" | ")
            else:
                # print(column[row])
                print(column[row], end="")
                
        print()
    
def deposit():
    while True:
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            
            if amount > 0:
                break 
            else:
                print("Amount to deposit should be greater than zero (0).")
        
        else:
            print("Please enter a number! ")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            
            # if lines > 0 and lines <= MAX_LINES: I'll use the alternative method
            if 1 <= lines <= MAX_LINES:
                break 
            else:
                print("Lines entered are not between 1 and 3")
        
        else:
            print("Please enter a number! ")
            
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            
            if MIN_BET <= amount <= MAX_BET:
                break 
            else:
                # I'll use an f string thats's only available in python 3.6 and above
                print(f"Amount to bet should be between ${MIN_BET} - ${MAX_BET}.")
        
        else:
            print("Please enter a number! ")
            
    return amount

def spin(balance):
    lines_to_play = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines_to_play
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your balance is ${balance} while your total bet would have been ${total_bet}.")
        else:
            break
        
    print(f"You are betting ${bet} on {lines_to_play} lines. Your total bet is ${total_bet}.")
    # print(balance, lines_to_play, bet)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines_to_play, bet, symbol_value)
    
    print(f"Your winnings for this round is ${winnings}!")
    # We will use the splat operator on unpack operator, *, to pass every line from the winning_lines variable to the print function 
    print(f"You won  lines: ", *winning_lines)
    
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer =="q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")
main()