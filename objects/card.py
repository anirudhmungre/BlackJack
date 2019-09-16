class Card:
    def __init__(self, suit: str, value: int):
        self._suit = suit
        self._value = value
    
    def __str__(self):
        return f'{self._value}{self._suit}'

    @property
    def value(self) -> int:
        return self._value
    
    @property
    def suit(self) -> str:
        return self._suit
