#Lucas Wenger

from random import randint

while True:  
    #Pick number
    number = randint(1,100) 
    #print(number) #Check number - COMMENT OUT
    
    #Pick mode
    mode = ""
    while mode != 'hs' and mode != 'c' and mode != "IMPOSSIBLE" and mode != "ART": #Secret modes!
        mode = input("Would you like to play in High Score Mode or Challenge Mode?\nEnter 'hs' or 'c'.\n")
        #print(mode) #Check mode - COMMENT OUT
        if mode != 'hs' and mode != 'c' and mode != "IMPOSSIBLE" and mode != "ART": #account for unexpected values
            print("Please enter 'hs' or 'c'")
    #Confirm mode chosen to user
    if mode == 'hs':
        print("Launching game in High Score Mode...\n")
    elif mode == 'c':
        #get level of challenge
        level = ""
        while level != '1' and level != '2' and level != '3' and level != 'custom':
            level = input("What level of challenge would you like to face?\nEnter '1', '2', '3', or 'custom'.\n")
            if level != '1' and level != '2' and level != '3' and level != 'custom':
                print("Please enter '1', '2', '3', or 'custom'.\n")
            #Set number of guesses
            elif level == '1':
                maxguesses = 15
            elif level == '2':
                maxguesses = 10
            elif level == '3':
                maxguesses = 5
            elif level == 'custom':
                maxguesses = ""
                while True:
                    maxguesses = input("How many guesses would you like?\nEnter a positive integer.\n")
                    if maxguesses.isdigit() == False:
                        print("Please enter a positive integer. \n")
                        continue
                    else:
                        maxguesses = int(maxguesses)
                        break
                
        #print(level) #Check level - COMMENT OUT
        print("Launching game in Challenge Mode - " + level + "...\n")
    
    #Intro
    print("Welcome to The Guessing Game: The Game Where Heroes Are Made. This is a game made to test your grit and resolve. A number has been chosen. Can you guess it?")
    numguesses = 0
    #hs mode
    guess = ""
    if mode == 'hs':
        while guess != number:
            #get guess
            while True:
                guess = input("Enter a positive integer as a guess:\n")
                if guess.isdigit() == False:
                    print("Please enter a positive integer. \n")
                    continue
                else:
                    guess = int(guess)
                    break
            numguesses += 1
            if guess > number:
                print("Too high! Guess again. You have guessed " + str(numguesses) + " times.")
            if guess < number:
                print("Too low! Guess again. You have guessed " + str(numguesses) + " times.")
        print("You guessed it in " + str(numguesses) + " guesses! Congrats!")
        #storing high score
        try: #if the file exists:
            with open("highscore.txt","r+") as f:
                highscore = f.read()
                #print(highscore) #check high score - COMMENT OUT
            if int(highscore) < numguesses:  #It's called HIGH SCORE MODE for a reason - only the most guesses makes it on the list! :-)
                with open("highscore.txt","w+") as f:
                    f.write(str(numguesses))
                    highscore = numguesses
                print("NEW HIGH SCORE!!!!!")
            else:
                print("The high score is " + str(highscore) + ".")
        except FileNotFoundError: #if the file doesn't exist:
            with open("highscore.txt","w+") as f:
                f.write(str(numguesses))
                highscore = numguesses
            print("NEW HIGH SCORE!!!!!")
        #play again?
        answer = ""
        while answer != "y" and answer != "n":
            answer = input("Would you like to play again? \n 'y' or 'n'.\n")
        if answer == "y":
            continue
        elif answer == "n":
            break
    #c mode
    if mode == "c":
        while guess != number and numguesses < maxguesses:
            #get guess
            while True:
                guess = input("Enter a positive integer as a guess:\n")
                if guess.isdigit() == False:
                    print("Please enter a positive integer. \n")
                    continue
                else:
                    guess = int(guess)
                    break
            numguesses += 1
            if guess > number:
                print("Too high! Guess again. You have guessed " + str(numguesses) + " times.")
            if guess < number:
                print("Too low! Guess again. You have guessed " + str(numguesses) + " times.")
        if guess == number:
            print("You guessed it in " + str(numguesses) + " guesses! Congrats! You had " + str(maxguesses - numguesses) + " guesses left.")
        elif maxguesses == numguesses:
            print("Sorry! You ran out of guesses.")
        #play again?
        answer = ""
        while answer != "y" and answer != "n":
            answer = input("Would you like to play again? \n 'y' or 'n'.\n")
        if answer == "y":
            continue
        elif answer == "n":
            break
    if mode == "IMPOSSIBLE":
        print("You lose.")
        #play again?
        answer = ""
        while answer != "y" and answer != "n":
            answer = input("Would you like to play again? \n 'y' or 'n'.\n")
        if answer == "y":
            continue
        elif answer == "n":
            break
    if mode == "ART":
        print("           ____  ")
        print("         o8%8888,  ")  
        print("       o88%8888888.  ")
        print("      8'-    -:8888b   ")
        print("     8'         8888  ")
        print("    d8.-=. ,==-.:888b  ")
        print("    >8 `~` :`~' d8888   ")
        print("    88         ,88888   ")
        print("    88b. `-~  ':88888  ")
        print("    888b ~==~ .:88888 ")
        print("    88888o--:':::8888   ")   
        print("    `88888| :::' 8888b  ")
        print("    8888^^'       8888b  ")
        print("   d888           ,%888b.  ") 
        print("  d88%            %%%8--'-.  ")
        print(" /88:.__ ,       _%-' ---  -  ")
        print("     '''::===..-'   =  --.  `")
        print("Art by Christopher Johnson")
        print("Original by Leonardo da Vinci")
        #play again?
        answer = ""
        while answer != "y" and answer != "n":
            answer = input("Would you like to play again? \n 'y' or 'n'.\n")
        if answer == "y":
            continue
        elif answer == "n":
            break
