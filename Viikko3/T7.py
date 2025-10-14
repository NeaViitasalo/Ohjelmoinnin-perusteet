print("Program starting.")
print("Testing decision structures.")

Feed = input("Insert an integer: ")
Value = int(Feed)

print("Options:")
print("1 - in one multi-branched decision")
print("2- In multiple independent if-statements")
print("0 - Exit")

Feed = input("Your choice: ")
choice = int(Feed)

if(choice == 1):
    print("Using one multi-branched decision structure")
    if(Value >= 400):
        Value += 44
    elif(Value >= 200):
        Value += 22
    elif(Value >= 100):
        Value += 11
    print(f"Result is {Value}")
elif(choice == 2):
    if(Value >= 400):
        Value += 44
    if(Value >= 200):
        Value += 22
    if(Value >= 100):
        Value += 11      
    print(f"Result is {Value}")  
elif(choice == 0):
    print("Exiting...")
else:
    print("Unknown option")

print("")
print("Program ending.")
