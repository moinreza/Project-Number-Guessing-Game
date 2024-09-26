import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    print("Enter 'exit' to quit the game at any time.")

    while True:
        user_input = input("Enter your guess: ")
        
        if user_input.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        
        try:
            user_guess = int(user_input)
            
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1

            if user_guess < target_number:
                print("Too low!")
            elif user_guess > target_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    number_guessing_game()

