from datetime import datetime

# Date format and category mappings
date_format = '%d-%m-%Y'
categories = {'I': 'Income', 'E': 'Expenses'}

def get_date(prompt, allow_default=False):
    """Get a date input from the user with optional default to today's date."""
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)  # Return the formatted date as a string
    except ValueError:
        print('Invalid date, please enter in this format (dd-mm-yyyy)')
        return get_date(prompt, allow_default)

def get_amount():
    """Get a valid positive amount from the user."""
    try:
        amount = float(input("Enter a valid amount: "))
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    """Get a valid category (Income or Expenses) from the user."""
    category = input('Enter the category ("I" for Income, "E" for Expenses): ').strip().upper()
    if category in categories:
        return categories[category]
    else:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expenses.")
        return get_category()

def get_description():
    """Get a description for the transaction."""
    return input('Enter a description: ').strip()