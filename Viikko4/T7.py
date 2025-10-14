print("Program startring.")
print()
print("Check multiplicative persistence.")
n = input("Insert an integer: ")
steps = 0

while len(n) > 1:
    digits = [int(d) for d in n]
    result = 1
    print(" * ".join(n), end=" = ")
    for d in digits:
        result *= d
    print(result)
    n = str(result)
    steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s).")
print()
print("Program ending.")
