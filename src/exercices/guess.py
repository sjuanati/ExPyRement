import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def test():
    print("I'm thinking on a number between 1 and 100.")
    diff = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    max_turns = EASY_LEVEL_TURNS if diff == "easy" else HARD_LEVEL_TURNS
    random_number = random.randint(1, 100)

    while max_turns > 0:
        print(f"You have {max_turns} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        if did_guess(guess_number, random_number):
            return
        max_turns -=1
    
    print("You lose 🥹")

def did_guess(guess_number, random_number):
    if guess_number < random_number:
        print("Too low")
        return False
    elif guess_number > random_number:
        print("Too high")
        return False
    else:
        print("You guessed it 😀")
        return True
