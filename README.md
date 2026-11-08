# Expense Tracker

A simple command-line app to track income and expenses. Data is saved in a
JSON file, so it is still there the next time you run the program.

## Features

- Add income and expenses (amount, category, description, today's date)
- View all transactions with item numbers
- Monthly summary: total income, total expense and balance
- Total spending by category
- Delete a transaction by its number
- Input checks: amounts must be positive numbers, categories cannot be empty

## Requirements

- Python 3.8 or newer
- No extra packages needed (uses only the standard library)

## How to run

```
python expense_tracker.py
```

## Menu

```
1. Add income   2. Add expense   3. View all
4. Monthly summary   5. Total by category
6. Delete item   7. Quit
```

## Example

```
Choose: 2
Amount: 250
Category (food, travel, bills, salary...): food
Description: lunch
Expense added.

Choose: 3
1. 2026-11-08 | expense | food | 250.00 | lunch

Choose: 4
Month (YYYY-MM): 2026-11
Total income : 50000.00
Total expense: 250.00
Balance      : 49750.00
```

## How it works

- `Transaction` class: stores one entry (amount, category, description, date, kind)
- Each entry is saved as a dictionary in `transactions.json`
- The month is read from the date text (`YYYY-MM-DD`), so nothing is stored twice
- Totals and balance are calculated each time and are not stored

## What I learned

- Classes and objects (`__init__`, `__str__`, a `to_dict` method)
- Reading and writing JSON files
- Input validation with `try / except`
- Splitting a program into small functions

## Future improvements

- Edit an existing transaction
- Export a monthly report to CSV
- Split the code into modules (`models.py`, `storage.py`, `main.py`)
