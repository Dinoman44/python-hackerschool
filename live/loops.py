number = int(input("Enter a number (0 to quit): "))

total = 0

while number != 0:
    total += number
    number = int(input("Enter a number (0 to quit): "))

print("Total sum is:", total)