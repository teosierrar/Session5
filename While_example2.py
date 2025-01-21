#Virtual dice game, you win if you roll a 6, you lose 1 life if not
#You have three lives

from random import randint
lives=3
while True:
    dice_roll=randint(1,6)
    if dice_roll==6:
        print("Congrats, you rolled a 6, you win!")
        break
    else:
        lives=lives -1
        print(f"You rolled a {dice_roll}, you lose a life, lives left: {lives}")
        if lives==0:
            print("you lost!")
            break
print("Thanks for playing my game")