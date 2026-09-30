import json

bill_file = "data/bills.json"

def save_bill(bill):
    try:
        with open(bill_file, "r") as file:
            bills = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        bills = []

    bills.append(bill)

    with open(bill_file, "w") as file:
        json.dump(bills, file, indent=4)

def load_bills():
    try:
        with open(bill_file, "r") as file:
            bills = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        bills = []

    return bills