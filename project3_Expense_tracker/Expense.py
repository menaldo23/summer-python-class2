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

def add_expense(expenses, amount, category):
    """
    Adds a new expense to the list.
    - expenses: list of expense dictionaries
    - amount: the money spent (float)
    - category: category of the expense (string)
    """
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    """
    Prints all expenses in a readable format.
    - expenses: list of expense dictionaries
    """
    for expense in expenses:
        # Each expense is a dictionary like {'amount': 50.0, 'category': 'Food'}
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


def total_expenses(expenses):
    """
    Calculates the sum of all expense amounts.
    - Uses map + lambda to extract the 'amount' field from each dictionary
    - sum() adds them up
    """
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    """
    Returns an iterator of expenses that belong to the given category.
    - filter() applies a condition to each expense
    - Only those where 'category' matches are included
    - NOTE: filter() returns an iterator, not a list, so you can loop over it but not index directly.
    """
    return filter(lambda expense: expense['category'] == category, expenses)


def main():
    """
    Main program loop: provides a menu for the user to interact with.
    """
    expenses = []  # Start with an empty list of expenses
    
    while True:  # Infinite loop until user chooses to exit
        # Display the menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Ask user for a choice
        choice = input('Enter your choice: ')

        if choice == '1':
            # Add a new expense
            amount = float(input('Enter amount: '))   # Convert input to float
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Show all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # Show the total of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            # Filter and display expenses by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)  # works because print_expenses can iterate over filter
    
        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break
