def expense_analysis(expenses):

    if len(expenses) == 0:

        print("No expenses available.")
        return

    total = 0

    categories = set()

    category_amount = {}

    for expense in expenses:

        total = total + expense["amount"]

        category = expense["category"]

        categories.add(category)

        if category in category_amount:

            category_amount[category] = (
                category_amount[category]
                + expense["amount"]
            )

        else:

            category_amount[category] = expense["amount"]

    print("\n===== EXPENSE ANALYSIS =====")

    print("Total Expenses:", len(expenses))
    print("Total Amount: ₹", total)

    print("\nUnique Categories:")

    for category in categories:

        print("-", category)

    print("\nCategory-wise Spending:")

    for category in category_amount:

        print(
            category,
            ": ₹",
            category_amount[category]
        )


def highest_expense(expenses):

    if len(expenses) == 0:

        print("No expenses available.")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:

            highest = expense

    print("\n===== HIGHEST EXPENSE =====")

    print("Name:", highest["name"])
    print("Amount: ₹", highest["amount"])
    print("Category:", highest["category"])


# RECURSION
def show_categories(categories, index=0):

    if index == len(categories):

        return

    print(index + 1, ".", categories[index])

    show_categories(categories, index + 1)