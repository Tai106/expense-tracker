def main():
    print(f"💵 Running Expense Tracker!")
    
    # Get user ti input expense
    get_user_expense()
    
    # Write their expense to a file
    save_expense_to_file()
    
    # Read file and summarize expense 
    summarize_expenses()
    

def get_user_expense():
    print(f"💲 Getting User Expense")
    expense_name = input("Enter expense: ")
    print(f"You've entered {expense_name}")
    

def save_expense_to_file():
    print(f"💲 Saving User Expense")
    

def summarize_expenses():
    print(f"💲 Summarizing User Expense")
    

if __name__ == "__main__":
    main()