from random import shuffle
import sys, time
sys.path.insert(1, r'C:\Users\Aloysius Goo\Desktop\Python and robotics code\blackjack simulator')
from actions import actions

def noStrategy():
    cards = [i // 32 for i in range(32,351)]
    for i in range(96):
        cards.append(10)
    playerCards = [[] for i in range(6)]
    splitCards = [[[] for i in range(3)] for j in range(6)]
    shuffle(cards)
    run = actions(cards, playerCards, splitCards)
    for i in range(2):
        for j in range(5):
            run.hit(j, 0)
        run.hit(5, 0)
    for i in range(6):
        minIndex = 4
        minSplitCard = 12
        if run.player[i][0] == run.player[i][1] and run.player[i][0] != 1:
            run.split(i,0)
            run.hit(i,0)
            run.hit(i,1)
            if run.player[i][0] == run.player[i][1] and run.splitCards[i][0][0] == run.splitCards[i][0][1] and run.splitCards[i][0][0] != 1:
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
                if run.splitCards[i][0][0] == run.splitCards[i][0][1] and run.splitCards[i][0][0] != 1:
                    run.split(i, 1)
                    run.hit(i,1)
                    run.hit(i,2)
            for j in range(3):
                if j == 0 :
                    if run.player[i][0] == run.player[i][1] and run.player[i][0] < minSplitCard and run.player[i][0] != 1:
                        minIndex = 0
                        minSplitCard = run.player[i][0]
                else:
                    if len(run.splitCards[i][j - 1]) != 0:
                        if run.splitCards[i][j - 1][0] == run.splitCards[i][j - 1][1] and run.splitCards[i][j - 1][0] < minSplitCard and run.splitCards[i][j - 1][0] != 1:
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
                softCheck = True
                while sum(run.player[i]) < 16:
                    if i == 5:
                        for k in run.player[5]:
                            if k == 11:
                                softCheck = False
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
                if i == 5:
                    if softCheck == False:
                        while sum(run.player[5]) < 18:
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
                                run.splitCards[i][j - 1][k] = 1
    return run.player, run.splitCards

for a in range(1):
    playerWins = 0
    playerLose = 0
    draw = 0
    dealerWins = 0
    dealerTies = 0
    attempts = 10 ** (a + 6)
    start = time.time()
    for i in range(attempts):
        playerCards, splitCards = noStrategy()
        dealerMainHand = sum(playerCards[5])
        specificWins = 0
        specificLose = 0
        dealerHands = 1
        k = 0
        while len(splitCards[5][k]) != 0:
            dealerHands += 1
            if k < 2:
                k += 1
            else:
                break
                    
        for j in range(5):
            playerHands = 1
            k = 0
            while len(splitCards[j][k]) != 0:
                playerHands += 1
                if k < 2:
                    k += 1
                else:
                    break
            playerResult = [[[] for i in range(dealerHands)] for j in range(playerHands)]
            for k in range(playerHands):
                if k == 0:
                    for l in range(dealerHands):
                        if l == 0:
                            if len(playerCards[j]) == 2 and sum(playerCards[j]) == 21:
                                if len(playerCards[5]) == 2 and dealerMainHand == 21:
                                    playerResult[k][l] = 2
                                else:
                                    playerResult[k][l] = 1
                            elif len(playerCards[5]) == 2 and dealerMainHand == 21:
                                playerResult[k][l] = 0
                            elif sum(playerCards[j]) == dealerMainHand:
                                playerResult[k][l] = 2
                            elif dealerMainHand < 22:
                                playerResult[k][l] = sum(playerCards[j]) > dealerMainHand and sum(playerCards[j]) < 22
                            elif sum(playerCards[j]) > 21:
                                playerResult[k][l] = 2
                            else:
                                playerResult[k][l] = 1
                        elif len(playerCards[j]) == 2 and sum(playerCards[j]) == 21:
                            if len(splitCards[5][l - 1]) == 2 and sum(splitCards[5][l - 1]) == 21:
                                playerResult[k][l] = 2
                            else:
                                playerResult[k][l] = 1
                        elif len(splitCards[5][l - 1]) == 2 and sum(splitCards[5][l - 1]) == 21:
                            playerResult[k][l] = 0
                        elif sum(playerCards[j]) == sum(splitCards[5][l - 1]):
                            playerResult[k][l] = 2
                        elif sum(splitCards[5][l - 1]) < 22:
                            playerResult[k][l] = sum(playerCards[j]) > sum(splitCards[5][l - 1]) and sum(playerCards[j]) < 22
                        elif sum(playerCards[j]) > 21:
                            playerResult[k][l] = 2
                        else:
                            playerResult[k][l] = 1
                else:
                    for l in range(dealerHands):
                        if l == 0:
                            if len(splitCards[j][k - 1]) == 2 and sum(splitCards[j][k - 1]) == 21:
                                if len(playerCards[5]) == 2 and dealerMainHand == 21:
                                    playerResult[k][l] = 2
                                else:
                                    playerResult[k][l] = 1
                            elif len(playerCards[5]) == 2 and dealerMainHand == 21:
                                playerResult[k][l] = 0
                            elif sum(splitCards[j][k - 1]) == dealerMainHand:
                                playerResult[k][l] = 2
                            elif dealerMainHand < 22:
                                playerResult[k][l] = sum(splitCards[j][k - 1]) > dealerMainHand and sum(splitCards[j][k - 1]) < 22
                            elif sum(splitCards[j][k - 1]) > 21:
                                playerResult[k][l] = 2
                            else:
                                playerResult[k][l] = 1
                        elif len(splitCards[j][k - 1]) == 2 and sum(splitCards[j][k - 1]) == 21:
                            if len(splitCards[5][l - 1]) == 2 and sum(splitCards[5][l - 1]) == 21:
                                playerResult[k][l] = 2
                            else:
                                playerResult[k][l] = 1
                        elif len(splitCards[5][l - 1]) == 2 and sum(splitCards[5][l - 1]) == 21:
                            playerResult[k][l] = 0
                        elif sum(splitCards[j][k - 1]) == sum(splitCards[5][l - 1]):
                            playerResult[k][l] = 2
                        elif sum(splitCards[5][l - 1]) < 22:
                            playerResult[k][l] = sum(splitCards[j][k - 1]) > sum(splitCards[5][l - 1]) and sum(splitCards[j][k - 1]) < 22
                        elif sum(splitCards[j][k - 1]) > 21:
                            playerResult[k][l] = 2
                        else:
                            playerResult[k][l] = 1
            for k in range(len(playerResult)):
                wins = 0
                lose = 0
                for l in range(len(playerResult[k])):
                    if playerResult[k][l] == 0:
                        lose += 1
                    if playerResult[k][l] == 1:
                        wins += 1
                if wins > lose:
                    playerResult[k] = 1
                if lose > wins:
                    playerResult[k] = 0
                if wins == lose:
                    playerResult[k] = 2
            wins = 0
            lose = 0
            for k in playerResult:
                if k == 0:
                    lose += 1
                if k == 1:
                    wins += 1
            if wins > lose:
                specificWins += 1
                playerWins += 1
            if lose > wins:
                specificLose += 1
                playerLose += 1
            if wins == lose:
                draw += 1
        if specificWins < specificLose:
            dealerWins += 1
        if specificLose == specificWins:
            dealerTies += 1

    print("ran for", attempts, "attempts")
    print("specific number of players who won are:", playerWins)
    print("specific number of players who lost are:", playerLose)
    print("specific number of draws are:", draw)
    print("----------------------------------------------------")
    print("assuming simple majority needed for players to win,")
    print("player wins are:", attempts - dealerWins - dealerTies)
    print("ties are:", dealerTies)
    print("dealer wins are:", dealerWins)
    print("time taken:", str(round(time.time() - start, 5)) + 's')
    print('\n' * 3)
