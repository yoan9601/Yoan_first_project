# Bill & Tip Calculator
# Simple console app to split a restaurant bill with tip
# Author: yoan9601

print("=" * 40)
print("   Welcome to the Tip Calculator!   ")
print("=" * 40)

# Input from user
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? (10, 12, 15, etc.) "))
people = int(input("How many people to split the bill? "))

# Validation (prevent division by zero)
if people == 0:
    print("Error: Number of people cannot be zero!")
else:
    # Calculations
    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    amount_per_person = total_bill / people

    # Round to 2 decimal places for money
    final_amount = round(amount_per_person, 2)

    # Nice formatted output
    print("\n" + "—" * 40)
    print(f"Each person should pay: ${final_amount:.2f}")
    print(f"Total bill with tip:    ${total_bill:.2f}")
    print(f"   • Original bill:     ${bill:.2f}")
    print(f"   • Tip amount ({tip_percent}%):      ${tip_amount:.2f}")
    print("—" * 40)
    print("Thank you! Have a great day! 💸")
