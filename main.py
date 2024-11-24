import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose from the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        user_choice_input = input("\nEnter the number of your choice (1, 2, or 3): ")

        if user_choice_input == '1':
            user_choice = 'rock'
        elif user_choice_input == '2':
            user_choice = 'paper'
        elif user_choice_input == '3':
            user_choice = 'scissors'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        # Display the choices and the result
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round.")
            computer_score += 1

        # Display the current score
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    print("Goodbye!")


if __name__ == "__main__":
    play_game()