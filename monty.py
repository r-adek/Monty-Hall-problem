import random
import pandas as pd
import matplotlib.pyplot as plt

"""
There is a panel with three doors (here generalized to a number >= 3) and behind one of them a prize. The player chooses
a door. But before this door is opened the moderator opens one of the other doors to an empty cell.
The player is then given the opportunity to switch his/her choice to one of the remaining doors. This is entire process 
is repeated as defined by the num_guesses.  A plot is generated for the two options: the player keeps or  
switches the original guessed door.
"""

#options
num_guesses = 1000  # number of repeated rounds of guessing for the prize
num_doors = 20      # maximum number of doors, 3 doors being the minimum


def one_round(switch_on_second_guess, num_doors):
    # this method describes one round of guessing the prize
    # returns the final guessed room number, room number for the prize, True for correctly guessed room
 
    list_rooms = list(range(1, num_doors+1))  # all possible rooms
    room_with_prize = random.choice(list_rooms)  # a random room  to contain the prize
    guess = random.randint(1, num_doors)       # initial guess

    remaining_rooms_0 = list_rooms[:]

    remaining_rooms_0.remove(guess)  # remove initial guess from the all rooms

    remaining_rooms_1 = remaining_rooms_0[:]
    if room_with_prize != guess:
         remaining_rooms_1.remove(room_with_prize)     #all rooms without initial guess and without the prize
    if switch_on_second_guess:
        show_room_without_prize = random.choice(remaining_rooms_1)  # a room that was not selected and does not have a prize
        remaining_rooms_0.remove(show_room_without_prize)  # all rooms but the one that was selected the first time
        guess = random.choice(remaining_rooms_0)
    if guess == room_with_prize:
        return guess, room_with_prize, True
    return guess, room_with_prize, False

def calculate(switch_on_second_guess = True, num_doors = num_doors):
    arr = []
    num_doors_range = range(3, num_doors)
    for j in num_doors_range:
        correct_guesses = 0.0
        for i in range(num_guesses+1):
            guess, prize, correct = one_round(switch_on_second_guess=switch_on_second_guess, num_doors = j)
            if correct:
                correct_guesses += 1.0
        perc = float(correct_guesses)/float(num_guesses)*100.0
        arr.append(perc)
    return(arr)


def main(num_doors=3):
    arr1 = calculate(switch_on_second_guess = True,  num_doors = num_doors)
    arr2 = calculate(switch_on_second_guess = False, num_doors = num_doors)
    arr3 = list(range(3, num_doors))
    df = pd.DataFrame(
        {'rooms': arr3,
        'switching': arr1,
         'keeping': arr2
        })
    df.set_index('rooms', inplace=True)


    plt.interactive(False)
    plt.figure(); df.plot(); plt.title("Monty Hall problem"); plt.ylabel("% correct guess")
    plt.show()

if __name__ == "__main__":
    num_doors = int(input("enter number of doors >= 3 \n ? "))
    while(num_doors < 3):
        num_doors= int(input("the minimum number of doors needs to be >= 3 \n enter again ? "))
    main(num_doors)