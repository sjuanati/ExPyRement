import random


def test():
    MAX_FAILS = 6
    fails = 0
    dictionary = ["michael", "elena", "sergi", "eufrasio", "estaquirot", "escripell"]
    # random_word = list(dictionary[random.randint(0, len(dictionary) - 1)])
    random_word = random.choice(dictionary)
    guess = ["_"] * len(random_word)

    print(random_word)
    print(guess)

    while fails < MAX_FAILS:
        # user input
        while True:
            user_input = input("Try a letter: ").lower()
            if len(user_input) == 1 and user_input.isalpha():
                break
            else:
                print("Invalid input. Please enter only one letter.")
        
        repeated = user_input in guess

        exist = False
        for i in range(0, len(random_word)):
            if user_input == random_word[i]:
                guess[i] = random_word[i]
                exist = True

        if random_word == guess:
            break

        if (not exist or repeated):
            fails += 1

        print(f'{guess} with {fails} attempts')
    
    if fails < MAX_FAILS:
        print('You won!!')
    else:
        print('You lose!')
