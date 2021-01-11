import random

gameList = ['Rock', 'Paper', 'Scissors']

computer = c = 0
player = p = 0
tie = t = 0
print("Score : Computer " + str(c) + " Player " + str(p) + " Tie " + str(t))

while True:
    computer_choice = random.choice(gameList)
    player = input("Rock, Paper, Scissors or Quit: ").capitalize()

    if player == computer:
        print("Tie")
        t += 1
    elif player == "Rock":
        if computer_choice == "Scissors":
            print("Player wins!")
            p += 1
        else:
            print("Computer wins!")
            c += 1    
    elif player == "Paper":
        if computer_choice == "Rock":
            print("Player wins!")  
            p += 1
        else:
            print("Computer wins!")
            c += 1
    elif player == "Scissors":
        if computer_choice == "Paper":
            print("Player wins!")
            p += 1
        else:  
            print("Computer wins!")
            c += 1  
    elif player == "Quit":
        break   
    else:
        print("Wrong selection!")

    if p == 5:
        print("Player won the game!")
        break
    if c == 5:
        print("Computer won the game") 
        break            

    print("Player: " + player)    
    print("Computer: " + computer_choice)
    print("Computer's score: " + str(c) + " | Player's score: " + str(p) + " | Ties: " + str(t))    

