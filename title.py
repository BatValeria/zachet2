import random
from random import choice

books_file = "book.txt"

with open(books_file) as file:
    a = [line for line in file]


def title_():
    b = random.choice(a)
    return b.replace("\n", "")
