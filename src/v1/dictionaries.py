def test():
    # create a blind auction program
    bids = []
    bidders = True
    while bidders:
        name = input("What is your name? ")
        bid = int(input("What is your bid? "))
        bids.append({"name": name, "bid": bid})
        add_bidders = input("Are there any other bidders? yes/no ").lower()
        bidders = True if add_bidders == "yes" else False
    # option 1
    max_bid = 0
    for elem in bids:
        print("elem", elem)
        if elem["bid"] > max_bid:
            max_bid = elem["bid"]
    for elem in bids:
        if elem["bid"] == max_bid:
            print(f'The winner is {elem["name"]} with a bid of ${elem["bid"]}')
    # option 2 ;)
    winner = max(bids, key=lambda x: x["bid"])
    print(f'The winner is {winner["name"]} with a bid of ${winner["bid"]}')
