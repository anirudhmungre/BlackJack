from constants import NUM_DECKS
from objects.deck import Deck
from objects.card import Card

def init_cards() -> Deck:
    deck = Deck(NUM_DECKS)
    print('Deck Initialized')
    shuffle_deck(deck)
    return deck

def shuffle_deck(deck: Deck) -> None:
    deck.shuffle()
    print('Deck Shuffled')

def hit(deck: Deck) -> Card:
    return deck.deal_card()

def init_hands(deck: Deck) -> list():
    player_hand = list()
    dealer_hand = list()
    player_hand.append(hit(deck))
    dealer_hand.append(hit(deck))
    player_hand.append(hit(deck))
    dealer_hand.append(hit(deck))
    print('Hands Initialized')
    return player_hand, dealer_hand

def play(deck: Deck) -> None:
    while deck.num_cards > deck.num_cards / 2:
        player_hand, dealer_hand = init_hands(deck)
        print(f'Dealer Showing: {dealer_hand[0]}')
        print(f'Player Has: {player_hand[0]} {player_hand[1]}')

def main():
    deck = init_cards()
    play(deck)

if __name__ == '__main__':
    main()