print("Program starting.")
print("Estimate how many minutes you spent programming...\n")

t1 = int(input("A1_T1: "))
t2 = int(input("A2_T2: "))
t3 = int(input("A3_T3: "))
t4 = int(input("A4_T4: "))
t5 = int(input("A5_T5: "))
t6 = int(input("A6_T6: "))
t7 = int(input("A7_T7: "))

total = t1 + t2 + t3 + t4 + t5 + t6 + t7
ka = total / 7 
#ka=keskiarvo
rounded_ka = round(ka)

print(f"\nIn total you spent {total} minutes on programming.")
print(f"Average per task was {ka:.2f} min and same rounded to the nearest integer {rounded_ka} min.")

print("\nprogram ending.")