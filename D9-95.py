from auction_logo import logo


def clrscr():
    print ("\n" * 100)


def winner(bidders):
    bid_winner = ''
    bid_amount = 0
    for key in bidders:
        if bidders[key] > bid_amount:
            bid_amount = bidders[key]
            bid_winner = key
    print(f'{bid_winner} is the winner with bid ${bid_amount}.')


print(logo)
print('Welcome to the secret auction program!')
bidders = {}
more_bidders = 'yes'

while more_bidders == 'yes':
    bidder = input('What is your name?\n')
    bid = float(input('What is your bid?\n$'))
    bidders[bidder] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    clrscr()

winner(bidders)





