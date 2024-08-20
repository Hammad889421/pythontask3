import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file)

    def log_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.expenses.append(expense)
        self.save_expenses()

    def generate_report(self, month, year):
        report = {}
        for expense in self.expenses:
            expense_date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
            if expense_date.month == month and expense_date.year == year:
                category = expense['category']
                report[category] = report.get(category, 0) + expense['amount']
        return report

    def display_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']} - ${expense['amount']} - {expense['description']}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Log Expense")
        print("2. Generate Monthly Report")
        print("3. Display All Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.log_expense(amount, category, description)
        elif choice == '2':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            report = tracker.generate_report(month, year)
            print("Monthly Report:", report)
        elif choice == '3':
            tracker.display_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
