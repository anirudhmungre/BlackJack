from objects.card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self._cards = self.build()
    
    def build(self) -> list():
        cards = []
        suits = ['S', 'C', 'D', 'H']
        cards = [ Card(s, v) for s in suits for v in range(1, 14) ]
        return cards
    
    def show_cards(self) -> None:
        for x in self._cards:
            print(x)

    def shuffle(self) -> None:
        shuffle(self._cards)
