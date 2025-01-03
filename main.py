"""import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from data_entry import get_amount, get_description, get_date, get_category

class CSV:
    csv_file = 'finance_data.csv'
    columns = ['date', 'amount', 'category', 'description']
    Format = '%d-%m-%Y'

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.csv_file, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        with open(cls.csv_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print('Entry added successfully')

    @classmethod
    def get_transactions(cls, startdate, enddate):
        try:
            df = pd.read_csv(cls.csv_file)
            df['date'] = pd.to_datetime(df['date'], format=CSV.Format)
        except Exception as e:
            print(f"Error reading or processing the CSV file: {e}")
            return

        startdate = pd.to_datetime(startdate, format=CSV.Format)
        enddate = pd.to_datetime(enddate, format=CSV.Format)

        mask = (df['date'] >= startdate) & (df['date'] <= enddate)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('No transactions were found in the specified date range.')
        else:
            print(f"Transactions from {startdate.strftime(CSV.Format)} to {enddate.strftime(CSV.Format)}:")
            print(filtered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.Format)}))

            total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
            total_expenses = filtered_df[filtered_df['category'] == 'Expenses']['amount'].sum()

            print('\nSummary:')
            print(f'Total Income: N{total_income:.2f}')
            print(f'Total Expenses: N{total_expenses:.2f}')
            print(f'Net Savings: N{total_income - total_expenses:.2f}')

            return filtered_df


def add():
    date = get_date('Enter the date of transaction (dd-mm-yyyy) or press Enter for today: ', allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transaction(df):
    df.set_index('date',inplace=True)
    
    income_df = df[df['category'] == 'Incomes'].resample('D').sum().reindex(df.index,fill_value=0)
    expense_df = df[df['category'] == 'Expenses'].resample('D').sum().reindex(df.index,fill_value=0)
    
    plt.figure(figsize=(10,5))
    plt.plot(income_df.index,income_df['amount'],label='Income',color='g')
    plt.plot(expense_df.index,expense_df['amount'],label='Expense',color='r') 
    plt.xlabel('Date')
    plt.ylabel('amount')
    plt.title('income and expense over time')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    CSV.initialize_csv()  # Initialize CSV only once
    while True:
        print('\n1. Add a new transaction')
        print('2. View transaction summary within a date range')
        print('3. Exit')
        choice = input('Enter your choice (1-3): ')
        if choice == '1':
            add()
        elif choice == '2':
            startdate = get_date('Enter the start date (dd-mm-yyyy): ')
            enddate = get_date('Enter the end date (dd-mm-yyyy): ')
            df=CSV.get_transactions(startdate, enddate)
            if df is not None and input('Do you want to see a plot? (y/n): ').lower() == 'y':
                plot_transaction(df)
        elif choice == '3':
            print('Exiting the program. Goodbye!')
            break  # Exit the loop
        else:
            print('Invalid choice. Please enter 1, 2, or 3.')



if __name__ == '__main__':
    main()
"""

import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from data_entry import get_amount, get_description, get_date, get_category

class CSV:
    csv_file = 'finance_data.csv'
    columns = ['date', 'amount', 'category', 'description']
    Format = '%d-%m-%Y'

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.csv_file, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        with open(cls.csv_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print('Entry added successfully')

    @classmethod
    def get_transactions(cls, startdate, enddate):
        try:
            df = pd.read_csv(cls.csv_file)
            df['date'] = pd.to_datetime(df['date'], format=CSV.Format)
        except Exception as e:
            print(f"Error reading or processing the CSV file: {e}")
            return

        startdate = pd.to_datetime(startdate, format=CSV.Format)
        enddate = pd.to_datetime(enddate, format=CSV.Format)

        mask = (df['date'] >= startdate) & (df['date'] <= enddate)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('No transactions were found in the specified date range.')
        else:
            print(f"Transactions from {startdate.strftime(CSV.Format)} to {enddate.strftime(CSV.Format)}:")
            print(filtered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.Format)}))

            total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
            total_expenses = filtered_df[filtered_df['category'] == 'Expenses']['amount'].sum()

            print('\nSummary:')
            print(f'Total Income: N{total_income:.2f}')
            print(f'Total Expenses: N{total_expenses:.2f}')
            print(f'Net Savings: N{total_income - total_expenses:.2f}')

            return filtered_df

def add():
    date = get_date('Enter the date of transaction (dd-mm-yyyy) or press Enter for today: ', allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transaction(df):
    df.set_index('date', inplace=True)
    
    income_df = df[df['category'] == 'Income'].resample('D').sum().reindex(df.index, fill_value=0)
    expense_df = df[df['category'] == 'Expenses'].resample('D').sum().reindex(df.index, fill_value=0)
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df['amount'], label='Income', color='g')
    plt.plot(expense_df.index, expense_df['amount'], label='Expense', color='r')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income and Expense Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    CSV.initialize_csv()  # Initialize CSV only once
    while True:
        print('\n1. Add a new transaction')
        print('2. View transaction summary within a date range')
        print('3. Exit')
        choice = input('Enter your choice (1-3): ')
        if choice == '1':
            add()
        elif choice == '2':
            startdate = get_date('Enter the start date (dd-mm-yyyy): ')
            enddate = get_date('Enter the end date (dd-mm-yyyy): ')
            df = CSV.get_transactions(startdate, enddate)
            if df is not None and input('Do you want to see a plot? (y/n): ').lower() == 'y':
                plot_transaction(df)
        elif choice == '3':
            print('Exiting the program. Goodbye!')
            break  # Exit the loop
        else:
            print('Invalid choice. Please enter 1, 2, or 3.')

if __name__ == '__main__':
    main()
