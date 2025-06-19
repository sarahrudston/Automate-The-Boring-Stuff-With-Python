# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.

import random

numberOfStreaks = 0
sides = ['H', 'T']

for experimentNumber in range(10000):
    results = []
    for i in range(100):
        results.append(random.choice(sides))

    for i in range(100 - 6):
        if results[i] == results[i+1] == results[i+2] == results[i+3] == results[i+4] == results[i+5]:
            numberOfStreaks += 1
            break

print('Change of streak: %s%%' % (numberOfStreaks / 100))