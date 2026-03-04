import json
import os

DATA_FILE = "transactions.json"

transactions = []  # each item: {"type": "expense"|"income", "amount": float, "category": str}


def show_menu():
    print("\n=== Finance Tracker ===")
    print("1) Add expense")
    print("2) Add income")
    print("3) View summary")
    print("4) Exit")


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
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    balance = total_income - total_expenses

    print("\n--- Summary ---")
    print(f"Transactions: {len(transactions)}")
    print(f"Total income:  +{total_income:.2f}")
    print(f"Total expenses: -{total_expenses:.2f}")
    print(f"Balance:       {balance:.2f}")


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


if __name__ == "__main__":
    main()