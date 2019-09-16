from objects.deck import Deck
from constants import NUM_DECKS

def init_cards() -> Deck:
    deck = Deck(NUM_DECKS)
    print('Deck Initialized')
    shuffle_deck(deck)
    return deck

def shuffle_deck(deck: Deck) -> None:
    deck.shuffle()
    print('Deck Shuffled')

def main():
    deck = init_cards()

if __name__ == '__main__':
    main()