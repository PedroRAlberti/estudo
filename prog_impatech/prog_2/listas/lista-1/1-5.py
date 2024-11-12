# o problema inicial era que deveriam estar sendo embaralhadas a instancia de cartas do baralho
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

#um print antes e depois de embaralhar
myDeck = FrenchDeck()
print(myDeck[1])  
random.shuffle(myDeck._cards)
print(myDeck[1])