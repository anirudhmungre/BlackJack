from objects.deck import Deck

class Hand:
    def __init__(self) -> None:
        self._cards = list()
    
    def __str__(self) -> str:
        end_card = ['───────┐', 
                    '       │', 
                    '       │',
                    '       │',
                    '       │',
                    '       │',
                    '       │',
                    '       │',
                    '───────┘']
        horizontal_cards = '\n'
        split_up = [ f'{c}'.split('\n') for c in self._cards ]
        for i in range(0, len(split_up[0])):
            for j in range(0, len(split_up)):
                horizontal_cards += f'{split_up[j][i]}'
            if end_card[i]:
                horizontal_cards += f'{end_card[i]}\n'
        return horizontal_cards
    
    @property
    def first_card(self) -> str:
        name_val = {
            1: 'A',
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        val = self._cards[0].value
        if self._cards[0]._value >= 10 or self.value == 1:
            val = name_val[self._cards[0]._value]
        return f"""
 ┌─────────┐
 │{val}        │
 │{self._cards[0].suit}        │
 │         │
 │         │
 │         │
 │         │
 │         │                         
 └─────────┘"""
    
    @property
    def cards(self) -> str:
        if 'A' in f'{self}' and self.value < 21 and sum([c.value for c in self._cards]) + 10 < 21:
            return f'({self.value - 10}/{self.value}) {self}'
        return f'({self.value}) {self}'
    
    @property
    def value(self) -> int:
        small_value = sum([c.value for c in self._cards])
        if 'A' in f'{self}' and small_value + 10 <= 21:
            return small_value + 10
        return small_value
    
    @property
    def num_cards(self) -> int:
        return len(self._cards)
    
    def hit(self, deck: Deck) -> None:
        self._cards.append(deck.deal_card())
    