from expense import Expense 


def main():
    print(f"💵 Running Expense Tracker!")
    expense_file_path = "expense.csv"

    # Get user to input expense
    # expense = get_user_expense()

    # Write their expense to a file
    # save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expenses(expense_file_path)


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
        
        

def save_expense_to_file(expense, expense_file_path):
    print(f"💲 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expenses(expense_file_path):
    print(f"💲 Summarizing User Expense")
    expenses = list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
    

    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category 



if __name__ == "__main__":
    main()
