# multiplication_table.py

# Prompt the user to enter a number (exact prompt required)
number = int(input("Enter a number to see its multiplication table:"))

# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
