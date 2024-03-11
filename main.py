from main import Expense 


def main():
    print(f"💵 Running Expense Tracker!")

    # Get user to input expense
    get_user_expense()

    # Write their expense to a file
    save_expense_to_file()

    # Read file and summarize expense
    summarize_expenses()


def get_user_expense():
    print(f"💲 Getting User Expense")
    expense_name = input("Enter expense: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["🥪 Food", "🏡 Home", "💼 Work", "🎉 Fun", "💡 Misc"]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"    
        selected_index = int(input(f"Enter a category number {value_range}: ")) -  1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, categor=selected_category, amount=expense_amount )
            return new_expense
        else:
            print("Invalid category. Please try again!")
        
        

def save_expense_to_file():
    print(f"💲 Saving User Expense")


def summarize_expenses():
    print(f"💲 Summarizing User Expense")


if __name__ == "__main__":
    main()
