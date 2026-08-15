import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("❌ Could not load expense data.")
        return []


def save_expenses(expenses):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except OSError as error:
        print(f"❌ Could not save expenses: {error}")


def add_expense(expenses):
    title = input("Expense name: ").strip()
    category = input("Category: ").strip()

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return

    except ValueError:
        print("❌ Enter a valid amount.")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses recorded.")
        return

    print("\n📋 EXPENSES")
    print("=" * 45)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n💰 TOTAL SPENDING")
    print("=" * 30)
    print(f"Total: ₹{total:.2f}")


def category_summary(expenses):
    if not expenses:
        print("📭 No expenses recorded.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n📊 CATEGORY SUMMARY")
    print("=" * 35)

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("❌ Invalid expense number.")
            return

        removed = expenses.pop(choice - 1)
        save_expenses(expenses)

        print(f"🗑️ Deleted: {removed['title']}")

    except ValueError:
        print("❌ Enter a valid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n╔══════════════════════════════╗")
        print("║       💰 EXPENSE TRACKER     ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Add Expense              ║")
        print("║ 2. View Expenses            ║")
        print("║ 3. Total Spending           ║")
        print("║ 4. Category Summary         ║")
        print("║ 5. Delete Expense            ║")
        print("║ 6. Exit                     ║")
        print("╚══════════════════════════════╝")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spending(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("👋 Expense Tracker closed.")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
