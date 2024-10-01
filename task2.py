import random

# Function to determine the winner
def find_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main program loop
def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Play")
        print("2. Exit")

        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            user_choice = input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): ")
            if user_choice=='1':
                user_choice='rock'
            elif user_choice=='2':
                user_choice='paper'
            elif user_choice=='3':
                user_choice='scissors'

            if user_choice not in choices:
                print("Invalid input. Please choose (1 for rock, 2 for paper, 3 for scissors).")
                continue

            computers_choice = random.choice(choices)
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computers_choice}")
            

            result = find_winner(user_choice, computers_choice)
            print(result)
        elif choice == '2':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    play_game()
