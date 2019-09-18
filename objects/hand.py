from objects.deck import Deck

class Hand:
    def __init__(self) -> None:
        self._cards = list()
    
    def __str__(self) -> str:
        horizontal_cards = ''
        split_up = [ f'{c}'.split('\n') for c in self._cards ]
        for i in range(0, len(split_up[0])):
            for j in range(0, len(split_up)):
                horizontal_cards += f'{split_up[j][i]} '
            horizontal_cards += '\n'
        return horizontal_cards
    
    @property
    def first_card(self) -> str:
        return self._cards[0]
    
    @property
    def cards(self) -> str:
        return f'({self.value}) {self}'
    
    @property
    def value(self) -> int:
        return sum([c.value for c in self._cards])
    
    def hit(self, deck: Deck) -> None:
        self._cards.append(deck.deal_card())
    