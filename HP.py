from __future__ import print_function
import random
from time import sleep
#to ask the program to "wait" for people to read the instructions properly

enemy = "a"
playerHealth = 100
enemyHealth =100
playerLevel = 1
losechange=20
winchange = 20
firsttime = True
#These variables will be used later on
def hangman():
    #this is the code for the hangman game, and this will run when the code says hangman()
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False
    #these are just variables to ensure the game is reseted and properly started
    words = {'animals':'thestral phoenix niffler bowtruckle fairy dragon hippogriff'.split(),
             'spells': 'lumos filipendo ridikkulus imperio nox duro felifors immobulus expelliarmus'.split(),
             'characters': 'harry hermione ron ginny lupin dumbledore flitwick snape luna nevile bill charlie molly draco'.split(),
             'subjects': 'transfiguration flying charms potions history astronomy divination herbology arithmancy'.split(),
             'houses': 'gryffindor slytherin ravenclaw hufflepuff'.split(),
             'horcruxes': 'ring diary harry nagini cup locket diadem'.split()}
    #this is the vocab that the proram will generate and whcih you will have to guess
    HANGMANPICS = ['''
    
    
    
    
    
    
    
    =========''', '''
    
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    #these are the diagrams that the program will show according to how many mistakes you have made
    alreadyGuessed = ''
    def getRandomWord(words):
        wordKey = random.choice(list(words.keys()))
        number = random.randint(0, len(words[wordKey])-1)
        return [words[wordKey][number], wordKey]
    #this is to get a random word from the list by using the random module we imported and the choices= of category will obviously chose from the list of vocab categories above and the actual word will also be a random number , and why it is (0, len(words[wordkey])-1) is because it can only choose the number from the number of words there are, and as 0 is the first term, the number that will be generated has to be between 0 and the number of words -1 as the len() function will count how many terms there actually are. 
    
    def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
        sleep(1)
        print('The secret word is in the category: ' + secretCategory)
        print(HANGMANPICS[len(missedLetters)])
        print()
        print('Missed letters:', end = " ")
        for letter in missedLetters:
            print(letter, end = " ")
        print()
        #this for loop basically says to print out the missing letters
        blanks = "_" *len(secretWord)
        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                blanks = blanks[:i]+ secretWord[i] + blanks[i+1:]
        #this is to generate how many blanks there are according to the secret word length and the correct letters, as there wont be blanks for the correct letters
        for letter in blanks:
            print(letter, end=" ")
        print()
    #this whole function is here to display the diagrams and the word we have to guess when we run the program
    def getGuess(alreadyGuessed):
        while True:
            guess = raw_input("Guess a letter: ")
            guess = guess.lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif guess in alreadyGuessed:
                print("You have already guessed this letter.")
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("Please enter a letter.")
            else:
                return guess
            
    #this is to store the answer you input in, and checks if the answer is valid or not, and if it is valid, it will be returned and later used in the code
    def playAgain():
        print("Do you want to play again?")
        return raw_input("Press \"y\" if you want to or press any other letter if you don't want to: ").lower().startswith('y')
    #this is to ask sure if you want to play again or not by using a raw input
    
    [secretWord, secretCategory] = getRandomWord(words)
    print("******************************")
    print('H O G W A R T S  H A N G M A N')
    print("******************************")
    sleep(1)
    print("Welcome to our hogwarts-themed hangman game!")
    sleep(1)
    print("If you haven't read Harry Potter, I'm afraid you might not do ")
    sleep(1)
    print("very well in this game. But anyways, let's start!")

    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        guess = getGuess(missedLetters + correctLetters)
        print("Please wait...")
        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            #This only runs if the user inputed a letter that is in the secret Word, and these two lines under the if statement is basically storing the correct answer so that we know the user has already guessed that lettter, and also assuming that the user has found all the letters, which might not be true, but the for loop under will know and if it is not true, the variable will be changed to False. 
            for letter in secretWord:
                if letter not in correctLetters:
                    foundAllLetters = False
                    break
            #this for loop basically checks if the player has entered all the letters in the secret or not by checking if every letter in secretWord is in the correctLetters variable
            if foundAllLetters:
                print('Yes! The secret word was ' + str(secretWord))
                gameIsDone = True
        #This is to show everything out when we run this program, by just putting all the functions we made previously. It prints out the diagrams and also check if we have found a correct letter or not, and if we have found all the letters, it will print yes the secret word was x and as the gamesIsDone variable is true, it will go to the next stage, which is asking if you want to play again or play the other game, or stop the program.
        else:
            missedLetters = missedLetters + guess
            #This happens if the user inputs a wrong guess, and the letter will be stored so we know this letter is already guessed
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print("You have ran out of guesses! \n After")
                print(str(len(missedLetters)) + " missed guesses and")
                print(str(len(correctLetters)) + " correct guesses")
                print("The word was " + secretWord)
                gameIsDone = True
            #this if statement is saying that if you have already guesseed too many times, it will print some stuff and as the gameIsDone variable is true, you will go on the next stage, which is asking if you want to play again or play the other game, or stop the program.
        if gameIsDone == True:
            if playAgain():
                print("Please wait...")
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                [secretWord, secretCategory] = getRandomWord(words)
            else:
                break
            #This if statement is saying that if the user said they want to play again (by using the playAgain function), the game will start over and a new word is picked, and of cours the gameIsDone variable will be False again and the missed and correct letters will be empty
    othergameornot = raw_input("You can also try the other game! Press \"y\" to play: ")
    if othergameornot == "y":
        hogwarts()
    else:
        print("You don't want to play either of them? Oh well... But if you change your mind, please run the program again and try them!")   
    #This is just saying that the player can also try the other game and if they say y, the other game will run and if no, the program will stop
def hogwarts():
    global firsttime
    if firsttime == True :
        print("**************************************")
        sleep(0.5)
        print("Welcome to the hogwarts duelling game!")
        sleep(0.5)
        print("**************************************")
        sleep(0.5)
        
        print("How this game works: ")
        sleep(1)
        print("You will pick a move to fight against your opponent.")
        sleep(1.5)
        print("The moves are Aggressive, Defensive and Sneaky.")
        sleep(1.5)
        print("Your opponent will fight back. If you both choose ")
        sleep(1.5)
        print("the same thing, it will be a draw. The person who")
        sleep(1.5)
        print("has less points will get 2 extra marks. If you choose")
        sleep(1.5)
        print("Aggressive, and if your opponent chooses defensive, ")
        sleep(1.5)
        print("you lose. If your opponent chooses sneaky, you win.")
        sleep(1.5)
        print("If you choose Defensive, and if your opponent chooses")
        sleep(1.5)
        print("Sneaky, you lose. If your opponent chooses Aggressive, ")
        sleep(1.5)
        print("you win. If you choose Sneaky, and if your opponent ")
        sleep(1.5)
        print("chooses aggressive, you lose. If your opponent chooses")
        sleep(1.5)
        s=raw_input("defensive, you win. All set? Let's start! (press s)")
        firsttime = False
        #This part is basically just the intro, and I have set firsttime to False as when you play the next time you don't have to read through all the instructions again
    if s == "s":
        while playerLevel <=3:
            #this means the loop will run until the player has passed all 3 levels, which the computer will record by using a variable
            if playerLevel == 0:
                break  
            print("  ")
            print("What move do you want to choose? A for Aggressive")
            attack=raw_input("D for defensive and S for Sneaky (all caps)")
            #this is how the user move is stored, by using a raw input
            enemyattack()
            #this is a function which I have made earlier in the program, and it basically generates a random move for the enemy
            if attack == "A":
                if enemy == "a":
                    draw()
                elif enemy == "d":
                    lose()
                elif enemy == "s":
                    win()
            elif attack == "D":
                    if enemy == "d":
                        draw()
                    elif enemy == "s":
                        lose()
                    elif enemy == "a":
                        win()
            elif attack == "S": 
                    if enemy == "s":
                        draw()
                    elif enemy == "a":
                        lose()
                    elif enemy == "d":
                        win()
            checkGameOver()
            #This huge loop is basically saying if you enter a, it will generate a random letter (between a, d, and s), and depending on the choices it will determine if you win or not, and same for d and s. This is a while loop, so it will keep running until the playerLevel is 3 and there are no more Levels available.
    else:
        print("Do you want to try again? Don't give up!")
        Starthdg = raw_input("If you want to try again, please input y and if not, press any other letter: ")
        if Starthdg == "y":
            hogwarts()
            Starthdg = ""
            #this is saying that if the player has inputed yes, that he/she wants to play again, the whole hogwarts function will run again. Note that this whole thing is a function
        else:
            print("Aww! You don't want to play this game? Don't worry, we still have another game!")
            Startothergame = raw_input("If you want to play the other game, please input the word game or if not, press any other letter: ")
            if Startothergame == "game":
                hangman()
                Startothergame = "0"
            else:
                print("You don't want to play either of them? Oh well... ")
                print("But if you change your mind, please run the program again and try them!")   
            #this is basically asking the player if he/she wants to play the other game, and if they do, the hangman game will run and if not, the program will stop
def draw():
    global playerHealth
    global enemyHealth
    if playerHealth <= enemyHealth:
        playerHealth = playerHealth +2
    else:
        enemyHealth = enemyHealth+2
    print ("It is a draw! Your Health is ", playerHealth)
    print ("and your opponent\'s health is ", enemyHealth)
#This function explains what happens when there is a draw between the player(input) and the computer (program)
#I have made the variables global because if they weren't the program wouldn't work
#This function basically changes the Health of the player or enemy according to who has the "better health"
#And at the end it prints out the Health
def lose():
    global playerHealth
    global enemyHealth    
    playerHealth = playerHealth-losechange
    print ("You lose! Your health is ", playerHealth)
    print ("and your opponent\'s health is ", enemyHealth)
#This function is similar to Draw, but just that the enemyHealth will be decreased without checking who has the better Health
def win():
    global playerHealth
    global enemyHealth    
    enemyHealth = enemyHealth-winchange
    print ("You win! Your health is ", playerHealth)
    print ("and your opponent\'s health is ", enemyHealth)
#Vice-versa of lose
def enemyattack():
    global enemy
    echoice = ["a", "d", "s"]
    enemy= random.choice(echoice)
#This function generates a move by the computer, which is randomly picked
def checkGameOver():
    global playerLevel
    global playerHealth
    global enemyHealth
    if playerHealth <= 0:
        print ("Game Over! You died!")
        print("Do you want to try again? Don't give up!")
        Starthdg = raw_input("If you want to try again, please input y and if not, press any other letter: ")
        if Starthdg == "y":
            hogwarts()
            Starthdg = ""
            #this is saying that if the player has inputed yes, that he/she wants to play again, the whole hogwarts function will run again. Note that this whole thing is a function    
        else:
            Startothergame = raw_input("If you want to play the other game, please input the word game or if not, press any other letter: ")
            if Startothergame == "game":
                hangman()
                Startothergame = "0"
            else:
                print("You don't want to play the other game? Oh well... ") 
                print("But if you change your mind, please run the program again and try them!")
            playerLevel = 0
    elif enemyHealth <=0:
        if playerLevel <=2:
            print("You have passed this Level!")
            enemyHealth = 150
            playerHealth = 150            
            levelup()
            print("You are now on Level ", playerLevel)
        else:
            print("You win! Congrats!")
            Startothergame = raw_input("If you want to play the other game, please input the word game or if not, press any other letter: ")
            if Startothergame == "game":
                hangman()
                Startothergame = "0"
            else:
                print("You don't want to play the other game? Oh well... But if you change your mind, please run the program again and try them!")             
#This function checks if the game is finished or not, by checking if the playerHealth or the enemyHealth is less than or equal to 0, because if it is, it either says you passed this level or you died (to the player), and also changing the Level variable so that the while loop will stop when it has reached a certain level.
def levelup():
    global playerLevel
    global losechange
    global winchange
    playerLevel = playerLevel +1
    losechange = losechange+20
    winchange = winchange +15
#This function makes the game harder by changing how much your Health is changed when you win/lose (with variables).
print("This is my program. Please wait while the game is loading...")
sleep(2)
print("---------------------")
print("\                   /")
print(" \     |     |     / ")
print("  \    |     |    /  ")
print("   \   -------   /          Brought to you by ")
print("    \  |     |  /          HOGWARTS  GAMES  LAB")
print("     \ |     | /     ")
print("      \       /      ")
print("       \     /       ")
print("        \   /        ")
print("         \ /         ")
print("          -          ")
print("We have 2 games available today! Would you want to play Hogwarts-themed Hangman or Hogwarts duelling game?")
selection = raw_input("Press \"h\" for Hangaman and \"hdg\" for Hogwarts duelling game: ")
if selection == "hdg":
    hogwarts()
elif selection == "h":
    hangman()
#This is the actual code that is not part of a function, and as you can see, it is very short, and the only important thing is that they will run the functions according to what the user inputs, with variables and a if statement
        
            
    
        

