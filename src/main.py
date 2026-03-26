import json
import os

DATA_FILE = "transactions.json"

transactions = []  # each item: {"type": "expense"|"income", "amount": float, "category": str}


def show_menu():
    print("\n=== Finance Tracker ===")
    print("1) Add expense")
    print("2) Add income")
    print("3) View summary")
    print("4) List transactions")
    print("5) Exit")


def get_amount():
    while True:
        raw = input("Amount (e.g. 25.50): ").strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number like 25.50")


def add_expense():
    print("\n--- Add Expense ---")
    amount = get_amount()
    category = input("Category: ").strip()

    transactions.append({
        "type": "expense",
        "amount": amount,
        "category": category
    })

    save_transactions()

    print("Expense saved.")

def add_income():
    print("\n--- Add Income ---")
    amount = get_amount()
    category = input("Source (e.g. salary, gift): ").strip() or "unspecified"
    transactions.append({"type": "income", "amount": amount, "category": category})
    print(f"Saved: +{amount:.2f} [{category}]")


def view_summary():
    total_expenses = 0
    total_income = 0
    category_totals = {}

    for t in transactions:
        if t["type"] == "expense":
            total_expenses += t["amount"]

            category = t["category"]
            category_totals[category] = category_totals.get(category, 0) + t["amount"]

        if t["type"] == "income":
            total_income += t["amount"]

    balance = total_income - total_expenses

    print("\n--- Summary ---")
    print(f"Total income: {total_income}")
    print(f"Total expenses: {total_expenses}")
    print(f"Balance: {balance}")

    print("\nExpenses by category:")
    for category, amount in category_totals.items():
        print(f"{category}: {amount}")


def main():
    load_transactions()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            add_income()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def load_transactions():
    global transactions

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            transactions = json.load(f)

def save_transactions():
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f)


def list_transactions():
    print("\n--- All Transactions ---")

    if not transactions:
        print("No transactions found.")
        return

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. {transaction['type'].upper()} | "
            f"Amount: {transaction['amount']} | "
            f"Category: {transaction['category']}"
        )

def main():
    load_transactions()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            add_income()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            list_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()