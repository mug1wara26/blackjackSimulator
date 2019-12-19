class actions:
    def __init__(self, cards, playerCards, splitCards):
        self.cards = cards
        self.player = playerCards
        self.splitCards = splitCards
        self.freeSplit = 0
        self.splitCard = 0
    def hit(self, player, index):
        self.draw = self.cards[0]
        self.cards.pop(0)
        if index == 0:
            self.player[player].append(self.draw)
        else:
            self.splitCards[player][index-1].append(self.draw)
    def split(self, player, index):
        self.freeSplit = 0
        if index == 0:
            self.player[player].pop(1)
            self.splitCard = self.player[player][0]
        else:
            self.splitCards[player][index - 1].pop(1)
            self.splitCard = self.splitCards[player][index - 1][0]
        while len(self.splitCards[player][self.freeSplit]) != 0:
            self.freeSplit += 1
        self.splitCards[player][self.freeSplit].append(self.splitCard)
