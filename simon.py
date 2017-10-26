from enum import Enum
from random import randint
import time
import os

class Color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4

    def get_value(self, num):
        for color in Color:
            print(color)

def compare(l1, l2):
    if not l1 or not l2: return False
    if len(l1) != len(l2): return False
    for i in range(len(l1)):
        if l1[i] != l2[i]: return  False
    return True

def clear():
    os.system('clear')

def print_list(l):
    for color in l:
        print (color.value)
        time.sleep(1)
    clear()

def game():
    l1 = list()
    test = True
    while test:
        clear()
        l2 = list()
        color = Color(randint(1, 4))
        l1.append(color)
        print_list(l1)
        print('Digite as cores:')
        for value in range(len(l1)):
            l2.append(Color(int(input())))
        test = compare(l1,l2)
    print('Infelizmente voce perdeu, voce acertou ' + str(len(l1) - 1) + ' vezes')

game()
