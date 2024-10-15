class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name(letters only): ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid name.Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name},Choose your symbol(single letter only): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("Invalid symbol.Please choose single letter only.")


class Menu:
    def display_main_menu(self):
        print("Welcome To x-o Game")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter your Choice(1 or 2) :")
            if choice == "1" or "2":
                break
            print("Please Choose Again")
        return choice

    def display_endgame_menu(self):
        print("Game Over!")
        print("1. Restart The Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter your Choice(1 or 2) :")
            if choice == "1" or "2":
                break
            print("Please Choose Again")
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    # for i in range(1,10):
    #    self.board.append(str(i)) #["1","2",.....,"9"]هيحول الارقام لحروف

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"player{number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            print("-" * 25)

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move ,try again. ")
            except ValueError:
                print("please enter a number between 1 and 9. ")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colums
            [0, 4, 8], [2, 4, 6]  # digonal
        ]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
              return True

        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)  # true

    def quit_game(self):
        print("Thanks For Playing!")


game = Game()
game.start_game()
