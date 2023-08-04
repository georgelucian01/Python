
import random
import time

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


def print_dice(face):

    for art in dice_art[face]:
        print(art)

# Make the dice roll until it hits the right spot
def roll_dice(face):
    
    rolls = [1, 2, 3, 4, 5, 6]
    random.shuffle(rolls)

    
    for roll in rolls:
        print_dice(roll)
        time.sleep(0.5)
        if roll == face:
            break
        



def main(): 
    responses = ['y', 'n']
    wins = 0
    losses = 0
    print()

    while True:
       
        # valid input
        while True:
            response = input("Continue? (y/n): ")
            if response not in responses:
                response = input("Continue? (y/n): ")
            else:
                break

        # check y or n
        if response == 'y':

            # make cpu roll
            cpu = random.randint(1,6)
            roll_dice(cpu)
            print(f"CPU rolled {cpu}")
            time.sleep(1)
            print()

            # roll for player
            player = random.randint(1, 6)
            roll_dice(player)
            print(f"You rolled {player}")
            time.sleep(1)
            print()

            # check win or loss
            if cpu > player:
                print(f"Computer wins! {cpu} > {player}")
                time.sleep(1)
                print()
                losses += 1
            elif player > cpu:
                print(f"You win! {player} > {cpu}")
                time.sleep(1)
                print()
                wins += 1
            else:
                print("Draw")
                time.sleep(1)
                print()
        else:
            break

    # print wins and losses
    print()
    print(f"You won {wins} times")
    time.sleep(0.5)
    print()
    print(f"Computer won {losses} times")
    time.sleep(0.5)
    print()

    time.sleep(0.5)
    if wins > losses:
        print("You won!")
    else:
        print("Computer won!") 
    print()

if __name__ == "__main__":
    main()