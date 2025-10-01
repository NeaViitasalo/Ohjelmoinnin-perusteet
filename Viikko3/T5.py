print("Program strating. \n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to celsius")
print("0 - Exit")

choice = input("Your choice: ")
if choice == "1":
    celsius = float(input("Insert the amount of Celcius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius:.1f} ℃ equals to {fahrenheit:.1f} ℉\n")
elif choice == "2":
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8    
    print(f"{fahrenheit:.1f} ℉ equals to {celsius:.1f} ℃\n")
elif choice == "0":
    print("Exiting...")
else: print("\nProgram ending.")
