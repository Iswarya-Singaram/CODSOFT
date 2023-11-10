import random
options=("rock","paper","scissors")
running=True
while running==True:
        player=None
        computer=random.choice(options)
        while player not in options:
            player=input("Enter Your Choice:")
        print("Computer's Choice:",computer)
        if player==computer:
            print("It's a Tie!")
        elif player=="scissors" and computer=="paper":
            print("You Win!")
        elif player=="rock" and computer=="scissors":
            print("You Win!")
        elif player=="paper" and computer=="rock":
            print("You Win!")
        else:
            print("You Lose!")
        play_again=input("Play again?(y/n):")
        if play_again.lower()!="y":
            running=False
print("Thanks for Playing!")
        
