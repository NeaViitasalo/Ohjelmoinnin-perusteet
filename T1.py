print("Program starting.")
print("Collect positive integers.")
numbers = []

while True:
    user_input = int(input("Insert positive integer(negative stops): "))

    if user_input < 0:
        break

    numbers.append(user_input)

print("Stopped collecting positive integers.")

# Display results
if len(numbers) == 0:
    print("No integers to display.")
else:
    print(f"Displaying {len(numbers)} integers:")
    for index, value in enumerate(numbers):
        ordinal = index + 1
        print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")

print("Program ending.")