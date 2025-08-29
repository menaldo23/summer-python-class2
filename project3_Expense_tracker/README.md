# Expense Tracker (Python CLI)

A simple command-line **Expense Tracker** built in Python.\
You can add expenses, list them, calculate totals, and filter by
category.

## 📖 Features

1.  **Add an expense** -- enter an amount and category.
2.  **List all expenses** -- display all saved expenses.
3.  **Show total expenses** -- calculate the total of all expenses.
4.  **Filter by category** -- view expenses that belong to a specific
    category.
5.  **Exit** -- quit the program.

## 🚀 Usage

Run the program with:

``` bash
python expense_tracker.py
```

### Example Run

    Expense Tracker
    1. Add an expense
    2. List all expenses
    3. Show total expenses
    4. Filter expenses by category
    5. Exit
    Enter your choice: 1
    Enter amount: 12.5
    Enter category: Food

    Expense Tracker
    1. Add an expense
    2. List all expenses
    3. Show total expenses
    4. Filter expenses by category
    5. Exit
    Enter your choice: 2

    All Expenses:
    Amount: 12.5, Category: Food

## 🛠 Example Code

``` python
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break
```

## ✅ Notes

-   This is a **basic prototype** for learning purposes.
-   For a real application, you'd likely want to:
    -   Save expenses to a file or database.
    -   Add input validation (prevent negative or invalid amounts).
    -   Improve the menu navigation.

------------------------------------------------------------------------

📌 This project is for **educational purposes only**.
