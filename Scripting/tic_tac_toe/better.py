import random
import os


class TickTackToe(object):
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.board = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
        self.ascii_board = f'''     |     |     \n  {self.board["1"]}  |  {self.board["2"]}  |  {self.board["3"]}     \n     |     |     \n------------------\n     |     |     \n  {self.board["4"]}  |  {self.board["5"]}  |  {self.board["6"]}     \n     |     |     \n------------------\n     |     |     \n  {self.board["7"]}  |  {self.board["8"]}  |  {self.board["9"]}     \n     |     |     \n'''
        self.player1 = []
        self.player2 = []
        self.choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print(self.ascii_board)

    def valid_move(self, move):
        if move in self.choices:
            return True
        else:
            return False

    def make_move(self, player, move):
        if player == "player1":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.board[move] = "o"
            self.player1.append(move)
            self.choices.remove(move)
            self.ascii_board = f'''     |     |     \n  {self.board["1"]}  |  {self.board["2"]}  |  {self.board["3"]}     \n     |     |     \n------------------\n     |     |     \n  {self.board["4"]}  |  {self.board["5"]}  |  {self.board["6"]}     \n     |     |     \n------------------\n     |     |     \n  {self.board["7"]}  |  {self.board["8"]}  |  {self.board["9"]}     \n     |     |     \n'''
            print(self.ascii_board)

        elif player == "player2":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.board[move] = "x"
            self.choices.remove(move)
            self.player2.append(move)
            self.ascii_board = f'''     |     |     \n  {self.board["1"]}  |  {self.board["2"]}  |  {self.board["3"]}     \n     |     |     \n------------------\n     |     |     \n  {self.board["4"]}  |  {self.board["5"]}  |  {self.board["6"]}     \n     |     |     \n------------------\n     |     |     \n  {self.board["7"]}  |  {self.board["8"]}  |  {self.board["9"]}     \n     |     |     \n'''
            print(self.ascii_board)

    def computer_move(self):
        move = random.choice(self.choices)
        self.make_move("player2", move)

    def check_game_over(self):
        if "1" in self.player1 and "2" in self.player1 and "3" in self.player1 or "1" in self.player2 and "2" in self.player2 and "3" in self.player2:
            return True
        elif "3" in self.player1 and "4" in self.player1 and "5" in self.player1 or "3" in self.player2 and "4" in self.player2 and "5" in self.player2:
            return True
        elif "7" in self.player1 and "8" in self.player1 and "9" in self.player1 or "7" in self.player2 and "8" in self.player2 and "9" in self.player2:
            return True
        elif "1" in self.player1 and "4" in self.player1 and "7" in self.player1 or "1" in self.player2 and "4" in self.player2 and "7" in self.player2:
            return True
        elif "2" in self.player1 and "5" in self.player1 and "8" in self.player1 or "2" in self.player2 and "5" in self.player2 and "8" in self.player2:
            return True
        elif "3" in self.player1 and "6" in self.player1 and "9" in self.player1 or "3" in self.player2 and "6" in self.player2 and "9" in self.player2:
            return True
        elif "1" in self.player1 and "5" in self.player1 and "9" in self.player1 or "1" in self.player2 and "5" in self.player2 and "9" in self.player2:
            return True
        elif "3" in self.player1 and "5" in self.player1 and "7" in self.player1 or "3" in self.player2 and "5" in self.player2 and "7" in self.player2:
            return True
        else:
            return False


game_on = True
while game_on:
    is_game_on = input("Do you want to play a game of Tick Tack Toe (y/n)\n")
    while is_game_on not in ["y", "n"]:
        print("please input y or n\n")
        is_game_on = input("Do you want to play a game of Tick Tack Toe (y/n)\n")
    if is_game_on == "y":
        game = TickTackToe()
        while not game.check_game_over():
            move = input("Make your move by inputing an integer in the screen\n")
            valid_move = game.valid_move(move)
            while not valid_move:
                print("invalid Move\n")
                move = input("Make your move by inputing an integer in the screen\n")
                valid_move = game.valid_move(move)
            game.make_move("player1", move)
            if not game.check_game_over():
                game.computer_move()
    else:
        game_on = False
