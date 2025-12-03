import random
random.seed(1234)


ASCII_ART = {
    1: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    2: """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""",
    3: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
}

CHOICES = {1: "rock", 2: "paper", 3: "scissors"}

def determine_winner(player, bot):
    if player == bot:
        return "draw"
    elif (player == 1 and bot == 3) or (player == 2 and bot == 1) or (player == 3 and bot == 2):
        return "player"
    else:
        return "bot"

print("Program starting.")
print("Welcome to the rock-paper-scissors game!")
player_name = input("Insert player name: ")
print(f"Welcome {player_name}!")
print("Your opponent is RPS-3PO.")
print("Game starts...\n")

scores = {
    player_name: {"wins": 0, "losses": 0, "draws": 0},
    "RPS-3PO": {"wins": 0, "losses": 0, "draws": 0}
}

while True:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    
    try:
        player_choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 0 to 3.\n")
        continue

    if player_choice == 0:
        break
    if player_choice not in [1, 2, 3]:
        print("Invalid choice. Try again.\n")
        continue

    print("Rock! Paper! Scissors! Shoot!\n")

    bot_choice = random.randint(1, 3)

    print("#" * 25)
    print(f"{player_name} chose {CHOICES[player_choice]}.\n")
    print(ASCII_ART[player_choice])
    print("#" * 25)
    print(f"RPS-3PO chose {CHOICES[bot_choice]}.\n")
    print(ASCII_ART[bot_choice])
    print("#" * 25 + "\n")

    result = determine_winner(player_choice, bot_choice)
    if result == "draw":
        print(f"Draw! Both players chose {CHOICES[player_choice]}.\n")
        scores[player_name]["draws"] += 1
        scores["RPS-3PO"]["draws"] += 1
    elif result == "player":
        print(f"{player_name} {CHOICES[player_choice]} beats RPS-3PO {CHOICES[bot_choice]}.\n")
        scores[player_name]["wins"] += 1
        scores["RPS-3PO"]["losses"] += 1
    else:
        print(f"RPS-3PO {CHOICES[bot_choice]} beats {player_name} {CHOICES[player_choice]}.\n")
        scores["RPS-3PO"]["wins"] += 1
        scores[player_name]["losses"] += 1

print("Results:")
print(f"{player_name} - wins ({scores[player_name]['wins']}), losses ({scores[player_name]['losses']}), draws ({scores[player_name]['draws']})")
print(f"RPS-3PO - wins ({scores['RPS-3PO']['wins']}), losses ({scores['RPS-3PO']['losses']}), draws ({scores['RPS-3PO']['draws']})\n")
print("Program ending.")