#here we start 
from expenses import (
    add_expense,
    view_expenses,
    delete_expense
)

from budget import (
    set_budget,
    check_budget
)

from analysis import (
    expense_analysis
)

from validation import valid_choice

#here we define the fucntion
def main():

    expenses = []

    budget = 0

    while True:

        print("\n=========================")
        print("    PERSONAL EXPENSE TRACKER")
        print("=========================")

        print("1. Add your Expense")

        print("2. View your Expenses")

        print("3. Delete any of your Expense")
        print("4. Set your Monthly Budget")

        print("5. Check your Budget")
        print("6. Expense Analysis")

        print("7. Exit")

        print("===========================")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            delete_expense(expenses)

        elif choice == "4":

            budget = set_budget()

        elif choice == "5":

            check_budget(expenses, budget)

        elif choice == "6":

            expense_analysis(expenses)

        elif choice == "7":

            print("\nThank you for using")
            print("Personal Expense Tracker!")

            break

        else:

            print("Invalid choice! Please enter 1 to 7.")


main()