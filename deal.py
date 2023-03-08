from full_deck import deck
import random

#creates first hand of seven cards, removes those cards from the deck and then creates another hand of seven cards
hand_a = random.sample(deck, 7)
for card in hand_a:
  deck.remove(card)
hand_b = random.sample(deck, 7)

value_asked = random.choice(hand_a)[:-1]

def go_fish():
  print("Player A: " + str(hand_a))
  print('Player B: ' + str(hand_b))
  print('\n')
  print('Player A: Do you have any ' + value_asked + 's?')
  for card in hand_b:
    if value_asked in card:
      print("Player B: Yes")
      break
  else:
    print("Player B: Go fish!")



