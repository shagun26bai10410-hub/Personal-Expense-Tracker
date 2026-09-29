from validation import valid_amount


def set_budget():#to set the monthly budget

    amount = input("Enter monthly budget: ₹")

    if valid_amount(amount) == False:

        print("Invalid budget!")
        return 0

    budget = float(amount)

    if budget <= 0:

        print("Budget must be greater than 0!")
        return 0

    print("Budget set successfully!")

    return budget


def check_budget(expenses, budget):

    if budget == 0:

        print("Please set your budget first.")
        return

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    remaining = budget - total

    print("\n===== BUDGET STATUS =====")
    print("Monthly Budget: ₹", budget)
    print("Total Expense: ₹", total)

    if remaining >= 0:

        print("Remaining Budget: ₹", remaining)

    else:

        print("Budget exceeded by: ₹", abs(remaining))