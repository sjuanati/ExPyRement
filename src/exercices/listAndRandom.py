import random

def test():
    # assign 0 or 1 randomly to a variable
    # use if/else to print heads or tails
    result = random.randint(0,1)
    if result == 1:
        print('heads!')
    else:
        print('tails!')

    ## city list generator to pickup a winner
    pre_list = input("Enter cities separated by a comma: ").split(",")
    post_list = [item.strip() for item in pre_list] # remove spaces on left & right
     # option 1
    pos = random.randint(0, len(post_list) - 1)
    print(f"And the winner is ... {post_list[pos]}")
    # option 2
    print(f"And the winner is ... {random.choice(post_list)}")

    # Mark position in table
    # @NOTICE: board contains references to row1, row2 & row3, but is not storing them.
    #          therefore, if board is updated, so the rows are
    row1 = ["H", "H", "H"]
    row2 = ["H", "H", "H"]
    row3 = ["H", "H", "H"]
    position = input("Which tile you'd like to change? Column & row, eg: 23 :")
    row = int(position[:1]) - 1
    column = int(position[1:]) - 1
    board = [row1, row2, row3]
    board[row][column] = "X"
    print(f"{row1}\n{row2}\n{row3}\n")

    # Rock, Paper, Scissors
    user_choice = input("What do you choose? Type rock, paper or scissors \n").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f'user: {user_choice}')
    print(f'computer: {computer_choice}')
    result = ""
    if user_choice == "rock":
        if computer_choice == "scissors":
            result += "You win"
        elif computer_choice == "paper":
            result += "You lose"
        else:
            result += "Draw"
    elif user_choice == "paper":
        if computer_choice == "rock":
            result += "You win"
        elif computer_choice == "scissors":
            result += "You lose"
        else:
            result += "Draw"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            result += "You win"
        elif computer_choice == "rock":
            result += "You lose"
        else:
            result += "Draw"
    else:
        print(f'Wrong user selection: {user_choice}')
        quit()
    print(f'{result} -> user: {user_choice} vs. computer: {computer_choice}')