from truecolor import fg
from os import system
from random import randint


t = ""
for x in range(100):
    s = ""
    for z in range(158):
        s += f"{fg((randint(0, 255), randint(0, 255), randint(0, 255)))}██"
    t += f"{s}\n"


system('cls')
input(t)