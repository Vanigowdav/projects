import json
import datetime

DATA_FILE = "transactions.json"


class Transaction:
    """One income or expense entry."""

    def __init__(self, amount, category, description, date, kind):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.kind = kind

    def to_dict(self):
        """Return the transaction as a dictionary so it can be saved as JSON."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
            "kind": self.kind,
        }

    def __str__(self):
        """Return a one-line readable summary of the transaction."""
        return (f"{self.date} | {self.kind} | {self.category} | "
                f"{self.amount:.2f} | {self.description}")


def save_transactions(transactions):
    """Write all transactions to the JSON file."""
    data = []
    for t in transactions:
        data.append(t.to_dict())
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_transactions():
    """Load saved transactions from the JSON file as Transaction objects."""
    try:
        with open(DATA_FILE, "r") as f:
            raw = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    transactions = []
    for d in raw:
        transactions.append(
            Transaction(d["amount"], d["category"], d["description"],
                        d["date"], d["kind"])
        )
    return transactions


def add_transaction(transactions, kind):
    """Ask for the details, add a new transaction, and save it."""
    while True:
        text = input("Amount: ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Enter a valid number.")
            continue
        if amount > 0:
            break
        print("Amount must be above 0.")

    while True:
        category = input("Category (food, travel, bills, salary...): ").strip()
        if category:
            break
        print("Category cannot be empty.")

    description = input("Description: ").strip()
    today = datetime.date.today().isoformat()

    transactions.append(Transaction(amount, category, description, today, kind))
    save_transactions(transactions)
    print(f"{kind.capitalize()} added.")


def view_transactions(transactions):
    """Print all transactions with item numbers."""
    if not transactions:
        print("No transactions yet.")
        return
    for number, t in enumerate(transactions, start=1):
        print(f"{number}. {t}")


def monthly_summary(transactions):
    """Print total income, total expense and balance for one month."""
    month = input("Month (YYYY-MM): ").strip()
    if len(month) != 7 or month[4] != "-":
        print("Please use the format YYYY-MM, for example 2026-11.")
        return

    total_income = 0
    total_expense = 0
    count = 0
    for t in transactions:
        if t.date.startswith(month):
            count += 1
            if t.kind == "income":
                total_income += t.amount
            else:
                total_expense += t.amount

    if count == 0:
        print(f"No transactions for {month}.")
        return

    balance = total_income - total_expense
    print(f"Total income : {total_income:.2f}")
    print(f"Total expense: {total_expense:.2f}")
    print(f"Balance      : {balance:.2f}")


def total_by_category(transactions):
    """Print the total expense for each category."""
    totals = {}
    for t in transactions:
        if t.kind == "expense":
            totals[t.category] = totals.get(t.category, 0) + t.amount

    if not totals:
        print("No expenses yet.")
        return
    for category, total in totals.items():
        print(f"{category}: {total:.2f}")


def delete_transaction(transactions):
    """Delete a transaction by its item number."""
    view_transactions(transactions)
    if not transactions:
        return
    text = input("Item number to delete: ").strip()
    if not text.isdigit() or not 1 <= int(text) <= len(transactions):
        print("Invalid item number.")
        return
    removed = transactions.pop(int(text) - 1)
    save_transactions(transactions)
    print(f"Deleted: {removed}")


def main():
    transactions = load_transactions()
    while True:
        print("\n1. Add income   2. Add expense   3. View all")
        print("4. Monthly summary   5. Total by category")
        print("6. Delete item   7. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_transaction(transactions, "income")
        elif choice == "2":
            add_transaction(transactions, "expense")
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            monthly_summary(transactions)
        elif choice == "5":
            total_by_category(transactions)
        elif choice == "6":
            delete_transaction(transactions)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()