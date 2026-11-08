Nexora – Personal Expense Tracker

Project 02 | Python Project Challenge

Developer:Innocent Kelvin

1. Project Overview

The Personal Expense Tracker is a Python application designed to help users record, manage and monitor their daily expenses.

The application allows users to add expenses, view recorded transactions, calculate total spending, identify their largest expense and filter expenses by category.

It uses JSON to store expense records permanently.

2. Features

- Add new expenses.
- View all recorded expenses.
- Calculate total spending.
- Identify the largest expense.
- Filter expenses by category.
- Save expense records in JSON format.
- Load previously saved expenses.
- Validate expense amounts and dates.

 3. Technologies Used

- Python 3
- JSON
- Visual Studio Code
- Git and GitHub

4. Project Structure

```text
personal-expense-tracker/
│
├── main.py
├── expenses.py
├── README.md
│
├── data/
│   └── expenses.json
│
└── tests/
    └── test_expenses.py
```

 5. How to Run the Application

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

5. Follow the application menu.

6. Running Automated Tests

To execute the automated tests, run:

```bash
python -m unittest discover -s tests -v
```

 7. Sample Expense Records

| Amount | Category | Description |
|---:|---|---|
| KSh 500 | Food | Lunch |
| KSh 200 | Transport | Bus fare |
| KSh 1,500 | Shopping | Clothes |

**Total spending: KSh 2,200**

8. Learning Outcomes

Through this project, I practised:

- Python functions.
- Lists and dictionaries.
- Conditional statements and loops.
- Exception handling.
- File handling.
- JSON data storage.
- Date validation.
- Automated testing using unittest.

 9. Developer

Innocent Kelvin

Nexora – Personal Expense Tracker