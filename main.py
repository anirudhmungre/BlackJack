from constants import NUM_DECKS
from objects.deck import Deck
from objects.card import Card
from objects.hand import Hand

from time import sleep

def init_cards() -> Deck:
    deck = Deck(NUM_DECKS)
    print('Deck Initialized')
    shuffle_deck(deck)
    return deck

def shuffle_deck(deck: Deck) -> None:
    deck.shuffle()
    print('Deck Shuffled')

def init_hands(deck: Deck) -> list():
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.hit(deck)
    dealer_hand.hit(deck)
    player_hand.hit(deck)
    dealer_hand.hit(deck)
    print('Hands Initialized')
    return player_hand, dealer_hand

def player_play(deck: Deck, player_hand: Hand) -> Hand:
    playing = True
    while player_hand.value <= 21 and playing:
        action = input("What would you like to do? ")
        while action.lower() not in ['hit', 'stand']:
            action = input("Available Actions: Hit, Stand: ")
        if action.lower() == 'hit':
            player_hand.hit(deck)
            print(f'Player Has: {player_hand.cards}')
        elif action.lower() == 'stand':
            playing = False
    return player_hand

def dealer_play(deck: Deck, dealer_hand: Hand) -> Hand:
    sleep(1)
    print(f'Dealer Has: {dealer_hand.cards}')
    while dealer_hand.value < 17:
        sleep(1)
        dealer_hand.hit(deck)
        print(f'Dealer Has: {dealer_hand.cards}')
    return dealer_hand

def play_hand(deck: Deck, player_hand: Hand, dealer_hand: Hand):
    player_hand = player_play(deck, player_hand)
    if player_hand.value <= 21:
        dealer_hand = dealer_play(deck, dealer_hand)
        if dealer_hand.value > 21:
            print('''
        -----------
        Dealer Bust
        -----------
            ''')
        elif dealer_hand.value < player_hand.value:
            print('''
        -----------
        Player Wins
        -----------
            ''')
        elif dealer_hand.value > player_hand.value:
            print('''
        -----------
        Dealer Wins
        -----------
            ''')
        else:
            print('''
        -----------
        Player Push
        -----------
            ''')
    else:
        print('''
        -----------
        Player Bust
        -----------
        ''')

def play(deck: Deck) -> None:
    while deck.num_cards > deck.num_cards / 2:
        player_hand, dealer_hand = init_hands(deck)
        print(f'Dealer Showing: {dealer_hand.first_card}')
        print(f'Player Has: {player_hand.cards}')
        play_hand(deck, player_hand, dealer_hand)

def main():
    deck = init_cards()
    play(deck)

if __name__ == '__main__':
    main()