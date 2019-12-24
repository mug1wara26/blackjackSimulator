from random import shuffle
import sys, time
sys.path.insert(1, r'C:\Users\Aloysius Goo\Desktop\Python and robotics code\blackjack simulator')
from actions import actions
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

def compositionChart(cards,dealer):
    cards.sort()
    if len(cards)==2:
        if cards==[2,6]:
            return 0
        if cards==[2,10]:
            if dealer==5:
                return 1
            return 0
        if cards==[3,9]:
            if dealer in [4,5,6]:
                return 1
            return 0
        if cards in [[4,8],[5,7],[3,10]]:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if cards in [[2,2],[6,6]]:
            if dealer in [8,9,10,1]:
                return 1
            return 2
        if cards==[3,3]:
            if dealer in [9,10,1]:
                return 1
            return 2
        if cards==[4,4]:
            if dealer in [4,5,6]:
                return 2
            return 1
        if cards==[5,5]:
            return 0
        if cards==[7,7]:
            if dealer==10:
                return 1
            if dealer in [9,1]:
                return 0
            return 2
        if cards in [[1,1],[8,8]]:
            return 2
        if cards==[9,9]:
            if dealer in [7,10,1]:
                return 1
            return 2
        if cards==[10,10]:
            return 1
        if 1 in cards:
            if sum(cards)<=7:
                return 0
            if sum(cards)==8:
                if dealer in [9,10]:
                    return 0
                return 1
            return 1
        if sum(cards)<=11:
            return 0
        if sum(cards)<=16:
            if dealer in [2,3,4,5,6]:
                return 1
            return 0
        return 1
    if len(cards)==3:
        if cards==[1,2,10]:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if cards in [[3,6,6],[4,5,6],[5,5,5]]:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        if cards in [[1,6,9],[2,6,8],[3,6,7],[4,6,6]]:
            if dealer in [2,3,4,5,6]:
                return 1
            return 0
        if cards in [[3,5,8],[4,4,8],[5,5,6]]:
            if dealer in [7,8,1]:
                return 0
            return 1
        if cards==[1,1,6]:
            if dealer in [9,10,1]:
                return 0
            return 1
        if 1 in cards:
            if sum(cards)<=7:
                return 0
            if sum(cards)==8:
                if dealer in [9,10]:
                    return 0
                return 1
            return 1
        if sum(cards)<=11:
            return 0
        if sum(cards)==12:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if sum(cards)<=15:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if sum(cards)==15:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        return 1
    if len(cards)==4:
        if cards in [[1,2,2,7],[1,2,3,6],[1,3,3,5],[2,2,2,6],[2,2,3,5],[2,3,3,4]]:
            if dealer in [4,5,6]:
                return 1
            return 0
        if cards in [[1,4,5,5],[1,3,5,6],[1,2,6,6]]:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        if cards in [[1,1,5,9],[1,2,4,9],[1,2,5,8],[1,3,4,8],[1,4,5,6],[2,2,4,8],[2,3,3,8],[2,4,4,8]]:
            if dealer in [7,8,1]:
                return 0
            return 1
        if cards in [[1,5,5,5],[2,4,5,5],[3,3,5,5],[3,4,4,5],[4,4,4,4]]:
            if dealer==1:
                return 1
            return 0
        if cards in [[1,1,3,3],[1,2,2,3]]:
            if dealer==9:
                return 1
            return 0
        if 1 in cards:
            if sum(cards)<=7:
                return 0
            if sum(cards)==8:
                if dealer in [9,10]:
                    return 0
                return 1
            return 1
        if sum(cards)<=11:
            return 0
        if sum(cards)==12:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if sum(cards)<=15:
            if dealer in [2,3,4,5,6]:
                return 1
            return 0
        if sum(cards)==16:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        return 1
    if len(cards)==5:
        if cards in [[1,1,3,3,4],[1,2,2,2,5],[1,2,2,3,4],[1,2,3,3,3],[2,2,2,2,4],[2,2,2,3,3]]:
            if dealer in [4,5,6]:
                return 1
            return 0
        if cards in [[1,1,1,3,10],[1,1,2,5,7],[1,1,3,4,7],[1,2,2,4,7],[1,2,3,3,7],[1,3,3,3,6],[2,2,2,3,7]]:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        if cards in [[1,1,4,5,5],[1,2,3,5,5],[1,2,4,4,5],[1,3,3,4,5],[1,3,4,4,4],[2,2,2,5,5],[2,2,3,4,5],[2,2,4,4,4],[2,3,3,3,5],[2,3,3,4,4],[2,3,3,3,5],[2,3,3,4,4],[3,3,3,3,4]]:
            if dealer==1:
                return 0
            return 1
        if cards in [[1,1,1,2,3],[1,1,2,2,2]]:
            if dealer==9:
                return 0
            return 1
        if 1 in cards:
            if sum(cards)<=7:
                return 0
            if sum(cards)==8:
                if dealer in [9,10]:
                    return 0
                return 1
            return 1
        if sum(cards)<=11:
            return 0
        if sum(cards)==12:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if sum(cards)<=15:
            if dealer in [2,3,4,5,6]:
                return 1
            return 0
        if sum(cards)==16:
            if dealer in [7,8,1]:
                return 0
            return 1
        return 1
    if len(cards)==6:
        if cards in [[1,1,1,3,3,3],[1,1,2,2,2,4],[1,1,2,2,3,3,],[1,2,2,2,2,3]]:
            if dealer in [4,5,6]:
                return 1
            return 0
        if cards==[1,1,1,1,5,6]:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        if cards in [[1,1,1,1,3,9],[1,1,1,2,2,9]]:
            if dealer in [7,8,1]:
                return 0
            return 1
        if cards in [[1,1,1,1,6,6],[1,2,2,2,3,6]]:
            if dealer in [2,3,4,5,6]:
                return 1
            return 0
        if cards in [[1,1,1,3,3,7],[1,1,2,2,3,7]]:
            if dealer in [8,9,1]:
                return 0
            return 1
        if cards in [[1,1,1,3,5,5],[1,1,2,2,5,5],[1,1,2,3,4,5],[1,1,2,4,4,4],[1,1,3,3,3,5],[1,1,3,3,4,4],[1,2,2,2,4,5],[1,2,2,3,3,5],[1,2,2,3,4,4],[2,2,2,2,3,5],[2,2,2,2,4,4],[2,2,2,3,3,4],[2,2,2,3,3,4],[2,2,3,3,3,3]]:
            if dealer==1:
                return 0
            return 1
        if cards==[1,2,2,2,2,7]:
            if dealer in [7,8,9,1]:
                return 0
            return 1
        if 1 in cards:
            if sum(cards)<=7:
                return 0
            if sum(cards)==8:
                if dealer in [9,10]:
                    return 0
                return 1
            return 1
        if sum(cards)<=11:
            return 0
        if sum(cards)==12:
            if dealer in [3,4,5,6]:
                return 1
            return 0
        if sum(cards)<=15:
            if dealer in [2,3,4,5,6]:
                return 1
            return 0
        if sum(cards)==16:
            if dealer in [8,1]:
                return 0
            return 1
        return 1
    if 1 in cards:
        if sum(cards)<=7:
            return 0
        if sum(cards)==8:
            if dealer in [9,10]:
                return 0
            return 1
        return 1
    if sum(cards)<=11:
        return 0
    if sum(cards)==12:
        if dealer in [3,4,5,6]:
            return 1
        return 0
    if sum(cards)<=15:
        if dealer in [2,3,4,5,6]:
            return 1
        return 0
    if sum(cards)==16:
        if dealer in [8,1]:
            return 0
        return 1
    return 1

