import random


class Player:

    def __init__(self):
        self.score = 0

    def choose_the_move(self):
        pass


class HumanPlayer(Player):

    def choose_the_move(self):
        super().choose_the_move()
        while True:
            move = input('Rock, paper or scissors [r,p,s]? ')
            if move in ['r','p','s']:
                return move


class ComputerPlayer(Player):

    def choose_the_move(self):
        super().choose_the_move()
        move = random.choice(['r','p','s'])
        return move


class Game:

    MOVES = {
        ('r', 'r'): 'tie', ('p', 'p'): 'tie', ('s', 's'): 'tie',
        ('r', 'p'): 'lost', ('p', 's'): 'lost', ('s', 'r'): 'lost',
        ('r', 's'): 'won', ('p', 'r'): 'won', ('s', 'p'): 'won'
    }

    def __init__(self, rounds):
        self.rounds = rounds
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()

    def settle_round(self, h_choice, c_choice):
        outcome = self.MOVES[(h_choice, c_choice)]
        if outcome == 'won':
            print('You won this round!\n')
            self.human_player.score += 1
        elif outcome == 'lost':
            print('You lost this round!\n')
            self.computer_player.score += 1
        else:
            print('This round is a tie!\n')

    def play_round(self):
        human_choice = self.human_player.choose_the_move()
        computer_choice = self.computer_player.choose_the_move()
        print(f'You: {human_choice} | Computer: {computer_choice}')
        self.settle_round(human_choice, computer_choice)

    def summarise_score(self):
        print(f'[Game summary] Your points: {self.human_player.score} | Computer points: {self.computer_player.score}')
        if self.human_player.score > self.computer_player.score:
            print ("You won.")
        elif self.human_player.score < self.computer_player.score:
            print ("Computer won.")
        else:
            print ("It was a tie.")   

    def play(self):
        for _ in range(self.rounds):
            self.play_round()
        self.summarise_score()     


print('--- Rock Paper Scissors Game ---')

while True:
    rounds = input('How many round would you like to play? ')

    if rounds.isnumeric():
        Game(int(rounds)).play()
        break
