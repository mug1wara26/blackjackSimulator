from random import shuffle
import sys
sys.path.insert(1, r'C:\Users\Aloysius Goo\Desktop\Python and robotics code\blackjack simulator')
from actions import actions
cards = [i // 32 for i in range(32,351)]
for i in range(96):
    cards.append(10)
playerCards = [[] for i in range(6)]
splitCards = [[[] for i in range(3)] for j in range(6)]

print("deck")
print(cards)
shuffle(cards)
run = actions(cards, playerCards, splitCards)
print("shuffled deck")
print(run.cards)
for i in range(2):
    for j in range(5):
        run.hit(j, 0)
        print("player cards are:")
        print(run.player[0:5])
    run.hit(5, 0)
    print("dealer cards are:")
    print(run.player[5])
for a in range(1000):
    for i in range(6):
        minIndex = 4
        minSplitCard = 12
        if run.player[i][0] == run.player[i][1]:
            run.split(i,0)
            run.hit(i,0)
            run.hit(i,1)
            if run.player[i][0] == run.player[i][1] and run.splitCards[i][0][0] == run.splitCards[i][0][1]:
                if run.player[i][0] <= run.splitCards[i][0][0]:
                    run.split(i, 0)
                    run.hit(i,0)
                    run.hit(i,2)
                else:
                    run.split(i, 1)
                    run.hit(i,1)
                    run.hit(i,2)
            else:
                if run.player[i][0] == run.player[i][1]:
                    run.split(i, 0)
                    run.hit(i,0)
                    run.hit(i,2)
                if run.splitCards[i][0][0] == run.splitCards[i][0][1]:
                    run.split(i, 1)
                    run.hit(i,1)
                    run.hit(i,2)
            for j in range(3):
                if j == 0 :
                    if run.player[i][0] == run.player[i][1] and run.player[i][0] < minSplitCard:
                        minIndex = 0
                        minSplitCard = run.player[i][0]
                else:
                    if len(run.splitCards[i][j - 1]) != 0:
                        if run.splitCards[i][j - 1][0] == run.splitCards[i][j - 1][1] and run.splitCards[i][j - 1][0] < minSplitCard:
                            minIndex = j
                            minSplitCard = run.splitCards[i][j - 1][0]
            if minIndex != 4:
                run.split(i, minIndex)
                run.hit(i, minIndex)
                run.hit(i, 3)
        if run.player[i][0] == 1:
            run.player[i][0] = 11
        if run.player[i][1] == 1 and run.player[i][0] != 11:
            run.player[i][1] = 11
        for j in range(3):
            if len(run.splitCards[i][j]) != 0:
                if run.splitCards[i][j][0] == 1:
                    run.splitCards[i][j][0] = 11
                if run.splitCards[i][j][1] == 1 and run.splitCards[i][j][0] != 11:
                    run.splitCards[i][j][1] = 11
        for j in range(4):
            if j == 0:
                while sum(run.player[i]) < 16:
                    truthCheck = True
                    run.hit(i, j)
                    if run.player[i][len(run.player[i]) - 1] == 1:
                        for k in range(len(run.player[i])):
                            truthCheck = (run.player[i][k] != 11) == truthCheck
                        if truthCheck:
                            run.player[i][len(run.player[i]) - 1] = 11
                    if sum(run.player[i]) > 21:
                        for k in range(len(run.player[i])):
                            if run.player[i][k] == 11:
                                run.player[i][k] = 1
            else:
                while sum(run.splitCards[i][j - 1]) < 16 and len(run.splitCards[i][j - 1]) != 0:
                    run.hit(i, j)
                    truthCheck = True
                    if run.splitCards[i][j - 1][len(run.splitCards[i][j - 1]) - 1] == 1:
                        for k in range(len(run.splitCards[i][j - 1])):
                            truthCheck = (run.splitCards[i][j - 1][k] != 11) == truthCheck
                        if truthCheck:
                            run.splitCards[i][j - 1][len(run.splitCards[i][j - 1]) - 1] = 11
                    if sum(run.splitCards[i][j - 1]) > 21:
                        for k in range(len(run.splitCards[i][j - 1])):
                            if run.splitCards[i][j - 1][k] == 11:
                                run.player[i][j - 1][k] = 1
        print("player:", run.player[0:5])
        print("dealer:", run.player[5])
        print("splitCards:", run.splitCards)
