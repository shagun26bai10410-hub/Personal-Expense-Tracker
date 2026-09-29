def valid_amount(amount):
    return amount.replace(".", "", 1).isdigit()


def valid_number(number):
    return number.isdigit()


def valid_choice(choice):
    return choice in (
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10"
    )