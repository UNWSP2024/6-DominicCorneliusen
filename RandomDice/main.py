#Title: Random Dice
#Author: Dominic Corneliusen
#Date last modified: 2-27-2026

#Start
import random
def randDice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum = roll1 + roll2
    return sum
total = 0
for number in range(100):
    total = randDice() + total
average = round(total / 100, 2)
print("The average is ", average)