print("Program starting.")

raw_input = input("Insert comma separated integers: ")

parts = raw_input.split(",")

valid_numbers = []

for p in parts:
    p = p.strip()
    try:
        number = int(p)
        valid_numbers.append(number)
    except ValueError:
        print(f"Invalid value detected: '{p}'")

if len(valid_numbers) == 0:
    print("No valid integers to analyze.")
else:

    total = sum(valid_numbers)

    if total % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    print(f"There are {len(valid_numbers)} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")

print("Program ending.")