import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def present(self):
        return f'{self.value} of {self.suit}'
    

class Deck:

    suits = ['hearts', 'diamonds', 'clubs',' spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self):
        self.cards = []
        for s in Deck.suits:
            for v in Deck.values:
                card = Card(s, v)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        # else:
        #     return None

    def count_remaining(self):
        return len(self.cards)
    
    def get_remaining(self):
        remaining_cards = [c.present() for c in self.cards]
        return remaining_cards
    
    def __str__(self):
        return self.cards
    

first_deck = Deck()

first_deck.shuffle()
first_deck.shuffle()
first_deck.shuffle()
print(first_deck.deal())
print(first_deck.deal())
print(first_deck.count_remaining())
for c in first_deck.cards:
    print(c.present())