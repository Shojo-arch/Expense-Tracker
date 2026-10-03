# Expense Tracker
# Expenses are saved in a json file so they are not lost

import json
import os
import calendar
from datetime import date, timedelta

FILE = "expenses.json"
expenses = []
budgets = {}

# words used by quick add to guess the category
keywords = {
    "food": ["lunch", "dinner", "breakfast", "coffee", "tea", "snack", "pizza"],
    "transport": ["uber", "ola", "bus", "metro", "petrol", "taxi", "auto"],
    "shopping": ["shirt", "shoes", "clothes", "amazon"],
    "bills": ["rent", "electricity", "wifi", "recharge"],
}

# load old data if the file exists
if os.path.exists(FILE):
    with open(FILE) as f:
        data = json.load(f)
        expenses = data["expenses"]
        budgets = data["budgets"]


def save():
    with open(FILE, "w") as f:
        json.dump({"expenses": expenses, "budgets": budgets}, f, indent=4)


def get_number(text):
    try:
        n = float(input(text))
        if n > 0:
            return n
    except ValueError:
        pass
    print("Please enter a valid number")
    return None


def add_expense(amount, category, note, d):
    expenses.append({"amount": amount, "category": category, "note": note, "date": str(d)})
    save()
    print("Added!")


def add():
    amount = get_number("Amount: ")
    if amount is None:
        return
    add_expense(amount, input("Category: ").lower(), input("Note: "), date.today())


def view():
    total = 0
    for e in expenses:
        print(e["date"], e["category"].ljust(12), str(e["amount"]).ljust(8), e["note"])
        total += e["amount"]
    print("Total:", total)


def spent_this_month(category):
    month = str(date.today())[:7]
    total = 0
    for e in expenses:
        if e["category"] == category and e["date"][:7] == month:
            total += e["amount"]
    return total


def summary():
    categories = set()
    for e in expenses:
        categories.add(e["category"])
    for cat in categories:
        print(cat.ljust(12), spent_this_month(cat))


def set_budget():
    category = input("Category: ").lower()
    limit = get_number("Monthly budget: ")
    if limit is not None:
        budgets[category] = limit
        save()
        print("Budget saved!")


# UNIQUE FEATURE 1: quick add
# type a sentence like "coffee 120 yesterday" and it finds the amount, date and category
def quick_add():
    words = input("Type your expense: ").lower().split()
    amount = None
    d = date.today()
    note_words = []
    for word in words:
        if word.replace(".", "", 1).isdigit():
            amount = float(word)
        elif word == "yesterday":
            d = date.today() - timedelta(days=1)
        else:
            note_words.append(word)

    if amount is None:
        print("No amount found")
        return

    category = "other"
    for cat in keywords:
        for word in note_words:
            if word in keywords[cat]:
                category = cat
    print("Category guessed:", category)
    add_expense(amount, category, " ".join(note_words), d)


# UNIQUE FEATURE 2: forecast
# predicts the spending at the end of the month using the average spent per day
def forecast():
    today = date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    days_left = days_in_month - today.day + 1
    for cat in budgets:
        spent = spent_this_month(cat)
        predicted = spent / today.day * days_in_month
        print(cat, "- budget:", budgets[cat], "spent:", spent, "predicted:", round(predicted))
        if spent >= budgets[cat]:
            print("  Budget already used up!")
        elif predicted > budgets[cat]:
            print("  You will go over! Spend less than", round((budgets[cat] - spent) / days_left), "per day")
        else:
            print("  On track. You can spend", round((budgets[cat] - spent) / days_left), "per day")


while True:
    print("\n1. Add  2. Quick add  3. View  4. Summary  5. Budget  6. Forecast  7. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add()
    elif choice == "2":
        quick_add()
    elif choice == "3":
        view()
    elif choice == "4":
        summary()
    elif choice == "5":
        set_budget()
    elif choice == "6":
        forecast()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
