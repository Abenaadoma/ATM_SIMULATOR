




import datetime
import os

# Global variables to store ATM state
balance = 1000.0
pin = "1234"
transaction_history = []
user_name = ""

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def authenticate():
    """Handle user authentication with PIN"""
    global user_name
    
    print("=" * 40)
    print("      WELCOME TO ATM SIMULATOR")
    print("=" * 40)
    
    # Get user name
    user_name = input("enter your name: ")
    print(f"hello {user_name}!")
    
    attempts = 3
    while attempts > 0:
        entered_pin = input(f"\nenter your pin ({attempts} attempts remaining): ")
        
        if entered_pin == pin:
            print(f"\nlogin successful! welcome {user_name}!")
            input("press enter to continue...")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"incorrect pin. {attempts} attempts remaining.")
            else:
                print("too many incorrect attempts. access denied.")
                return False
    
    return False

def show_menu():
    """Display the main menu options"""
    global user_name
    
    clear_screen()
    print("=" * 40)
    print("           ATM MAIN MENU")
    print(f"         Welcome {user_name}")
    print("=" * 40)
    print("1. check balance")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. transaction history")
    print("5. change pin")
    print("6. exit")
    print("=" * 40)

def check_balance():
    """Display current account balance"""
    global balance
    
    clear_screen()
    print("=" * 40)
    print("         BALANCE INQUIRY")
    print("=" * 40)
    print(f"current balance: ₵{balance:.2f}")
    print("=" * 40)
    
    while True:
        choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
        if choice == 'm':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("invalid choice. please enter 'm' for main menu or 'e' to exit.")

def deposit():
    """Handle money deposits"""
    global balance, transaction_history
    
    clear_screen()
    print("=" * 40)
    print("           DEPOSIT MONEY")
    print("=" * 40)
    
    try:
        amount = float(input("enter deposit amount: ₵"))
        
        if amount <= 0:
            print("invalid amount. please enter a positive number.")
            while True:
                choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
                if choice == 'm':
                    return
                elif choice == 'e':
                    exit_program()
                else:
                    print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
            return
        
        # Update balance
        balance += amount
        
        # Record transaction
        transaction = {
            'type': 'deposit',
            'amount': amount,
            'balance': balance,
            'timestamp': datetime.datetime.now()
        }
        transaction_history.append(transaction)
        
        # Print receipt
        print_receipt(transaction)
        
    except ValueError:
        print("invalid input. please enter a valid number.")
        while True:
            choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
            if choice == 'm':
                return
            elif choice == 'e':
                exit_program()
            else:
                print("invalid choice. please enter 'm' for main menu or 'e' to exit.")

def withdraw():
    """Handle money withdrawals"""
    global balance, transaction_history
    
    clear_screen()
    print("=" * 40)
    print("          WITHDRAW MONEY")
    print("=" * 40)
    
    print(f"current balance: ₵{balance:.2f}")
    
    try:
        amount = float(input("enter withdrawal amount: ₵"))
        
        if amount <= 0:
            print("invalid amount. please enter a positive number.")
            while True:
                choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
                if choice == 'm':
                    return
                elif choice == 'e':
                    exit_program()
                else:
                    print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
            return
        
        # Check if sufficient balance
        if amount > balance:
            print("insufficient funds.")
            while True:
                choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
                if choice == 'm':
                    return
                elif choice == 'e':
                    exit_program()
                else:
                    print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
            return
        
        # Process withdrawal
        balance -= amount
        
        # Record transaction
        transaction = {
            'type': 'withdrawal',
            'amount': amount,
            'balance': balance,
            'timestamp': datetime.datetime.now()
        }
        transaction_history.append(transaction)
        
        # Print receipt
        print_receipt(transaction)
        
    except ValueError:
        print("invalid input. please enter a valid number.")
        while True:
            choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
            if choice == 'm':
                return
            elif choice == 'e':
                exit_program()
            else:
                print("invalid choice. please enter 'm' for main menu or 'e' to exit.")

