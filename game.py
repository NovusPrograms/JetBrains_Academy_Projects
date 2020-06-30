import random


class ScoreRating:
    def __init__(self, file_name, name):
        self.player_name = name
        self.file_name = file_name
        self.rating_list = []
        self.player_position = 0
        self.player_score = 0

    def start_score(self):
        if self.is_rating_file_exist():
            if self.is_player_on_list():
                self.read_rating_list()
            else:
                self.read_rating_list()
                self.add_new_player()
        else:
            self.make_new_rating_file()
            self.add_new_player()

    def is_rating_file_exist(self):
        try:
            with open(self.file_name, 'r') as _f:
                return True
        except FileNotFoundError:
            return False

    def make_new_rating_file(self):
        with open(self.file_name, 'w') as rating:
            rating.write(" ")

    def is_player_on_list(self):
        with open(self.file_name, 'r') as rating:
            for line in rating:
                if self.player_name in set(line.split()):
                    return True
            return False

    def add_new_player(self):
        self.rating_list.append(f"{self.player_name} {self.player_score}\n")
        self.player_position = len(self.rating_list) - 1

    def read_rating_list(self):
        with open(self.file_name, 'r') as rating:
            for line in rating.readlines():
                self.rating_list.append(line)
                if self.player_name in set(line.split()):
                    self.player_position = len(self.rating_list) - 1
                    self.player_score = int(self.rating_list[self.player_position].split()[1])
            return

    def save_rating_list(self):
        with open(self.file_name, 'w') as rating:
            self.rating_list[self.player_position] = f"{self.player_name} {self.player_score}\n"
            rating.writelines(self.rating_list)


player_name = input('Enter your name: > ')
print("Hello, " + player_name)

deck = input('\nInput your game deck or left empty for standard: >').split()
if not deck:
    deck = ['rock', 'paper', 'scissors']
print("Okay, let's start")

table = ScoreRating('rating.txt', player_name)
table.start_score()

player_chose = input("> ")
while player_chose != "!exit":
    if player_chose == "!rating":
        print(f"Your rating: {table.player_score}")
    elif player_chose in set(deck):
        computer_chose = deck[random.randint(0, len(deck)) - 1]
        if deck.index(computer_chose) - deck.index(player_chose) in set(range(1, int((len(deck) - 1) / 2) + 1)) \
                or deck.index(computer_chose) - deck.index(player_chose) \
                in set(range(-len(deck) + 1, - (int((len(deck) - 2) / 2) + 1))):
            print(f"Sorry, but computer chose {computer_chose}")
        elif deck.index(computer_chose) - deck.index(player_chose) \
                in set(range(int((len(deck) - 1) / 2) + 1, len(deck))) \
                or deck.index(computer_chose) - deck.index(player_chose) \
                in set(range(-(int((len(deck) - 2) / 2) + 1), 0)):
            print(f"Well done. Computer chose {computer_chose} and failed")
            table.player_score += 100
        else:
            print(f"There is a draw {computer_chose}")
            table.player_score += 50
    else:
        print("Invalid input")
    player_chose = input("> ")
table.save_rating_list()
print("Bye!")
