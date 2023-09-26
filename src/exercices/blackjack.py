import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
TARGET_SCORE = 21
DEALER_MIN_SCORE = 17


def test():
    while True:
        player = []
        dealer = []

        # initial round
        for _ in range(0, 2):
            add_card(player)
        add_card(dealer)

        # next player rounds
        while sum(player) < TARGET_SCORE:
            show_cards(player, dealer)
            next_round = input(
                "Type 'y' to get another card, type 'n' to pass "
            ).lower()
            if next_round == "y":
                add_card(player)
            else:
                break

        # next dealer rounds
        while sum(player) < TARGET_SCORE and (
            sum(dealer) < DEALER_MIN_SCORE or sum(dealer) < sum(player)
        ):
            add_card(dealer)

        # check & show results
        show_cards(player, dealer)
        check_result(player, dealer)

        # play again?
        again = input("Do you want to play a game of Blackjack? (y/n) ").lower()
        if again != "y":
            break


def show_cards(player, dealer):
    print(f"Your cards: {player} -> Score: {sum(player)}")
    print(f"Computer cards: {dealer} -> Score: {sum(dealer)}")


def add_card(hand: list) -> None:
    # add card to hand
    hand.append(random.choice(CARDS))
    # Replace 11 to 1 if score > 21
    if sum(hand) > TARGET_SCORE and 11 in hand:
        # CAREFUL! this creates a new list 'hand' inside function,
        # but does not update the parameter 'hand':
        # hand = [1 if card == 11 else card for card in hand]
        hand[hand.index(11)] = 1


def check_result(player: list, dealer: list):
    score_player, score_dealer = sum(player), sum(dealer)
    if score_player > TARGET_SCORE:
        print("You lose 😔")
    elif score_dealer > TARGET_SCORE:
        print("You win 😀")
    elif score_player == score_dealer:
        print("Draw 🥸")
    elif score_player > score_dealer:
        print("You win 😀")
    else:
        print("You lose 😔")
