import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # deck = FrenchDeck()
    # print(len(deck))
    # print(deck[0])
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    print(beer_card.rank, beer_card.suit)
    print(Card('Q', 'hearts'))
