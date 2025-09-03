import random

def play_game():
    user_score, comp_score = 0, 0

    while True:
        print("\n=== Rock-Paper-Scissors ===")
        user = input("Choose Rock, Paper, or Scissors: ").lower()
        if user not in ["rock", "paper", "scissors"]:
            print("⚠ Invalid choice! Try again.")
            continue

        comp = random.choice(["rock", "paper", "scissors"])
        print(f"You chose: {user.capitalize()} | Computer chose: {comp.capitalize()}")

        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "scissors" and comp == "paper") or \
             (user == "paper" and comp == "rock"):
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            comp_score += 1

        print(f"Score → You: {user_score} | Computer: {comp_score}")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("\nFinal Score → You:", user_score, "| Computer:", comp_score)
            print("Thanks for playing 🎉")
            break

play_game()
