from random import shuffle
import sys
sys.path.insert(1, r'C:\Users\Aloysius Goo\Desktop\Python and robotics code\blackjack simulator')
from actions import actions
cards = [i // 32 for i in range(32,351)]
for i in range(96):
    cards.append(10)
playerCards = [[] for i in range(6)]
splitCards = [[[] for i in range(3)] for j in range(6)]
#0 means hit
#1 means stand
#2 means split
#1st dimension is the dealer's card, going from A, 2, 3, 4 and so on
#2nd dimension is the player's hand
#the dealer's upcard is the 1st card

chartHard = [[0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,1,1,1,1,1], [0,0,0,0,0,1,1,1,1,1,1], [0,0,0,0,1,1,1,1,1,1,1], [0,0,0,0,1,1,1,1,1,1,1], [0,0,0,0,1,1,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,1,1]]
#4-8, 9, 10, 11 and so on

chartSoft = [[0,0,0,0,0,0,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,1,1,1], [0,0,0,0,0,0,1,1], [0,0,0,0,0,0,1,1]]
#13, 14, 15, 16 and so on

chartSplit = [[2,0,0,0,0,0,2,1], [2,0,0,0,0,2,2,2], [2,0,0,0,2,2,2,2], [2,2,2,0,2,2,2,2], [2,2,2,0,2,2,2,2], [2,2,2,0,2,2,2,2], [2,2,2,0,0,2,1,2], [2,0,0,0,0,0,2,2], [2,0,0,0,0,0,2,2], [2,0,0,0,0,0,2,1]]
#A, 2, 3, 4 and so on

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
action = 3
upCard = playerCards[5][0]
upCard -= 1

for i in range(5):
    if run.player[i][0] == run.player[i][1] and run.player[i][0] != 5 and run.player[i][0] != 10:
        playerCard = run.player[i][0]
        playerCard -= 1
        if playerCard > 4:
            playerCard -= 1
        action = chartSplit[upCard][playerCard]
        if action == 2:
            run.split(i, 0)
            run.hit(i,0)
            run.hit(i,1)
            playerCard = run.player[i][0]
            playerCard -= 1
            if playerCard > 4:
                playerCard -= 1
            if run.player[i][0] == run.player[i][1] and chartSplit[upCard][playerCard] == 2:
                run.split(i, 0)
                run.hit(i, 0)
                run.hit(i, 2)
            playerCard = run.splitCards[i][0][0]
            playerCard -= 1
            if playerCard > 4:
                playerCard -= 1
            if run.splitCards[i][0][0] == run.splitCards[i][0][1] and chartSplit[upCard][playerCard]:
                run.split(i, 1)
                run.hit(i, 1)
                if len(run.splitCards[i][1]) != 0:
                    run.hit(i, 3)
                else:
                    run.hit(i, 2)
                    bestIndex = 4
                    bestSplitCard = 12
                    minIndex = 4
                    minSplitCard = 12
                    for j in range(3):
                        if j == 0:
                            playerCard = run.player[i][0]
                        else:
                            playerCard = run.splitCards[i][j - 1][0]
                        playerCard -= 1
                        if playerCard > 4:
                            playerCard -= 1
                        if chartSplit[i][playerCard] == 2:
                            if j == 0:
                                if run.player[i][0] == run.player[i][1] and run.player[i][0] < minSplitCard:
                                    minIndex = 0
                                    minSplitCard = run.player[i][0]
                                    if run.player[i][0] == 1:
                                        bestIndex = 0
                                        bestSplitCard = 1
                                    if run.player[i][0] == 8 and bestSplitCard != 1:
                                        bestIndex = 0
                                        bestSplitCard = 8
                            else:
                                if len(run.splitCards[i][j - 1]) != 0:
                                    if run.splitCards[i][j - 1][0] == run.splitCards[i][j - 1][1] and run.splitCards[i][j - 1][0] < minSplitCard:
                                        minIndex = j
                                        minSplitCard = run.splitCards[i][j - 1][0]
                                        if run.splitCards[i][j - 1][0] == 1:
                                            bestIndex = j
                                            bestSplitCard = 1
                                        if run.splitCards[i][j - 1][0] == 8 and bestSplitCard != 1:
                                            bestIndex = j
                                            bestSplitCard = 8
                    if bestIndex != 4:
                        run.split(i, bestIndex)
                        run.hit(i, bestIndex)
                        run.hit(i, 3)
                    else:
                        run.split(i, minIndex)
                        run.hit(i, minIndex)
                        run.hit(i, 3)
    print("player:", run.player[0:5])
    print("dealer:", run.player[5])
    print("splitCards:", run.splitCards)
    action = 3
    while action != 1:
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
            hsCheck = True
            if j == 0:
                playerCard = sum(run.player[i])
                for k in range(len(run.player[i])):
                    hsCheck = (run.player[i][k] != 11) == hsCheck
                if hsCheck:
                    if playerCard > 8:
                        if playerCard < 19:
                            action = chartHard[upCard][playerCard - 8]
                        else:
                            action = chartHard[upCard][10]
                    else:
                        action = chartHard[upCard][0]
                else:
                    if playerCard  < 21:
                        action = chartSoft[upCard][playerCard - 13]
                    else:
                        action = chartSoft[upCard][7]
                if action == 0:
                    run.hit(i, 0)
                    aceCheck = True
                    if run.player[i][len(run.player[i]) - 1] == 1:
                        for k in range(len(run.player[i])):
                            aceCheck = (run.player[i][k] != 11) == aceCheck
                        if aceCheck:
                            run.player[i][len(run.player[i]) - 1] = 11
                    if sum(run.player[i]) > 21:
                        for k in range(len(run.player[i])):
                            if run.player[i][k] == 11:
                                run.player[i][k] = 1
            else:
                if len(run.splitCards[i][j - 1]) != 0:
                    playerCard = sum(run.splitCards[i][j - 1])
                    for k in range(len(run.splitCards[i][j - 1])):
                        hsCheck = (run.splitCards[i][j - 1][k] != 11) == hsCheck
                    if hsCheck:
                        if playerCard > 8:
                            if playerCard < 19:
                                action = chartHard[upCard][playerCard - 8]
                            else:
                                action = chartHard[upCard][10]
                        else:
                            action = chartHard[upCard][0]
                    else:
                        if playerCard < 21:
                            action = chartSoft[upCard][playerCard - 13]
                        else:
                            action = chartSoft[upCard][7]
                    if action == 0:
                        run.hit(i, j)
                        aceCheck = True
                        if run.splitCards[i][j - 1][len(run.splitCards[i][j - 1]) - 1] == 1:
                            for k in range(len(run.splitCards[i][j - 1])):
                                aceCheck = (run.splitCards[i][j - 1][k] != 11) == aceCheck
                            if aceCheck:
                                run.splitCards[i][j - 1][len(run.splitCards[i][j - 1]) - 1] = 11
                        if sum(run.splitCards[i][j - 1]) > 21:
                            for k in range(len(run.splitCards[i][j - 1])):
                                if run.splitCards[i][j - 1][k] == 11:
                                    run.splitCards[i][j - 1][k] = 1
    print("player:", run.player[0:5])
    print("dealer:", run.player[5])
    print("splitCards:", run.splitCards)
