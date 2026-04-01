import random
import numpy as np

class Deck:
    """ Full deck of shuffled cards """
    
    def __init__(self):
        """ Creates a full deck of cards and shuffles it """
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = [s+r for r in ranks for s in suits]
        random.shuffle(self.deck)

    def hand(self, n=5):
        '''Deal n cards, removing them from the deck)'''
        deal = self.deck[:n]
        del self.deck[:n]
        return deal

if __name__ == ' __main__':
    deck = Deck()
    print(len(deck.deck))
    print(deck.hand())
    print(len(deck.deck))

        