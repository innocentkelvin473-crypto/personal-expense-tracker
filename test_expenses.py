# ==========================================
# NEXORA - PERSONAL EXPENSE TRACKER
# Automated Tests
# Developer: Innocent Kelvin
# ==========================================

# STEP 1: Import testing tools

import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

# STEP 2: Import functions from expenses.py

from expenses import (
    add_expense,
    calculate_total,
    largest_expense,
    filter_by_category
)


# STEP 3: Create our test class

class TestExpenseTracker(unittest.TestCase):

    # STEP 4: Prepare sample expense records

    def setUp(self):

        self.expenses = [
            {
                "amount": 500.0,
                "category": "Food",
                "description": "Lunch",
                "date": "2026-11-08"
            },
            {
                "amount": 200.0,
                "category": "Transport",
                "description": "Bus fare",
                "date": "2026-11-08"
            },
            {
                "amount": 1500.0,
                "category": "Shopping",
                "description": "Clothes",
                "date": "2026-11-08"
            }
        ]

    # TEST 1: Calculate total spending

    def test_calculate_total(self):

        with redirect_stdout(StringIO()):
            result = calculate_total(self.expenses)

        self.assertEqual(result, 2200.0)

    # TEST 2: Calculate total when no expenses exist

    def test_empty_expenses_total(self):

        with redirect_stdout(StringIO()):
            result = calculate_total([])

        self.assertEqual(result, 0)

    # TEST 3: Identify the largest expense

    def test_largest_expense(self):

        with redirect_stdout(StringIO()):
            result = largest_expense(self.expenses)

        self.assertEqual(result["amount"], 1500.0)
        self.assertEqual(result["category"], "Shopping")

    # TEST 4: Handle an empty expense list

    def test_largest_expense_empty(self):

        with redirect_stdout(StringIO()):
            result = largest_expense([])

        self.assertIsNone(result)

    # TEST 5: Filter expenses by category

    def test_filter_by_category(self):

        with redirect_stdout(StringIO()):
            result = filter_by_category(
                self.expenses, "Food"
            )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 500.0)

    # TEST 6: Check category filtering without case sensitivity

    def test_filter_category_case_insensitive(self):

        with redirect_stdout(StringIO()):
            result = filter_by_category(
                self.expenses, "food"
            )

        self.assertEqual(len(result), 1)

    # TEST 7: Add a new expense successfully

    @patch("builtins.input", side_effect=[
        "500",
        "Food",
        "Lunch",
        "2026-11-08"
    ])

    def test_add_expense(self, mock_input):

        new_expenses = []

        with redirect_stdout(StringIO()):
            add_expense(new_expenses)

        self.assertEqual(len(new_expenses), 1)
        self.assertEqual(new_expenses[0]["amount"], 500.0)
        self.assertEqual(new_expenses[0]["category"], "Food")


# STEP 5: Run all automated tests

if __name__ == "__main__":
    unittest.main()
    
