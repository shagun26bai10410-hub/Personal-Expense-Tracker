from validation import valid_amount, valid_number


def add_expense(expenses):#to add daily expense

    name = input("Enter expense name: ")
    amount = input("Enter amount: ₹")
    category = input("Enter category: ")

    if valid_amount(amount) == False:
        print("Invalid amount!")
        return

    amount = float(amount)

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses(expenses):#to view  daily expense

    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n===== EXPENSE LIST =====")

    for i in range(len(expenses)):

        expense = expenses[i]

        print(
            i + 1,
            ".",
            expense["name"],
            "- ₹",
            expense["amount"],
            "-",
            expense["category"]
        )


def delete_expense(expenses):#to delete daily expenses

    if len(expenses) == 0:
        print("No expenses available.")
        return

    view_expenses(expenses)

    number = input("Enter expense number to delete: ")

    if valid_number(number) == False:
        print("Please enter a valid number!")
        return

    number = int(number)

    if number >= 1 and number <= len(expenses):

        expenses.pop(number - 1)

        print("Expense deleted successfully!")

    else:

        print("Invalid expense number!")


def search_expense(expenses):#searching daily expenses

    name = input("Enter expense name to search: ")

    found = False

    for expense in expenses:

        if expense["name"].lower() == name.lower():

            print("\n===== EXPENSE FOUND =====")
            print("Name:", expense["name"])
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])

            found = True

    if found == False:

        print("Expense not found.")