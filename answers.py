# Zadanie 3

def validate_password(str):
    valid_characters = (['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]}\|;:?/>.<,'])
    if 'i' in valid_character and (len(str) > 8:    #już tu nic nie stworzę.
        return True
    else:
        return False


# Zadanie 4

def div(a, b):
    if a % b == 0:
        return True
    else:
        return False


# Zadanie 5

def find_longest_word(word_list):
    longest_word =  max(word_list, key=len)
    return longest_word

#powinno działać, ale gdzieś jest błąd


#Zadanie 6

import itertools, random    # Zdaję sobie sprawę, że ta linijka powinna być na samej górze

deck = list(itertools.product(['A', 'K', 'Q', 'J',
                                '10', '9', '8', '7', '6', '5', '4', '3', '2'],
                              ['Heart', 'Diamond', 'Spade', 'Club']))

random.shuffle(deck)

print("Rozdanie:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

# Nie użyłem podanej listy, bo z nią wychodziły mi takie bzdety, że głowa mała.
# W nazwach kolorów dałem wielkie litery na początku i zlikwidowałem "s" na końcu,
# bo pisze się np. Jack of Diamond, a nie diamonds. Tonę, ale fason trzymam!

