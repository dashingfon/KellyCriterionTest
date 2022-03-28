from random import randint
import json


GENERATIONS = 150
ROUNDS = 30
BALANCE = 8000
SAVE = True
DISPLAY = False
EDGE_STATUS = 'VARIABLE'
REAL_STATUS = 'VARIABLE'
PROB_EDGE = [45,50]
PROB_REAL = [55,65]
PLAYER = 'kelly'


class Game():
    def __init__(self,player):
        self.player = player
        
        if self.player.method == 'manual':
            self.gens = 1
        else:
            self.gens = GENERATIONS
            
        self.rounds = ROUNDS
        self.real = PROB_REAL
        self.edge = PROB_EDGE
        self.balance = BALANCE
        self.display = DISPLAY
        
    def getEdge(self):
        if EDGE_STATUS == 'FIXED':
            return self.edge
        elif EDGE_STATUS == 'VARIABLE':
            return randint(self.edge[0],self.edge[1])
    
    def getReal(self):
        if REAL_STATUS == 'FIXED':
            return self.real
        elif REAL_STATUS == 'VARIABLE':
            return randint(self.real[0],self.real[1])

    def save(self,load):
        if SAVE:
            with open(r'Kelly.json','w') as KJ:
                json.dump(load,KJ,indent = 2)

    def Play(self):
        Round = 0
        if self.display:
            print('Welcome to the betting simulation game')
            print('The aim of the game is to wager an amount of money to maximize the balance after the game without going bust')
        
        Result = {}

        for gen in range(self.gens):
            self.balance = BALANCE
            name = f'Gen{gen + 1}'
            Result[name] = []
            Result[name].append(self.balance)
            for i in range(self.rounds):

                Round += 1
                Edge = self.getEdge()
                Real = self.getReal()
                if self.display:
                    print(f'Round {Round} / {self.rounds}')
                    print(f'your edge is {Edge}')
                    
                info = {
                    'Round':f'{Round} /' + str(self.rounds),
                    'Edge': Edge,
                    'Real' : Real,
                    'Balance': self.balance
                }

                if self.balance <= 0:
                    Result[name].append(0)
                else:
                    Wager = self.player.getWager(info)
                    self.balance -= Wager

                    outcome = randint(1,100)
                    if outcome > Real:
                        Result[name].append(self.balance)
                    else:
                        self.balance += (Wager * (1/(Edge/100)))
                        Result[name].append(self.balance)

        self.save(Result)

class Player():
    def __init__(self, PLAYER):
        self.method = PLAYER
    
    def getWager(self,info):
        if self.method == 'manual':
            found = False
            
            while not found:
                print('Please Enter the amount you want to wager')
                amount = input()
                try: 
                    int(amount)
                except ValueError:
                    print('Invalid ammount')
                else:
                    if int(amount) <= info['Balance']:
                        found = True
                    else:
                        print('amount is more than the balance')
            
            return int(amount)
                    
        elif self.method == 'kelly':
            pWin = info['Real']/100
            wager = (pWin - (1 - pWin)/(1/(info['Edge']/100)-1)) * info['Balance']

            return wager

if __name__ == '__main__':
    player = Player(PLAYER)
    game = Game(player)
    game.Play()

