#BY DEVELOPER INNOCENT KELVIN
# NEXORA - PERSONAL EXPENSE TRACKER
# PROJECT 02
# MAIN APPLICATION FILE
# STEP 1: Import functions from expenses.py

from expenses import (
    add_expense,
    view_expenses,
    calculate_total,
    largest_expense,
    filter_by_category,
    save_expenses,
    load_expenses)


# STEP 2: Create the main application function

def main():

    # Load previously saved expenses
    expenses = load_expenses()

    # STEP 3: Display the application menu repeatedly
    while True:

        print("\n================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("================================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Spending")
        print("4. Identify Largest Expense")
        print("5. Filter by Category")
        print("6. Exit")

        print("================================")

        # STEP 4: Ask the user to select an option
        choice = input("Select an option (1-6): ").strip()


        # STEP 5: Process the user's selection

        if choice == "1":

            add_expense(expenses)
            save_expenses(expenses)


        elif choice == "2":

            view_expenses(expenses)


        elif choice == "3":

            calculate_total(expenses)


        elif choice == "4":

            largest_expense(expenses)


        elif choice == "5":

            category = input("Enter category to search: ").strip()

            filter_by_category(expenses, category)


        elif choice == "6":

            save_expenses(expenses)

            print("Thank you for using Personal Expense Tracker!")
            print("Goodbye!")

            break


        else:

            print("Invalid option. Please select between 1 and 6.")


# STEP 6: Start the application

if __name__ == "__main__":
    main()
