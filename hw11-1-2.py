# Kyle Bautista (AMDG) 12/17/20

from random import randint


def rock_paper_scissors():
    player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
    computer = randint(0, 2)
    if player == computer:
        print("It's a tie!")
        return "tie"
    elif player == 0:
        if computer == 1:
            print("You lose, paper covers rock.\n")
            return "loss"
        else:
            print("You win, rock crushes scissors!\n")
            return "win"
    elif player == 1:
        if computer == 2:
            print("You lose, scissors cuts paper.\n")
            return "loss"
        else:
            print("You win, paper covers rock!\n")
            return "win"
    elif player == 2:
        if computer == 0:
            print("You lose, rock crushes scissors.\n")
            return "loss"
        else:
            print("You win, scissors cuts paper!\n")
            return "win"


games = 0
won = 0
lost = 0
tied = 0

while True:
    play = input("Want to play a game of Rock, Paper, or Scissors? Y/N: ")
    if play.upper() == "Y":
        result = rock_paper_scissors()
        if result == "win":
            won += 1
            games += 1
        elif result == "loss":
            lost += 1
            games += 1
        elif result == "tie":
            tied += 1
            games += 1
    elif play.upper() == "N":
        break
    else:
        print("You picked neither")
        continue

print("Your results: {0} game(s), {1} win(s), {2} loss(es), {3} tie(s).".format(games, won, lost, tied))
