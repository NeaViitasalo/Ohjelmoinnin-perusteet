WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()  # Clear list just in case
    try:
        with open(PFilename, "r") as f:
            next(f)
            for line in f:
                line = line.rstrip("\n")
                if line == "":
                    continue
                PRows.append(line)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    WeekdayTimestampAmount = [0] * len(WEEKDAYS)
    
    for row in PRows:
        for j, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[j] += 1

    # Prepare results strings
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")

    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ").strip()
    
    readFile(filename, rows)

    analyseTimestamps(rows, results)

    displayResults(results)
    
    rows.clear()
    results.clear()

    print("Program ending.")

main()