from objects.deck import Deck

class Hand:
    def __init__(self):
        self._cards = list()
    
    def __str__(self):
        return ' '.join([ f'{c}' for c in self._cards ])
    
    @property
    def first_card(self) -> str:
        return self._cards[0]
    
    @property
    def cards(self) -> str:
        return f'({self.value}) {self}'
    
    @property
    def value(self) -> int:
        return sum([c.value for c in self._cards])
    
    def hit(self, deck: Deck):
        self._cards.append(deck.deal_card())
    