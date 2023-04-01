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

class Hand:
  def __init__(self, is_dealer = False):
    self.cards = []
    self.value = 0
    self.is_dealer = is_dealer

  def add_card(self, card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    self.value = 0
    has_ace = False

    for card in self.cards:
      self.value += int(card.rank["value"])
      if card.rank["rank"] == "A":
        has_ace = True
    
    if has_ace and self.value > 21:
      self.value -= 10

  def get_value(self):
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    return self.get_value() == 21
  
  def display(self, show_all_dealer_cards = False):
    print(f'''=== {"Dealer's" if self.is_dealer else "Your"} hand: ===''')
    # Using enumerate returns index, card
    for key, card in enumerate(self.cards):
      # \ is used to break the long statement into multiple line
      if key == 0 and self.is_dealer \
        and not show_all_dealer_cards and not self.is_blackjack():
        print("hidden")
      else:
        print(card)

    if not self.is_dealer:
      print("Value: ", self.get_value())


class Game:
  def check_winner(self, player_hand, dealer_hand, game_over = False):
    if not game_over:
      if player_hand.get_value() > 21:
        print("You're busted. Dealer wins!")
        return True
      elif dealer_hand.get_value() > 21:
        print("Dealer's busted. You win!")
        return True
      elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
        print("Both players have blackjack. Tie!")
        return True
      elif player_hand.is_blackjack():
        print("You have blackjack. You win!")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer has blackjack. Dealer wins!")
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print("You win!")
        return True
      elif player_hand.get_value() == dealer_hand.get_value():
        print("It's a tie!")
        return True
      else:
        print("Dealer wins!")
        return True
    return False
  

  def play(self):
    game_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try: 
        games_to_play = int(input("How many games do you want to play? "))
      except Exception as error:
        print("Please enter a valid number")

    while game_number < games_to_play:
      game_number += 1

      deck = Deck()
      deck.shuffle_cards()

      player_hand = Hand()
      dealer_hand = Hand(is_dealer = True)

      for i in range(2):
        player_hand.add_card(deck.deal_cards(1))
        dealer_hand.add_card(deck.deal_cards(1))

      print()
      print("*" * 30)
      print(f"Game {game_number} of {games_to_play}")
      print("*" * 30)
      player_hand.display()
      dealer_hand.display()

      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("Please choose 'Hit' or 'Stand': ").lower()
        print()
        while choice not in ["h", "hit", "s", "stand"]:
          choice = input("Please choose 'Hit' or 'Stand': ").lower()
          print()
        if choice in ["h", "hit"]:
          player_hand.add_card(deck.deal_cards(1))
          player_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      while dealer_hand_value < 17:
        dealer_hand.add_card(deck.deal_cards(1))
        dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(show_all_dealer_cards=True)
      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final Results")
      print("Your hand:", player_hand_value)
      print("Dealer hand:", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, game_over=True)
    
    print("\n Thanks for playing!")

game = Game()
game.play()