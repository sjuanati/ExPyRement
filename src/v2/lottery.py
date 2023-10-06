import random

# 4 players with 6 numbers each (from 1 to 22)
# only the player with most numbers matching winns, according to 100 ** len(numbers_matched)


def test():
    players = [
        {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
        {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
        {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
        {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
    ]
    # WRONG!! any repeated number will be removed
    # lottery_numbers = {random.randint(1, 22) for _ in range(6)}
    # CORRECT: 6 unique integers from 1 to 22
    lottery_numbers = set(random.sample(range(1, 23), k=6))

    # start assuming 1st player is the current winner
    top_player = players[0]
    winnings = 0

    print(f"lottery number: {lottery_numbers}")
    for player in players:
        numbers_matched = len(player["numbers"].intersection(lottery_numbers))
        if numbers_matched >= winnings:
            top_player = player
            winnings = numbers_matched

    # order the numbers of the winner in ascending order
    winning_numbers = set(sorted(top_player["numbers"]))
    prize = f"{100 ** winnings:,}"
    message = (
        f'player {top_player["name"]} with numbers {winning_numbers} '
        f"did {winnings} wins and was awarded ${prize}"
    )
    print(message)