def show_transaction_history():
    """Display transaction history"""
    global transaction_history
    
    clear_screen()
    print("=" * 50)
    print("           TRANSACTION HISTORY")
    print("=" * 50)
    
    if len(transaction_history) == 0:
        print("no transactions found.")
    else:
        print("date         time     type         amount     balance")
        print("-" * 50)
        
        # Show last 10 transactions
        recent_transactions = transaction_history[-10:]
        for transaction in recent_transactions:
            date_str = transaction['timestamp'].strftime("%Y-%m-%d")
            time_str = transaction['timestamp'].strftime("%H:%M:%S")
            transaction_type = transaction['type']
            amount = transaction['amount']
            balance_at_time = transaction['balance']
            
            print(f"{date_str} {time_str} {transaction_type:<12} ₵{amount:<9.2f} ₵{balance_at_time:<9.2f}")
    
    print("=" * 50)
    
    while True:
        choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
        if choice == 'm':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("invalid choice. please enter 'm' for main menu or 'e' to exit.")

def print_receipt(transaction):
    """Print a transaction receipt"""
    global user_name
    
    print("\n" + "=" * 30)
    print("        ATM RECEIPT")
    print("=" * 30)
    print(f"account holder: {user_name}")
    print(f"transaction: {transaction['type']}")
    print(f"amount: ₵{transaction['amount']:.2f}")
    print(f"new balance: ₵{transaction['balance']:.2f}")
    print(f"date: {transaction['timestamp'].strftime('%Y-%m-%d')}")
    print(f"time: {transaction['timestamp'].strftime('%H:%M:%S')}")
    print("=" * 30)
    print("thank you for using our atm!")
    print("=" * 30)
    
    while True:
        choice = input("\nenter 'm' to return to main menu or 'e' to exit: ").lower()
        if choice == 'm':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("invalid choice. please enter 'm' for main menu or 'e' to exit.")

def change_pin():
    """Allow user to change their PIN"""
    global pin
    
    clear_screen()
    print("=" * 40)
    print("           CHANGE PIN")
    print("=" * 40)
    
    current_pin = input("enter current pin: ")
    if current_pin != pin:
        print("incorrect current pin.")
        while True:
            choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
            if choice == 'm':
                return
            elif choice == 'e':
                exit_program()
            else:
                print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
        return
    
    new_pin = input("enter new pin (4 digits): ")
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("pin must be exactly 4 digits.")
        while True:
            choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
            if choice == 'm':
                return
            elif choice == 'e':
                exit_program()
            else:
                print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
        return
    
    confirm_pin = input("confirm new pin: ")
    if new_pin != confirm_pin:
        print("pins do not match.")
        while True:
            choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
            if choice == 'm':
                return
            elif choice == 'e':
                exit_program()
            else:
                print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
        return
    
    pin = new_pin
    print("pin changed successfully!")
    while True:
        choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
        if choice == 'm':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("invalid choice. please enter 'm' for main menu or 'e' to exit.")

def exit_program():
    """Handle program exit"""
    global user_name
    
    clear_screen()
    print("=" * 40)
    print(f"thank you for using our atm, {user_name}!")
    print("have a great day!")
    print("=" * 40)
    exit()

def main():
    """Main program function"""
    global user_name
    
    print("starting atm simulator...")
    
    # Authentication
    if not authenticate():
        return
    
    # Main program loop
    while True:
        show_menu()
        
        try:
            choice = input("select an option (1-6): ")
            
            if choice == '1':
                check_balance()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdraw()
            elif choice == '4':
                show_transaction_history()
            elif choice == '5':
                change_pin()
            elif choice == '6':
                exit_program()
            else:
                print("invalid option. please select 1-6.")
                while True:
                    choice = input("enter 'm' to return to main menu or 'e' to exit: ").lower()
                    if choice == 'm':
                        break
                    elif choice == 'e':
                        exit_program()
                    else:
                        print("invalid choice. please enter 'm' for main menu or 'e' to exit.")
                
        except KeyboardInterrupt:
            print("\n\nsession terminated by user.")
            break
        except Exception as e:
            print(f"an error occurred: {e}")
            input("press enter to continue...")

# Run the program
if __name__ == "__main__":
    main()