def composition():
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

    for i in range(5):
        run = actions(cards,playerCards,splitCards)
        action = 3
        allAction = 0
        for l in range(4):
            maxIndex = 4
            maxCard = 0
            for j in range(4):
                if j == 0:
                    action = compositionChart(run.player[i], run.player[5][0])
                    if action == 2 and run.player[i][0] > maxCard:
                        maxIndex = j
                        maxCard = run.player[i][0]
                else:
                    if len(run.splitCards[i][j - 1]) != 0:
                        action = compositionChart(run.splitCards[i][j - 1], run.player[5][0])
                        if action == 2 and run.splitCards[i][j - 1][0] > maxCard:
                            maxIndex = j
                            maxCard = run.splitCards[i][j - 1][0]
            if maxIndex != 4:
                run.split(i, maxIndex)
                run.hit(i, maxIndex)
                freeSplit = 4
                for j in range(3):
                    if len(run.splitCards[i][j]) != 2:
                        freeSplit = j
                        break
                run.hit(i, freeSplit + 1)
            if len(run.splitCards[i][2]) != 0:
                break
        #print('here')
        for j in range(4):
            action = 3
            while action != 1 and action != 2:
                if j == 0:
                    action = compositionChart(run.player[i], run.player[5][0])
                    if action == 0:
                        run.hit(i, j)
                else:
                    if len(run.splitCards[i][j - 1]) != 0:
                        action = compositionChart(run.splitCards[i][j - 1], run.player[5][0])
                        if action == 0:
                            run.hit(i, j)
                    else:
                        break
                
        #print('here1')
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
    minIndex = 4
    minSplitCard = 12
    if run.player[5][0] == run.player[5][1] and run.player[5][0] != 1:
        run.split(5,0)
        run.hit(5,0)
        run.hit(5,1)
        if run.player[5][0] == run.player[5][1] and run.splitCards[5][0][0] == run.splitCards[5][0][1] and run.splitCards[5][0][0] != 1:
            if run.player[5][0] <= run.splitCards[5][0][0]:
                run.split(5, 0)
                run.hit(5,0)
                run.hit(5,2)
            else:
                run.split(5, 1)
                run.hit(5,1)
                run.hit(5,2)
        else:
            if run.player[5][0] == run.player[5][1] and run.player[5][0] != 1:
                run.split(5, 0)
                run.hit(5,0)
                run.hit(5,2)
            if run.splitCards[5][0][0] == run.splitCards[5][0][1] and run.splitCards[5][0][0] != 1:
                run.split(5, 1)
                run.hit(5,1)
                run.hit(5,2)
        for j in range(3):
            if j == 0 :
                if run.player[5][0] == run.player[5][1] and run.player[5][0] < minSplitCard:
                    minIndex = 0
                    minSplitCard = run.player[5][0]
            else:
                if len(run.splitCards[5][j - 1]) != 0:
                    if run.splitCards[5][j - 1][0] == run.splitCards[5][j - 1][1] and run.splitCards[5][j - 1][0] < minSplitCard and run.splitCards[5][j - 1][0] != 1:
                        minIndex = j
                        minSplitCard = run.splitCards[5][j - 1][0]
        if minIndex != 4:
            run.split(5, minIndex)
            run.hit(5, minIndex)
            run.hit(5, 3)
    if run.player[5][0] == 1:
        run.player[5][0] = 11
    if run.player[5][1] == 1 and run.player[5][0] != 11:
        run.player[5][1] = 11
    for j in range(3):
        if len(run.splitCards[5][j]) != 0:
            if run.splitCards[5][j][0] == 1:
                run.splitCards[5][j][0] = 11
            if run.splitCards[5][j][1] == 1 and run.splitCards[5][j][0] != 11:
                run.splitCards[5][j][1] = 11
    for j in range(4):
        if j == 0:
            softCheck = True
            while sum(run.player[5]) < 16:
                for k in run.player[5]:
                    if k == 11:
                        softCheck = False
                truthCheck = True
                run.hit(5, j)
                if run.player[5][len(run.player[5]) - 1] == 1:
                    for k in range(len(run.player[5])):
                        truthCheck = (run.player[5][k] != 11) == truthCheck
                    if truthCheck:
                        run.player[5][len(run.player[5]) - 1] = 11
                if sum(run.player[5]) > 21:
                    for k in range(len(run.player[5])):
                        if run.player[5][k] == 11:
                            run.player[5][k] = 1
            if softCheck == False:
                while sum(run.player[5]) < 18:
                    truthCheck = True
                    run.hit(5, j)
                    if run.player[5][len(run.player[5]) - 1] == 1:
                        for k in range(len(run.player[5])):
                            truthCheck = (run.player[5][k] != 11) == truthCheck
                        if truthCheck:
                            run.player[5][len(run.player[5]) - 1] = 11
                    if sum(run.player[5]) > 21:
                        for k in range(len(run.player[5])):
                            if run.player[5][k] == 11:
                                run.player[5][k] = 1
        else:
            while sum(run.splitCards[5][j - 1]) < 16 and len(run.splitCards[5][j - 1]) != 0:
                run.hit(5, j)
                truthCheck = True
                if run.splitCards[5][j - 1][len(run.splitCards[5][j - 1]) - 1] == 1:
                    for k in range(len(run.splitCards[5][j - 1])):
                        truthCheck = (run.splitCards[5][j - 1][k] != 11) == truthCheck
                    if truthCheck:
                        run.splitCards[5][j - 1][len(run.splitCards[5][j - 1]) - 1] = 11
                if sum(run.splitCards[5][j - 1]) > 21:
                    for k in range(len(run.splitCards[5][j - 1])):
                        if run.splitCards[5][j - 1][k] == 11:
                            run.splitCards[5][j - 1][k] = 1
    return run.player, run.splitCards

for a in range(1):
    playerWins = 0
    playerLose = 0
    draw = 0
    dealerWins = 0
    dealerTies = 0
    attempts = 10 ** (a + 6)
    start = time.time()
    for b in range(attempts):
        playerCards, splitCards = composition()
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
        if b % (attempts / 100) == 0:
            print(str(b / (attempts / 100)) + '%')

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
