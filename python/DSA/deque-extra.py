# Shuffling Cards
from collections import deque

deck = deque(['♠A', '♠2', '♠3', '♠4', '♠5'])

print("Original deck:", deck)

# Rotate right by 2 (simulate cutting the deck)
deck.rotate(2)
print("After rotate(2):", deck)

# Rotate left by 1
deck.rotate(-1)
print("After rotate(-1):", deck)