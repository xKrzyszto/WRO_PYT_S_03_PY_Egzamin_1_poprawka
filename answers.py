_card_values = ['A', 'K', 'Q', 'J',
                '10', '9', '8', '7', '6', '5', '4', '3', '2']
_card_colors = ['hearts', 'diamonds', 'spades', 'clubs']

# do rozwiązania zadania z kartami pokerowymi użyj tej listy:
cards = [v + ' of ' + c for v in _card_values for c in _card_colors]
