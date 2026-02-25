def show_menu():
    print("\n=== Finance Tracker ===")
    print("1) Add expense")
    print("2) Add income")
    print("3) View summary")
    print("4) Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Expense feature coming soon.")
        elif choice == "2":
            print("Income feature coming soon.")
        elif choice == "3":
            print("Summary feature coming soon.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()