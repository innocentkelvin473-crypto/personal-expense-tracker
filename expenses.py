# NEXORA - PERSONAL EXPENSE TRACKER
# Project 02
# Developer: Innocent Kelvin
# Description: Functions for managing expenses

# STEP 1: Import the datetime module
# This helps us work with and validate dates.

from datetime import datetime
# Import JSON to save and retrieve expense records
import json

# Import OS to manage file paths and folders
import os



# STEP 2: Create a function to add an expense
# This function collects expense details from the user.

def add_expense(expenses):

    # STEP 3: Ask the user to enter the expense amount
    try:
        amount = float(input("Enter amount: "))

        # STEP 4: Check whether the amount is valid
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        # STEP 5: Collect the remaining expense details
        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD): ").strip()

        # STEP 6: Check that category and description are not empty
        if not category or not description:
            print("Category and description are required.")
            return

        # STEP 7: Validate the date entered by the user
        datetime.strptime(date, "%Y-%m-%d")

        # STEP 8: Store the expense information in a dictionary
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date}

        # STEP 9: Add the expense dictionary to the expenses list
        expenses.append(expense)

        # STEP 10: Notify the user that the expense was recorded
        print("Expense added successfully!")

    # STEP 11: Handle invalid amounts and dates
    except ValueError:
        print("Invalid amount or date.")
    
# STEP 12: VIEW ALL EXPENSES

# This function displays all recorded expenses.

def view_expenses(expenses):

    # STEP 1: Check whether the expenses list is empty
    if not expenses:
        print("No expenses recorded.")
        return

    # STEP 2: Display all expenses using a for loop
    for expense in expenses:

        # STEP 3: Display a separator for better organization
        print("-------------------------")

        # STEP 4: Display individual expense details
        print("Amount: KSh", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("Date:", expense["date"])

    # STEP 5: Display a closing separator
    print("-------------------------")
    
# STEP 13: CALCULATE TOTAL SPENDING

# This function calculates the total amount
# of money spent across all recorded expenses.

def calculate_total(expenses):

    # STEP 1: Check whether the expenses list is empty
    if not expenses:
        print("No expenses available.")
        return 0

    # STEP 2: Calculate the total using sum()
    total = sum(
        expense["amount"]
        for expense in expenses)

    # STEP 3: Display the total spending
    print("Total spending: KSh", total)

    # STEP 4: Return the calculated
# ==========================================
# STEP 14: IDENTIFY THE LARGEST EXPENSE

# This function identifies the expense
# with the highest monetary value.

def largest_expense(expenses):

    # STEP 1: Check whether the expenses list is empty
    if not expenses:
        print("No expenses available.")
        return None

    # STEP 2: Find the expense with the highest amount
    largest = max( expenses, key=lambda expense: expense["amount"])

    # STEP 3: Display the largest expense
    print("Largest Expense")
    print("-------------------------")
    print("Amount: KSh", largest["amount"])
    print("Category:", largest["category"])
    print("Description:", largest["description"])
    print("Date:", largest["date"])

    # STEP 4: Return the largest expense
    return largest


# STEP 15: FILTER EXPENSES BY CATEGORY

# This function searches for expenses
# belonging to a specific category.

def filter_by_category(expenses, category):

    # STEP 1: Search for expenses matching the category
    results = [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()]

    # STEP 2: Check whether matching expenses were found
    if not results:
        print("No expenses found in this category.")
        return []

    # STEP 3: Display the matching expenses
    print("Expenses in category:", category)
    print("-------------------------")

    for expense in results:

        print("Amount: KSh", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("Date:", expense["date"])
        print("-------------------------")

    # STEP 4: Return the matching expenses
    return results
# STEP 16: SAVE EXPENSES TO A JSON FILE

# This function saves expense records permanently.

def save_expenses(expenses):

    # STEP 1: Define the location of the JSON file
    file_path = os.path.join("data", "expenses.json")

    # STEP 2: Create the data folder if it does not exist
    os.makedirs("data", exist_ok=True)

    # STEP 3: Open the JSON file in write mode
    with open(file_path, "w") as file:

        # STEP 4: Convert Python data into JSON format
        json.dump(expenses, file, indent=4)

    # STEP 5: Confirm that records have been saved
    print("Expenses saved successfully!")
    
# STEP 17: LOAD EXPENSES FROM A JSON FILE

# This function retrieves previously saved expenses.

def load_expenses():

    # STEP 1: Define the location of the JSON file
    file_path = os.path.join("data", "expenses.json")

    # STEP 2: Check whether the JSON file exists
    if not os.path.exists(file_path):
        return []

    # STEP 3: Open the JSON file in read mode
    try:
        with open(file_path, "r") as file:

            # STEP 4: Convert JSON data into Python data
            expenses = json.load(file)

        # STEP 5: Return the retrieved expenses
        return expenses

    # STEP 6: Handle an empty or invalid JSON file
    except (json.JSONDecodeError, OSError):
        print("Unable to load expense records.")
        return []




