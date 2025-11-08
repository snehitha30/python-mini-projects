# rock_paper_scissors.py
import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def main():
    print("=== Rock, Paper, Scissors Game ===")
    print("Type 'rock', 'paper', or 'scissors'. Type 'q' to quit.")

    user_score = 0
    computer_score = 0
    ties = 0

    while True:
        user_choice = input("\nYour choice: ").strip().lower()

        if user_choice in ['q', 'quit', 'exit']:
            print("\nThanks for playing!")
            break

        if user_choice not in CHOICES:
            print("Invalid choice! Please type 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            print("🎉 You win this round!")
            user_score += 1
        elif result == "lose":
            print("😢 You lose this round!")
            computer_score += 1
        else:
            print("😐 It's a tie!")
            ties += 1

        print(f"\nScores → You: {user_score} | Computer: {computer_score} | Ties: {ties}")

    print(f"\nFinal Score → You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    print("Bye!")

if __name__ == "__main__":
    main()
