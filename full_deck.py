suits = ['♦', '♠', '♣', '♥']
face_cards = ['A', 'J', 'Q', 'K']

deck = []
template = '{value}{suit}'

for suit in suits:
  for card in face_cards:
    deck.append(template.format(value = card, suit=suit))
  for i in range(2, 11):
    deck.append(template.format(value = i, suit=suit))

