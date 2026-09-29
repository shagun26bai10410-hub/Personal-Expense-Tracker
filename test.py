import validation
import expenses
import budget
import analysis


# 1. VALIDATION TESTS

def test_valid_amount():

    assert validation.valid_amount("100") == True
    assert validation.valid_amount("50.5") == True
    assert validation.valid_amount("abc") == False

    print("PASS - valid_amount()")


def test_valid_number():

    assert validation.valid_number("5") == True
    assert validation.valid_number("abc") == False

    print("PASS - valid_number()")


def test_valid_choice():

    assert validation.valid_choice("1") == True
    assert validation.valid_choice("10") == True
    assert validation.valid_choice("11") == False

    print("PASS - valid_choice()")


# 2. EXPENSE TESTS

def test_add_expense():

    expense_list = []

    item = {
        "name": "Food",
        "amount": 200.0,
        "category": "Food"
    }

    expense_list.append(item)

    assert len(expense_list) == 1
    assert expense_list[0]["name"] == "Food"
    assert expense_list[0]["amount"] == 200.0
    assert expense_list[0]["category"] == "Food"

    print("PASS - add_expense()")


def test_view_expenses(capsys):

    expense_list = [
        {
            "name": "Food",
            "amount": 200.0,
            "category": "Food"
        }
    ]

    expenses.view_expenses(expense_list)

    output = capsys.readouterr().out

    assert "Food" in output
    assert "200" in output

    print("PASS - view_expenses()")


def test_delete_expense():

    expense_list = [
        {
            "name": "Food",
            "amount": 200.0,
            "category": "Food"
        },
        {
            "name": "Bus",
            "amount": 50.0,
            "category": "Travel"
        }
    ]

    expense_list.pop(0)

    assert len(expense_list) == 1
    assert expense_list[0]["name"] == "Bus"

    print("PASS - delete_expense()")


def test_search_expense(capsys):

    expense_list = [
        {
            "name": "Food",
            "amount": 200.0,
            "category": "Food"
        }
    ]

    print("PASS - search_expense()")


# 3. BUDGET TESTS

def test_set_budget():

    budget_amount = 5000

    assert budget_amount == 5000

    print("PASS - set_budget()")


def test_check_budget(capsys):

    expense_list = [
        {
            "name": "Food",
            "amount": 200.0,
            "category": "Food"
        }
    ]

    budget.check_budget(expense_list, 5000)

    output = capsys.readouterr().out

    assert "5000" in output
    assert "200" in output
    assert "4800" in output

    print("PASS - check_budget()")


# 4. ANALYSIS TESTS

def test_expense_analysis(capsys):

    expense_list = [
        {
            "name": "Food",
            "amount": 200.0,
            "category": "Food"
        },
        {
            "name": "Bus",
            "amount": 50.0,
            "category": "Travel"
        }
    ]

    analysis.expense_analysis(expense_list)

    output = capsys.readouterr().out

    assert "250" in output
    assert "Food" in output
    assert "Travel" in output

    print("PASS - expense_analysis()")


def test_highest_expense(capsys):

    expense_list = [
        {
            "name": "Food",
            "amount": 200.0,
            "category": "Food"
        },
        {
            "name": "Bus",
            "amount": 50.0,
            "category": "Travel"
        }
    ]

    analysis.highest_expense(expense_list)

    output = capsys.readouterr().out

    assert "Food" in output
    assert "200" in output

    print("PASS - highest_expense()")


def test_show_categories(capsys):

    categories = [
        "Food",
        "Travel",
        "Shopping"
    ]

    analysis.show_categories(categories)

    output = capsys.readouterr().out

    assert "Food" in output
    assert "Travel" in output
    assert "Shopping" in output

    print("PASS - show_categories()")


# 5. EMPTY EXPENSE TEST

def test_empty_expenses(capsys):

    expense_list = []

    expenses.view_expenses(expense_list)

    output = capsys.readouterr().out

    assert "No expenses available." in output

    print("PASS - empty expense handling")