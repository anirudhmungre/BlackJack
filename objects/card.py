class Card:
    def __init__(self, suit: str, value: int):
        self._suit = suit
        self._value = value
    
    def __str__(self):
        name_val = {
            1: 'A',
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        val = self.value
        if self._value >= 10 or self.value == 1:
            val = name_val[self._value]
        
        return f"""
 ┌─────────┐
 │{val}        │
 │         │
 │         │
 │    {self.suit}    │
 │         │
 │         │
 │        {val}│                         
 └─────────┘"""
        # return f'{val}{self.suit}'

    @property
    def value(self) -> int:
        if self._value > 10:
            return 10
        return self._value
    
    @property
    def suit(self) -> str:
        return self._suit
