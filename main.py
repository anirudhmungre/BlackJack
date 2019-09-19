from os import system, name
from msvcrt import getch
from sys import argv
from time import sleep

from objects.deck import Deck
from objects.card import Card
from objects.hand import Hand

# print(argv[0])
try:
    NUM_DECKS = int(argv[1])
except:
    NUM_DECKS = 1

def clear() -> None:
    _ = system('cls' if name == 'nt' else 'clear')

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

def cards_and_results(deck: Deck, player_hand: Hand, dealer_hand: Hand, player_turn: bool = False) -> None:
    print(f'Cards Left: {deck.num_cards}')
    if player_turn:
        print(f'Dealer Showing: {dealer_hand.first_card}')
    else:
        print(f'Dealer Showing: {dealer_hand.cards}')
    print(f'Player Has: {player_hand.cards}')
    

def player_play(deck: Deck, player_hand: Hand, dealer_hand: Hand) -> Hand:
    playing = True
    while player_hand.value < 21 and playing:
        print("What would you like to do? Hit(h) or Stand(s) ")
        action = getch()
        while action.lower() not in [b'h', b's']:
            print("Available Actions: Hit (h) or Stand(s) ")
            action = getch()
        if action.lower() == b'h':
            player_hand.hit(deck)
            clear()
            cards_and_results(deck, player_hand, dealer_hand, True)
        elif action.lower() == b's':
            playing = False
    return player_hand

def dealer_play(deck: Deck, dealer_hand: Hand, player_hand: Hand) -> Hand:
    sleep(1)
    clear()
    cards_and_results(deck, player_hand, dealer_hand)
    while dealer_hand.value < 17:
        sleep(1)
        clear()
        dealer_hand.hit(deck)
        cards_and_results(deck, player_hand, dealer_hand)
    return dealer_hand

def play_hand(deck: Deck, player_hand: Hand, dealer_hand: Hand) -> None:
    player_hand = player_play(deck, player_hand, dealer_hand)
    if player_hand.value <= 21:
        if player_hand.num_cards == 2 and player_hand.value == 21:
            clear()
            cards_and_results(deck, player_hand, dealer_hand)
            if dealer_hand.value == 21:
                print('''
        -----------
        Player push
        -----------
            ''')
            else:
                print('''
        -----------------
        Player BLACKJACK!
        -----------------
            ''')
        else:
            dealer_hand = dealer_play(deck, dealer_hand, player_hand)
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
            elif dealer_hand.value == player_hand.value:
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

def play() -> None:
    play_again = True
    while play_again:
        deck = init_cards()
        print('Shoe Changed')
        while deck.num_cards > NUM_DECKS*52 / 2 and play_again:
            player_hand, dealer_hand = init_hands(deck)
            cards_and_results(deck, player_hand, dealer_hand, True)
            play_hand(deck, player_hand, dealer_hand)
            print('Would you like to play again! (y)es or (n)o')
            option = getch()
            while option not in [b'y', b'n']:
                option = getch()
            play_again = True if option == b'y' else False
            clear()
    


def main() -> None:
    clear()
    play()

if __name__ == '__main__':
    main()