python
#!/usr/bin/python3
# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # New line after each row
    row += 1