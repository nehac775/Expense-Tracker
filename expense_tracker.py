import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        if not os.path.exists(filename):
            df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
            df.to_csv(filename, index=False)

    def add_expense(self, category, description, amount):
        date = datetime.now().strftime("%Y-%m-%d")
        new_expense = pd.DataFrame([[date, category, description, amount]],
                                   columns=["Date", "Category", "Description", "Amount"])
        new_expense.to_csv(self.filename, mode="a", header=False, index=False)
        print(f"✅ Added: {description} (${amount}) in {category}")

    def view_expenses(self):
        df = pd.read_csv(self.filename)
        if df.empty:
            print("No expenses recorded yet.")
        else:
            print(df)

    def summary_by_category(self):
        df = pd.read_csv(self.filename)
        if df.empty:
            print("No expenses recorded yet.")
            return
        summary = df.groupby("Category")["Amount"].sum()
        print("\n📊 Expenses by Category:")
        print(summary)
        summary.plot(kind="bar", title="Expenses by Category")
        plt.show()

    def monthly_report(self):
        df = pd.read_csv(self.filename)
        if df.empty:
            print("No expenses recorded yet.")
            return
        df["Date"] = pd.to_datetime(df["Date"])
        df["Month"] = df["Date"].dt.to_period("M")
        monthly = df.groupby("Month")["Amount"].sum()
        print("\n📅 Monthly Report:")
        print(monthly)
        monthly.plot(kind="line", marker="o", title="Monthly Expenses")
        plt.show()


# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()

    # Add some example expenses
    tracker.add_expense("Food", "Pizza", 12.50)
    tracker.add_expense("Transport", "Uber ride", 8.20)
    tracker.add_expense("Entertainment", "Movie ticket", 15.00)

    # View all expenses
    tracker.view_expenses()

    # Show category summary
    tracker.summary_by_category()

    # Show monthly report
    tracker.monthly_report()
