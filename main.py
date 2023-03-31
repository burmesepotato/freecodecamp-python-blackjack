import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self) -> str:
    return f"{self.rank['rank']} of {self.suit}"

class Deck:
  def __init__(self):
    self.cards = []
    self.suits = ["spades", "clubs", "hearts", "diamonds"]
    self.ranks = [
        { "rank": "A", "value": 11 },
        { "rank": "2", "value": 2 },
        { "rank": "3", "value": 3 },
        { "rank": "4", "value": 4 },
        { "rank": "5", "value": 5 },
        { "rank": "6", "value": 6 },
        { "rank": "7", "value": 7 },
        { "rank": "8", "value": 8 },
        { "rank": "9", "value": 9 },
        { "rank": "10", "value": 10 },
        { "rank": "J", "value": 10 },
        { "rank": "Q", "value": 10 },
        { "rank": "K", "value": 10 },
      ]
    # cards_dealt = []
    for suit in self.suits:
      for rank in self.ranks:
          self.cards.append(Card(suit, rank))

  def shuffle_cards(self):
      if len(self.cards) > 1:
        random.shuffle(self.cards)

  # def deal_card(number, dealt = []):
  #     if number == 0: return dealt
  #     dealt.append(cards.pop())
  #     return deal_card(number - 1, dealt)

  def deal_cards(self, number):
      dealt_cards = []
      for x in range(number):
          if len(self.cards) > 0:
            dealt_cards.append(self.cards.pop())
      return dealt_cards
    
deck = Deck()
deck.shuffle_cards()

cards_dealt = deck.deal_cards(2)

print(cards_dealt[0])