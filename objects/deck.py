from objects.card import Card
from random import shuffle

class Deck:
    def __init__(self, num_decks: int = 1):
        self._cards = self.build(num_decks)
    
    @property
    def num_cards(self) -> int:
        return len(self._cards)
    
    @staticmethod
    def build(num_decks: int) -> list():
        cards = []
        suits = ['♠', '♣', '♦', '♥']
        cards = [ Card(s, v) for _ in range(0, num_decks) for s in suits for v in range(1, 14) ]
        return cards
    
    def show_cards(self) -> None:
        for x in self._cards:
            print(x)

    def shuffle(self) -> None:
        shuffle(self._cards)
    
    def deal_card(self) -> Card:
        return self._cards.pop()