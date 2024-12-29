print("Welcome to rock, paper, scissors game.")
player1= input("Whats the name of the player 1?\n")
player2= input("Whats the name of the player 2?\n")

player1wincount=0
player2wincount=0
inputError=["rock","paper","scissors"]

while(player1wincount-player2wincount !=2 and player2wincount-player1wincount !=2):
    player1choice=input(f"Hi {player1}, rock,paper or scissors?\n").lower().strip()
    player2choice=input(f"Hi {player2}, rock,paper or scissors?\n").lower().strip()

    while(player1choice not in inputError or player2choice not in inputError):
        if(player1choice not in inputError):
            print(player1," has choose a wrong input, please try again.")
            player1choice=input(f"Hi {player1}, rock,paper or scissors?\n").lower().strip()
        else:
            print(player2," has choose a wrong input, please try again.")
            player2choice=input(f"Hi {player2}, rock,paper or scissors?\n").lower().strip()


    if(player1choice =="rock"):
        if(player2choice == "rock"):
            print("It's a draw, go again buddies!")
        elif(player2choice =="paper"):
            print(player2," it's the winner on this round!")
            player2wincount+=1
        else:
            print(player1," it's the winner on this round!")
            player1wincount+=1
    if(player1choice =="paper"):
        if(player2choice  == "paper"):
            print("It's a draw, go again buddies!")
        elif(player2choice =="scissors"):
            print(player2," it's the winner on this round!")
            player2wincount+=1
        else:
            print(player1," it's the winner on this round!")
            player1wincount+=1
    if(player1choice =="scissors"):
        if(player2choice  == "scissors"):
            print("It's a draw, go again buddies!")
        elif(player2choice =="rock"):
            print(player2," it's the winner on this round!")
            player2wincount+=1
        else:
            print(player1," it's the winner on this round!")
            player1wincount+=1

    if(player1wincount-player2wincount == 2):
        print(player1," has win the game!")
    elif(player2wincount-player1wincount==2):
        print(player2," has win the game!")
    else:
        pass