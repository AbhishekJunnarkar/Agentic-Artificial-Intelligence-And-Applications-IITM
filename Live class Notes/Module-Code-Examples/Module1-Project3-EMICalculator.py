prompt1 = 'Any python code you provide should be formatted such that it can be easily run in jupyter notebook'
prompt2 = 'Each function and logical block of code should be a separate block of code that i can copy paste'
prompt3 = 'Also ensure that there is plenty of code comments'
prompt4 = 'Help me build a monthly installment (EMI) calculator app. the inputs would be the loan amount, loan tenure in months, and interest rate.  Make it a text interface that i can run easily in jupyter notebook.'

#!/usr/bin/env python3
"""
=============================================
📟  EMI Calculator - Text Interface App
---------------------------------------------
Author : Your Name
Usage  : python emi_calculator.py
Purpose: Calculate Monthly Installments (EMI),
         Total Payment, and Total Interest
=============================================
"""

# -------------------------------
# 1️⃣ Core EMI Calculation Function
# -------------------------------

def calculate_emi(principal: float, tenure_months: int, annual_interest_rate: float):
    """
    Calculate EMI, total payment, and total interest.

    Formula:
      EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
    Where:
      P = principal (loan amount)
      r = monthly interest rate = (annual_interest_rate / 12 / 100)
      n = tenure in months
    """
    if principal <= 0 or tenure_months <= 0:
        raise ValueError("Principal and tenure must be greater than 0.")

    monthly_rate = (annual_interest_rate / 100.0) / 12.0

    if monthly_rate == 0:  # Handle zero-interest loans
        emi = principal / tenure_months
    else:
        factor = (1 + monthly_rate) ** tenure_months
        emi = principal * monthly_rate * factor / (factor - 1)

    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)


# -------------------------------
# 2️⃣ Amortization Schedule Function (Optional)
# -------------------------------

def amortization_schedule(principal: float, tenure_months: int, annual_interest_rate: float):
    """
    Generate a month-by-month loan amortization schedule.
    Each row shows: EMI, Interest, Principal, Balance.
    """
    monthly_rate = (annual_interest_rate / 100.0) / 12.0
    emi, _, _ = calculate_emi(principal, tenure_months, annual_interest_rate)

    balance = principal
    schedule = []

    for month in range(1, tenure_months + 1):
        interest_component = round(balance * monthly_rate, 2) if monthly_rate > 0 else 0.0
        principal_component = round(emi - interest_component, 2)

        # Adjust for rounding errors in the last month
        if month == tenure_months:
            principal_component = round(balance, 2)
            emi_effective = round(principal_component + interest_component, 2)
        else:
            emi_effective = emi

        balance = round(balance - principal_component, 2)
        balance = max(balance, 0.0)

        schedule.append({
            "Month": month,
            "EMI": emi_effective,
            "Interest": interest_component,
            "Principal": principal_component,
            "Balance": balance
        })

    return schedule


# -------------------------------
# 3️⃣ Helper Function (Formatting)
# -------------------------------

def fmt_money(x, symbol="₹"):
    """Format a number as currency string."""
    return f"{symbol}{x:,.2f}"


# -------------------------------
# 4️⃣ Text-Based Interface
# -------------------------------

def run_emi_calculator():
    """Run the EMI calculator interactively from the terminal."""
    print("📟 Welcome to the EMI Calculator\n")

    try:
        principal = float(input("Enter loan amount (e.g., 500000): ").strip())
        tenure_months = int(input("Enter loan tenure in months (e.g., 60): ").strip())
        annual_rate = float(input("Enter annual interest rate in % (e.g., 9.5): ").strip())

        if principal <= 0 or tenure_months <= 0:
            print("\n❌ Loan amount and tenure must be greater than 0.")
            return

    except ValueError:
        print("\n⚠️ Invalid input. Please enter numeric values only.")
        return

    # Compute results
    emi, total_payment, total_interest = calculate_emi(principal, tenure_months, annual_rate)

    # Display results
    print("\n📊 EMI Calculation Results")
    print("-" * 45)
    print(f"Loan Amount (Principal): {fmt_money(principal)}")
    print(f"Tenure (Months):        {tenure_months}")
    print(f"Interest Rate (Annual): {annual_rate}%")
    print("-" * 45)
    print(f"Monthly EMI:            {fmt_money(emi)}")
    print(f"Total Payment:          {fmt_money(total_payment)}")
    print(f"Total Interest:         {fmt_money(total_interest)}")
    print("-" * 45)

    # Ask user if they want to view schedule
    choice = input("Show first 12 months of amortization schedule? (y/n): ").strip().lower()
    if choice == "y":
        schedule = amortization_schedule(principal, tenure_months, annual_rate)
        print("\n📅 Amortization Schedule (First 12 Months)")
        print("-" * 65)
        print(f"{'Month':>5} | {'EMI':>10} | {'Interest':>10} | {'Principal':>10} | {'Balance':>12}")
        print("-" * 65)

        for row in schedule[:12]:
            print(f"{row['Month']:>5} | {fmt_money(row['EMI']):>10} | {fmt_money(row['Interest']):>10} | "
                  f"{fmt_money(row['Principal']):>10} | {fmt_money(row['Balance']):>12}")

        if len(schedule) > 12:
            print("... (schedule continues)")


# -------------------------------
# 5️⃣ Entry Point
# -------------------------------

if __name__ == "__main__":
    run_emi_calculator()
