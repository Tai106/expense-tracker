from expense import Expense
import calendar
from datetime import date


def main():
    print(f"💵 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2500

    # Get user to input expense
    expense = get_user_expense()

    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"💲 Getting User Expense")
    expense_name = input("Enter expense: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["🥪 Food", "🏡 Home", "💼 Work", "🎉 Fun", "💡 Misc",]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"💲 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"💲 Summarizing User Expense")
    expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(name=expense_name, amount=float(
                expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key} : ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"Total spent ${total_spent:.2f} this month!")

    remaning_budget = budget - total_spent
    print(f"Budget Remaining: ${remaning_budget:.2f}")

    # Get the current date
    today = date.today()

    # Get the last day of the current month
    _, last_day = calendar.monthrange(today.year, today.month)

    # Calculate the remaining days in the current month
    remaining_days = last_day - today.day
    print(f"Remaining days in the current month: {remaining_days}")

    daily_budget = remaning_budget / remaining_days
    print(f"Budget Per Day: ${daily_budget:.2f}")

# def green(text):
#     return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()
