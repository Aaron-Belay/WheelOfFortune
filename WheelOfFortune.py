import random, time, os, sys #Here are the imported moduals 
from wheel import * # imported from wheel.py
#Greetings 
input("\033[1;39;36mWelcome to Wheel of Fortune (Python Edition)!\033[0;38;36m\nPress Enter to continue >>> ") #Greetings 
time.sleep(0.5) 
os.system('clear')
time.sleep(1)
#Objectives of the game are explained below
print("""\033[1;39;36mOBJECTIVE OF THE GAME\033[0;38;36m
The objective of WHEEL OF FORTUNE \033[0;31;50m(Python Edition)\033[0;38;36m is to earn the most amount of money by spinning the Wheel and
solving a series of word puzzles on the Puzzle Board. 
The player with the most money after \033[0;31;50m1\033[0;38;36m round is the winner. 
You virtually spin the wheel and depending on what you land on, you can get a multiple for each letter you get right.""")
time.sleep(17)
#Intructions explained below
print("""\n\033[1;39;36mTHINGS TO KEEP IN MIND\033[0;38;36m
- There are \033[0;31;50m3\033[0;38;36m contestants in which YOU get to decide the order 
- The player must spin the wheel and guess a consanant 
- Vowels must be bought with at least \033[0;31;50m$250\033[0;38;36m 
- All categories are related to charaters from childhood movies, books, and TV series
- Possible spin outcomes include: Bankrupt, Vacations, Skip Turn, Cars, etc.  """) 
time.sleep (23) #time.sleep allows the print statment to appear in specified intervals 
print("""\n\033[1;39;36mTHINGS YOU MUST KNOW BEFORE PLAYING\033[0;38;36m
As this is a condensed version of the famous Wheel Of Fortune, there are some things that are different, like "solving the puzzle"
In the case that a player has no money to buy a vowel and the only letters left are vowels, you are to use the \033[0;31;50mdababy\033[0;38;36m card. You must use it as told...
  - When asked to guess a letter, type in \033[0;31;50mdababy\033[0;38;36m and press enter
  - Then, guess the vowel. This elite maneuver bypasses the code and will leave you screaming "LETS GO"  
Like in the real game, slots can be removed after being used and serve as a different prize or forfeit. 
In our case, after a prize slot (Car or Fiji) has been used, it will turn into a "Free to Play" slot
  - The new slot will allow you to guess a letter but will not give you a prize for getting a letter right. 
  - Keep in mind that you can still get it incorrect, and lose your turn!
""")
    
time.sleep (36) #time.sleep allows the print statment to appear in specified intervals 
print("""\033[1;39;36mMOST IMPORTANTLY, HAVE FUN!\033[0;38;36m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
time.sleep (4)
input("Press Enter To Continue\n>>>")
os.system('clear')

#game function
def game(): 
  
  p1s = 0 #money score
  p1p = [] #prize score 
  p2s = 0 #money score
  p2p = [] #prize score
  p3s = 0 #money score
  p3p = [] #prize score

#Here is the Gut function. The global syntax allows the scores to apply to all other funtiosn
  def guts():
    global p1s 
    global p2s
    global p3s
    global p1p
    global p2p 
    global p3p
      
    p1s = 0 #money score
    p1p = [] #prize score 
    p2s = 0 #money score
    p2p = [] #prize score
    p3s = 0 #money score
    p3p = [] #prize score

    #Here the program greets the players as well as compile their names 
    print("\033[1;39;36mWELCOME TO MULTIPLAYER MODE\033[0;38;36m")
    time.sleep(2.5)
    print("\nBefore We Start, I Need All \033[0;31;50m3\033[0;38;36m Of Your Names.")
    time.sleep(1)
    p1name = input("\n\033[0;31;50mP1\033[0;38;36m, What's Your Name? \n>>>\033[1;34m ") #name for player1
    time.sleep(0.8)
    print("\033[0;38;36mThank You!") 
    time.sleep(0.8)
    p2name = input("\n\033[0;31;50mP2\033[0;38;36m, What's Your Name? \n>>>\033[1;34m ") #name for player2
    time.sleep(0.8)
    print("\033[0;38;36mThank You!")
    time.sleep(0.8)
    p3name = input("\n\033[0;31;50mP3\033[0;38;36m, What's Your Name? \n>>>\033[1;34m ")#name for player3
    time.sleep(0.8)
    print("\033[0;38;36mThank You!")
    time.sleep(1.5)
    print("\n\033[3mWe May Now Begin...\033[0;38;36m")
    time.sleep(2)
    os.system('clear')
    time.sleep(1)
    print("\033[1;39;36mWHEEL OF FORTUNE\033[0;38;36m - \033[1;39;36mMULTIPLAYER\033[0;38;36m") #Second greetings 
    time.sleep(1)

    #Here is where the Wheel is displayed. 
    print("""

                           ▄▄▄▄
                          █ || █ 
                          █ || █
                         ▄▄█\/█▄▄
                     ▄█▀▀▄  ▀▀  ▄▀▀█▄
                   ▄█    █ $800 █    █▄                 
                   █▄ $700▐    ▌$6969▄█
                  █  ▀▀▄   █  █   ▄▀▀  █
                 █ BANK ▀▀▄▄██▄▄▀▀ FIJI █
                ▐█▄▄▄▄▄▄▄████████▄▄▄▄▄▄▄█▌
                ▐█▀▀▀▀▀▀▀████████▀▀▀▀▀▀▀█▌
                 █ $500 ▄▄▀▀██▀▀▄▄ SKIP █
                  █  ▄▄▀   █  █   ▀▄▄  █
                   █▀ $400▐    ▌ CAR ▀█
                   ▀█    █$5000 █    █▀
                     ▀█▄▄▀      ▀▄▄█▀
                         ▀▀████▀▀
    """)

    def output(phrase): #function which identifies letter choosen and replaces it with phrase 
        message = ''
        for letter in phrase: 
            message += letter
            message += " "
        print(message) 



    w = random.randint(0,27) #range for the index within the lists containing phrases  


    # ~~List section 1 ~~ this section of list displays the lines where the user must guess a letter 
    p1 = ['_','_','_','_','_','_',' ','_','_','_',' ','_','_','_','_','_','_',' ','_','_','_','_']
    p2 = ['_','_','_','_','_','_',' ','_','_','_',' ','_','_','_','_','_','_',' ','_','_','_']
    p3 = ['_','_','_','_',' ','_','_','_','_','_',' ','_','_','_','_','_','_','_','_']
    p4 = ['_','_','_',' ','_','_','_','_',' ','_','_','_','_','_','_']
    p5 = ['_','_','_',' ','_','_','_',' ','_','_',' ','_','_','_',' ','_','_','_','_']
    p6 = ['_','_','_','_',' ','_','_','_',' ','_','_','_']
    p7 = ['_','_','_','_','_','_','_','_','_']
    p8 = ['_','_','_','_','_',' ','_','_','_','_',' ','_','_',' ','_','_','_',' ','_','_','_','_','_','_','_','_','_'] 
    p9 = ['_','_','_','_','_',' ','_','_','_','_','_','_']
    p10 = ['_','_','_',' ','_','_','_','_','_']
    p11 = ['_','_','_','_',' ','_','_','_','_','_']
    p12 = ['_','_','_','_','_',' ','_','_','_','_','_','_','_']
    p13 = ['_','_','_','_','_',' ','_','_','_','_']
    p14 = ['_','_','_','_','_',' ','_','_','_','_']
    p15 = ['_','_','_','_','_','_','_','_','_','_','_',' ','_','_','_','_']
    p16 = ['_','_','_','_','_','_','_',' ','_','_','_','_','_']
    p17 = ['_','_','_','_',' ','_','_','_','_','_','_','_']
    p18 = ['_','_','_','_',' ','_','_',' ','_','_','_','_','_','_']
    p19 = ['_','_','_','_','_','_',' ','_','_','_','_','_']
    p20 = ['_','_','_','_','_',' ','_','_','_','_']
    p21 = ['_','_','_','_',' ','_','_',' ','_','_','_','_','_','_']
    p22 = ['_','_','_','_',' ','_','_','_','_']
    p23 = ['_','_','_','_','_',' ','_','_','_']
    p24 = ['_','_','_','_','_','_','_','_','_','_']
    p25 = ['_','_','_',' ','_','_','_',' ','_','_','_','_','_','_']
    p26 = ['_','_','_',' ','_','_','_','_','_','_','_',' ','_','_',' ','_','_','_','_','_','_','_','_','_','_']
    p27 = ['_','_','_',' ','_','_','_','_','_','_',' ','_','_','_','_','_','_']
    p28 = ['_','_','_','_','_','_','_','_',' ','_','_','_']

    #list containing all lists in section 1
    phrase = [p1, p2, p3, p4 ,p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,p21, p22, p23, p24, p25, p26, p27, p28] 


    choice_p = phrase[w] #varible which randomly selects a list from section 1

    # ~~List section 2 ~~ this section of list are the actual answer sections 1 blacnk list 
    w1 = ['L','I','T','T','L','E',' ','R','E','D',' ','R','I','D','I','N','G',' ','H','O','O','D']
    w2 = ['P','O','P','E','Y','E',' ','T','H','E',' ','S','A','I','L','O','R',' ','M','A','N']
    w3 = ['S','N','O','W',' ','W','H','I','T','E',' ','P','R','I','N','C','E','S','S']
    w4 = ['T','H','E',' ','F','R','O','G',' ','P','R','I','N','C','E']
    w5 = ['T','H','E',' ','M','A','N',' ','I','N',' ','T','H','E',' ','M','O','O','N']
    w6 = ['W','I','S','E',' ','O','L','D',' ','O','W','L']
    w7 = ['A','P','H','R','O','D','I','T','E']
    w8 = ['B','A','B','A','R',' ','K','I','N','G',' ','O','F',' ','T','H','E',' ','E','L','E','P','H','A','N','T','S']
    w9 = ['B','E','T','T','Y',' ','R','U','B','B','L','E']
    w10 = ['T','H','E',' ','F','L','A','S','H']
    w11 = ['B','U','G','S',' ','B','U','N','N','Y']
    w12 = ['C','O','U','N','T',' ','D','R','A','C','U','L','A',]
    w13 = ['D','A','F','F','Y',' ','D','U','C','K']
    w14 = ['E','L','M','E','R',' ','F','U','D','D']
    w15 = ['H','U','C','K','L','E','B','E','R','R','Y',' ','F','I','N','N']
    w16 = ['I','N','D','I','A','N','A',' ','J','O','N','E','S']
    w17 = ['L','A','D','Y',' ','M','A','C','B','E','T','H']
    w18 = ['J','A','C','K',' ','B','E',' ','N','I','M','B','L','E']
    w19 = ['M','O','T','H','E','R',' ','G','O','O','S','E']
    w20 = ['N','A','N','C','Y',' ','D','R','E','W']
    w21 = ['J','A','C','K',' ','B','E',' ','N','I','M','B','L','E']
    w22 = ['P','A','P','A',' ','B','E','A','R']
    w23 = ['O','L','I','V','E',' ','O','Y','L']
    w24 = ['P','O','C','A','H','O','N','T','A','S']
    w25 = ['R','I','P',' ','V','A','N',' ','W','I','N','K','L','E']
    w26 = ['T','H','E',' ','S','H','E','R','I','F','F',' ','O','F',' ','N','O','T','T','I','N','G','H','A','M']
    w27 = ['W','E','E',' ','W','I','L','L','I','E',' ','W','I','N','K','I','E']
    w28 = ['Y','O','S','E','M','I','T','E',' ','S','A','M']

    words = [w1, w2, w3, w4 ,w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, w26, w27, w28] #list containing all lists in section 2

    choice_w = words[w] #varible which randomly selects a list from section 2

    #The function for player1 
    def player1():  
      #applys score      
      global p1s 
      global p2s
      global p3s
      global p1p
      global p2p 
      global p3p

      #If words do not equal phrase i.e, the phrase is not fully complete 
      if words[w] != phrase[w]:  
        # ~~List section 3 ~~ this section Contains the slots which is randomly allotted to the user
        wheel = ["$400","$500","$700","$800","$5000","6969","Trip to FIJI", "Car","Skip","Bankrupt",]
            
        #Once user clicks a random wheel will print
        spin = input("\n\033[1;34m%s\033[0;38;36m, Click \033[1;39;36mEnter\033[0;38;36m To Spin The Wheel: " % p1name) 
        time.sleep(1) #small break 
        os.system('clear') #clears the shell


        x = random.randint(0,9) #range for wheel list

        #Here is the function that spins the wheel. function is defined in wheel.py file. 

        #Here is the function that spins the wheel. function is defined in wheel.py file.
        def wheelspin():
          if wheel[x] == wheel[0]: 
            wheelspin400() 
          elif wheel[x] == wheel[1]:
            wheelspin500()
          elif wheel[x] == wheel[2]:
            wheelspin700()
          elif wheel[x] == wheel[3]:
            wheelspin800()
          elif wheel[x] == wheel[4]:
            wheelspin5000()
          elif wheel[x] == wheel[5]:
            wheelspin6969()
          elif wheel[x] == wheel[6]:
            wheelspinFIJI()
          elif wheel[x] == wheel[7]:
            wheelspinCAR()
          elif wheel[x] == wheel[8]:
            wheelspinSKIP()
          elif wheel[x] == wheel[9]:
            wheelspinBANK()

        wheelspin() #prints the wheel 

        # ~~List section 4 ~~ this section divides the wheel into three parts, each part leads to a different statement 
        money = [wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], wheel[5]]
        prize = [wheel[6], wheel[7]]
        forfeit = [wheel[8], wheel[9]]
        
        wheels = [400,500,700,800,5000,6969] #A List containing numbers that equates to wheel value 

        #converts wheel value into numbers 
        if wheel[x] == wheel[0]:
          wheels [0]
        elif wheel[x] == wheel[1]:
          wheels[1]
        elif wheel[x] == wheel[2]:
          wheels[2]
        elif wheel[x] == wheel[3]:
          wheels[3]
        elif wheel[x] == wheel[4]:
          wheels[4]
        elif wheel[x] == wheel[5]:
          wheels[5]


        #Contains the last two elements of the wheel list 
        wheelp = ["Car","Trip to FIJI"]   

        #Takes wheel value for the last two elements and replaces it in wheelp 
        if wheel[x] == wheel[6]:
          wheelp[0]
        elif wheel[x] == wheel[7]:
          wheelp[1]

        #List containing all the consonanst in the alphabets  
        letters = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

        #Lists containing all the vowels in the alphabets 
        vowels = ['A','E','I','O','U',]


        time.sleep(1) #pause
        

        y = random.randint(0,5) #range for phrase list

        if wheel[x] in money or prize or forfeit: 
        #this if statement should count for money and prizes
          while words[w] != phrase[w] and wheel[x] not in forfeit: 
            print("Spun = ", end = '\033[1;33m') #prints spin
            print(wheel[x], end = '\033[0;38;36m') #prints the random wheel slot 

            #prints the random phrase from list 1 
            print("\n\nPhrase = ", end = ' ') 
            time.sleep(1.5)  
            output(phrase[w]) #outputs phrase      
            time.sleep(1)
            
            #Keeps track of player ones score
            print("\n\033[1;34m%s\033[0;38;36m, You Have \033[1;33m$%d\033[0;38;36m And Your Prizes Include: %s " %(p1name, p1s,p1p))
            guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ") #User gets to input a letter  

            guess = guess.upper() #This module allows the guess to be both lowercase and uppercase 
            
            #While loop if player1's score is less than $250 and they choose to guess a vowel  
            while guess in vowels and p1s <= 249: 
              print("\nYou Need At Least \033[1;33m$250\033[0;38;36m For A Vowel!")
              print("Try Again.")
              output(phrase[w])
              guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ")
              guess = guess.upper()
            if guess in vowels:
              if p1s > 0:
                p1s -= 250      
              if p1s < 0:
                p1s = 0  


            #while loop here checks if the letter guessed was already used in the letter list
            while guess not in letters and guess not in vowels: 
              print("\nThe Letter Has Already Been Used!") #
              print("Please Try Again.")
              output(phrase[w]) #output phrase
              guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ")
              guess = guess.upper() #allows for lowercase inputs 
            #If guess is a letter in the list
            if guess in letters:
              #pops letter used from letter list 
              indl = letters.index(guess) 
              letters.pop(indl)
            # if guess is a letter from the vowel list
            elif guess in vowels: 
              #pops letter used in vowel list
              indv = vowels.index(guess)
              vowels.pop(indv)

            # if guess matches a letter insdie the choice_w list 
            if guess in choice_w: 
              for i in range(len(choice_w)): #i is the number of elements inside the random choice_w list 
                if choice_w[i] == guess: #if choice is equivalent to guess
                  choice_p[i] = guess #Here is where we assign guess to the empty underlined phrase
                  #if slot is a prize
                  if wheel[x] in prize and wheel[x] not in p1p: 
                    p1p.append(wheel[x]) #append wheel[x] (prize slot) to p1p which keeps track of prize 
                  #Adds slot number as score if the random slot is money 
                  if guess not in ['A','E','I','O','U'] and wheel[x] not in prize: 
                    p1s += wheels[x] 


              output(phrase[w]) #out outs updated phrase 
              time.sleep(2) 
              #keeps track of score for player1
              print("\n\033[1;39;36mCORRECT!\033[0;38;36m") #if correct 
              time.sleep(1)                 
              print("\nYour Total Is Now \033[1;33m$%d\033[0;38;36m And Your Prizes Include: %s" % (p1s,p1p))
              time.sleep(2)
            #if incorrect the program move to player2
            else: 
                print("\nSorry \033[1;34m%s\033[0;38;36m, But That Is \033[0;31;50mIncorrect!\033[0;38;36m" % p1name)
                time.sleep(2) 
                print("\nYou're Total Remains \033[0;38;36m$%d\033[0;38;36m and your prizes are still: %s" % (p1s,p1p))
                time.sleep(2)
                print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p2name)
                time.sleep(2)
                player2() #player2 function
                break  
            
            if words[w] != phrase[w]: #if the empty phrase is not complete the user can spin again so long as they previously gueseed correctly
              spin = input("\nCLICK \033[1;39;36mENTER\033[0;38;36m TO SPIN: ") 
              time.sleep(1)
              os.system('clear') #clears shell 
              x = random.randint(0,9) #range for wheel list and all section 2 lists
              wheelspin()
          

          #If wheel[x] (random slot) is a skip the program goes to player2
          if wheel[x] == forfeit[0] and words[w] != phrase[w]:
            #keeps track of score of all players score
            print("\nSorry \033[1;34m%s\033[0;38;36m , But Your Turn Has Been \033[0;31;50mSKIPPED!\033[0;38;36m" % p1name) 
            time.sleep(2)   
            print("\nYour Total Is Still \033[0;38;36m$%d\033[0;38;36m And Your Prizes Include: %s" % (p1s,p1p))
            time.sleep(3)
            print("\n\033[1;34m%s's\033[0;38;36m  Total is \033[0;38;36m$%d\033[0;38;36m And Their Prizes Include: %s" % (p2name,p2s,p2p))
            time.sleep(3)
            print("\n\033[1;34m%s's\033[0;38;36m  Total is \033[0;38;36m$%d\033[0;38;36m And Their Prizes Include: %s" % (p3name,p3s,p3p))  
            time.sleep(3)
            print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p2name)  
            time.sleep(2)
            player2() #player2 function 

          #If wheel[x] (random slot) is a bankrupt the program goes erases their score and goes on to player2
          elif wheel[x] == forfeit[1] and words[w] != phrase[w]:
              time.sleep(1)
              #keeps track of score of all players
              print("\n\033[0;31;50mBANKRUPT!\033[0;38;36m YOU LOSE ALL YOUR MONEY")
              p1s = 0 #assigns new money score
              p1p = [] #assings new prize score
              print("\nYour Total Is Now $%d And You Lost All Of Your Prizes!" % (p1s))
              time.sleep(2)
              print("\n\033[1;34m%s's\033[0;38;36m Total is $%d And Their Prizes Include: %s" % (p2name,p2s,p2p))
              time.sleep(2)
              print("\n\033[1;34m%s's\033[0;38;36m Total is $%d And Their Prizes Include: %s" % (p3name,p3s,p3p))  
              time.sleep(2)
              print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p2name) 
              time.sleep(2)
              player2() #player2 function    

    def player2():
      #maintains value from player1 function    
      global p1s 
      global p2s
      global p3s
      global p1p
      global p2p 
      global p3p
      if words[w] != phrase[w]:
        # ~~List section 1 ~~ this section Contains the slots which is randomly allotted to the user
        wheel = ["$400","$500","$700","$800","$5000","6969","Trip to FIJI", "Car","Skip","Bankrupt",]

        #Once user clicks a random wheel will print
        spin = input("\n\033[1;34m%s\033[0;38;36m, Click \033[1;39;36mEnter\033[0;38;36m To Spin The Wheel: " % p2name) 
        time.sleep(1)
        os.system('clear')
                                  

        #variable in random randint
        x = random.randint(0,9) #range for wheel list and all section 2 lists
      

        #Here is the function that spins the wheel. function is defined in wheel.py file. 
        def wheelspin():
          if wheel[x] == wheel[0]:
            wheelspin400()
          elif wheel[x] == wheel[1]:
            wheelspin500()
          elif wheel[x] == wheel[2]:
            wheelspin700()
          elif wheel[x] == wheel[3]:
            wheelspin800()
          elif wheel[x] == wheel[4]:
            wheelspin5000()
          elif wheel[x] == wheel[5]:
            wheelspin6969()
          elif wheel[x] == wheel[6]:
            wheelspinFIJI()
          elif wheel[x] == wheel[7]:
            wheelspinCAR()
          elif wheel[x] == wheel[8]:
            wheelspinSKIP()
          elif wheel[x] == wheel[9]:
            wheelspinBANK()

        wheelspin()

        # ~~ List section 2 ~~ this section divides the wheel into three parts,each part leads to a different statement 
        money = [wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], wheel[5]]
        prize = [wheel[6], wheel[7]]
        forfeit = [wheel[8], wheel[9]]

     
        wheels = [400,500,700,800,5000,6969] #A List containing numbers that equates to wheel value 
        
        #converts wheel value into numbers 
        if wheel[x] == wheel[0]:
          wheels [0]
        elif wheel[x] == wheel[1]:
          wheels[1]
        elif wheel[x] == wheel[2]:
          wheels[2]
        elif wheel[x] == wheel[3]:
          wheels[3]
        elif wheel[x] == wheel[4]:
          wheels[4]
        elif wheel[x] == wheel[5]:
          wheels[5]
        
        #Contains the last two elements of the wheel list 
        wheelp = ["Car","Trip to FIJI"]   

      
        #Takes wheel value for the last two elements and replaces it in wheelp
        if wheel[x] == wheel[6]:
          wheelp[0]
        elif wheel[x] == wheel[7]:
          wheelp[1]
        
        #List containing all the consonanst in the alphabet
        letters = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

        #Lists containing all the vowels in the alphabet 
        vowels = ['A','E','I','O','U',]
        time.sleep(1) #pause
        y = random.randint(0,5) #range for phrase list

        if wheel[x] in money or prize or forfeit: #If the slot lands on money prize or forfeits 
        #this if statement should count for money and prizes
          while words[w] != phrase[w] and wheel[x] not in forfeit:
            print("Spun = ", end = '\033[1;33m') #prints spin
            print(wheel[x], end = '\033[0;38;36m') #prints the random wheel slot 

            #prints the random phrase from list 1 
            print("\n\nPhrase = ", end = ' ')
            time.sleep(1.5)  
            output(phrase[w]) #outputs phrase
            time.sleep(1)

            #Keeps track of player ones score
            print("\n\033[1;34m%s\033[0;38;36m, You Have \033[1;33m$%d\033[0;38;36m And Your Prizes Include: %s " %(p2name, p2s,p2p))
            guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ") #User gets to input a letter 

            guess = guess.upper() #This module allows the guess to be both lowercase and uppercase

            #While loop if player1's score is less than $250 and they choose to guess a vowel  
            while guess in vowels and p2s <= 249:
              print("\nYou Need At Least \033[1;33m$250\033[0;38;36m For A Vowel!")
              print("Try Again.")
              output(phrase[w]) #outputs phrase
              guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ")
              guess = guess.upper() #allows for both uppercase and lowercase
            #if the guess is inside the vowel then $250 is subtracted from user score
            if guess in vowels: 
              if p2s > 0:
                p2s -= 250      
              if p2s < 0:
                p2s = 0 


           #while loop here checks if the letter guessed was already used in the letter list
            while guess not in letters and guess not in vowels:
              print("\nThe Letter Has Already Been Used!")
              print("Please Try Again.")
              output(phrase[w]) #output phrase
              guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ")
              guess = guess.upper() #allows for lowercase inputs 
            #If guess is a letter in the list
            if guess in letters:
              #pops letter used from letter list 
              indl = letters.index(guess)
              letters.pop(indl)
              
            # if guess is a letter from the vowel list
            elif guess in vowels:
              #pops letter used in vowel list
              indv = vowels.index(guess)
              vowels.pop(indv)

             # if guess matches a letter insdie the choice_w list 
            if guess in choice_w:
              for i in range(len(choice_w)): #i is the number of elements inside the random choice_w list 
                if choice_w[i] == guess: #if choice is equivalent to guess
                  choice_p[i] = guess #Here is where we assign guess to the empty underlined phrase
                  #if slot is a prize
                  if wheel[x] in prize and wheel[x] not in p2p: 
                    p2p.append(wheel[x]) #append wheel[x] (prize slot) to p1p which keeps track of prize    
                  #Adds slot number as score if the random slot is money      
                  if guess not in ['A','E','I','O','U'] and wheel[x] not in prize:
                    p2s += wheels[x]  


              output(phrase[w]) #output with updated phrase 
              time.sleep(2) 
              #keeps track of score for player2
              print("\n\033[1;39;36mCORRECT!\033[0;38;36m")  
              time.sleep(1)                 
              print("\nYour Total Is Now \033[1;33m$%d\033[0;38;36m And Your Prizes Include: %s" % (p2s,p2p))
              time.sleep(2)
            #if incorrect the program move to player3
            else:
                print("\nSorry \033[1;34m%s\033[0;38;36m , But That Is \033[0;31;50mIncorrect!\033[0;38;36m" % p2name)
                time.sleep(2) 
                print("\nYou're Total Remains \033[0;38;36m$%d\033[0;38;36m and your prizes are still: %s" % (p2s,p2p))
                time.sleep(2)
                print("\nNow, on to \033[1;34m%s\033[0;38;36m " % p3name)
                time.sleep(2)
                player3() #player3 function
                break  


            if words[w] != phrase[w]:#if the empty phrase is not complete the user can spin again so long as they previously gueseed correctly
              spin = input("\nCLICK \033[1;39;36mENTER\033[0;38;36m TO SPIN: ") 
              time.sleep(1)
              os.system('clear') #clears shell 
              x = random.randint(0,9) #range for wheel list and all section 2 lists
              wheelspin()
              print("\n") 
            
            

          #If wheel[x] (random slot) is a skip the program goes to player3
          if wheel[x] == forfeit[0] and words[w] != phrase[w]:
            #keeps track of score of all players score
            print("\nSorry \033[1;34m%s\033[0;38;36m, But Your Turn Has Been \033[0;31;50mSKIPPED!\033[0;38;36m" % p2name) 
            time.sleep(2)   
            print("\nYour Total Is Still \033[0;38;36m$%d\033[0;38;36m And Your Prizes Include: %s" % (p2s,p2p))
            time.sleep(3)
            print("\n\033[1;34m%s's\033[0;38;36m Total is \033[0;38;36m$%d\033[0;38;36m And Their Prizes Include: %s" % (p1name,p1s,p1p))
            time.sleep(3)
            print("\n\033[1;34m%s's\033[0;38;36m Total is \033[0;38;36m$%d\033[0;38;36m And Their Prizes Include: %s" % (p3name,p3s,p3p))  
            time.sleep(3)
            print("\nNow, on to \033[1;34m%s\033[0;38;36m " % p3name)  
            time.sleep(2)
            player3() #player3 function 

          #If wheel[x] (random slot) is a bankrupt the program goes erases their score and goes on to player2
          elif wheel[x] == forfeit[1] and words[w] != phrase[w]:
              time.sleep(1)
              #keeps track of score of all players
              print("\n\033[0;31;50mBANKRUPT!\033[0;38;36m YOU LOSE ALL YOUR MONEY")
              p2s = 0 #assigns new money score
              p2p = [] #assings new prize score
              print("\nYour Total Is Now $%d And You Lost All Of Your Prizes!" % (p2s))
              time.sleep(2)
              print("\n\033[1;34m%s's\033[0;38;36m Total is $%d And Their Prizes Include: %s" % (p1name,p1s,p1p))
              time.sleep(2)
              print("\n\033[1;34m%s's\033[0;38;36m Total is $%d And Their Prizes Include: %s" % (p3name,p3s,p3p))  
              time.sleep(2)
              print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p3name) 
              time.sleep(2)
              player3() #player2 function 

    def player3(): 
      #maintains value from player2 function 
      global p1s
      global p2s
      global p3s
      global p1p
      global p2p 
      global p3p
      if words[w] != phrase[w]:
        # ~~List section 1 ~~ this section Contains the slots which is randomly allotted to the user
        wheel = ["$400","$500","$700","$800","$5000","6969","Trip to FIJI", "Car","Skip","Bankrupt",]

        #Once user clicks a random wheel will print
        spin = input("\n\033[1;34m%s\033[0;38;36m, Click \033[1;39;36mEnter\033[0;38;36m To Spin The Wheel: " % p3name) 
        time.sleep(1)
        os.system('clear')
                                  

        #variable in random randint
        x = random.randint(0,9) #range for wheel list and all section 2 lists
        

        #Here is the function that spins the wheel. function is defined in wheel.py file. 
        def wheelspin():
          if wheel[x] == wheel[0]:
            wheelspin400()
          elif wheel[x] == wheel[1]:
            wheelspin500()
          elif wheel[x] == wheel[2]:
            wheelspin700()
          elif wheel[x] == wheel[3]:
            wheelspin800()
          elif wheel[x] == wheel[4]:
            wheelspin5000()
          elif wheel[x] == wheel[5]:
            wheelspin6969()
          elif wheel[x] == wheel[6]:
            wheelspinFIJI()
          elif wheel[x] == wheel[7]:
            wheelspinCAR()
          elif wheel[x] == wheel[8]:
            wheelspinSKIP()
          elif wheel[x] == wheel[9]:
            wheelspinBANK()

        wheelspin()

        # ~~List section 2 ~~ this section divies the wheel into three parts, each part leads to a different statement 
        money = [wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], wheel[5]]
        prize = [wheel[6], wheel[7]]
        forfeit = [wheel[8], wheel[9]]

        
        wheels = [400,500,700,800,5000,6969] #A List containing numbers that equates to wheel value 

        #converts wheel value into numbers 
        if wheel[x] == wheel[0]:
          wheels [0]
        elif wheel[x] == wheel[1]:
          wheels[1]
        elif wheel[x] == wheel[2]:
          wheels[2]
        elif wheel[x] == wheel[3]:
          wheels[3]
        elif wheel[x] == wheel[4]:
          wheels[4]
        elif wheel[x] == wheel[5]:
          wheels[5]

        #Contains the last two elements of the wheel list 
        wheelp = ["Car","Trip to FIJI"]   

        #Takes wheel value for the last two elements and replaces it in wheelp
        if wheel[x] == wheel[6]:
          wheelp[0]
        elif wheel[x] == wheel[7]:
          wheelp[1]

        #List containing all the consonanst in the alphabets
        letters = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

        #Lists containing all the vowels in the alphabets 
        vowels = ['A','E','I','O','U',]

        time.sleep(1) #pause

        y = random.randint(0,5) #range for phrase list
        time.sleep(2)

        if wheel[x] in money or prize or forfeit: #If the slot lands on money prize or forfeits 
        #this if statement should count for money and prizes
          while words[w] != phrase[w] and wheel[x] not in forfeit:
            print("Spun = ", end = '\033[1;33m') #prints spin
            print(wheel[x], end = '\033[0;38;36m') #prints the random wheel 

            #prints the random phrase from list 1 
            print("\n\nPhrase = ", end = ' ')
            time.sleep(1.5)  
            output(phrase[w]) #outputs phrase     
            time.sleep(1)
          
            #Keeps track of player ones prize
            print("\n\033[1;34m%s\033[0;38;36m, You Have \033[1;33m$%d\033[0;38;36m And Your Prizes Include: %s " %(p3name, p3s,p3p))
            guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ") #User gets to input a letter 

            guess = guess.upper() #This module allows the guess to be both lowercase and uppercase

            #While loop if player1's score is less than $250 and they choose to guess a vowel  
            while guess in vowels and p3s <= 249:
              print("\nYou Need At Least \033[1;33m$250\033[0;38;36m For A Vowel!")
              print("Try Again.")
              output(phrase[w]) #outputs phrase
              guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ")
              guess = guess.upper() #allows for both uppercase and lowercase
            #if the guess is inside the vowel then $250 is subtracted from user score
            if guess in vowels:
              if p3s > 0:
                p3s -= 250      
              if p3s < 0:
                p3s = 0  


           #while loop here checks if the letter guessed was already used in the letter list
            while guess not in letters and guess not in vowels:
              print("\nThe Letter Has Already Been Used!")
              print("Please Try Again.")
              output(phrase[w]) #output phrase
              guess = input ("\n\033[1;33mGUESS\033[0;38;36m >>> ")
              guess = guess.upper() #allows for lowercase inputs 
            #If guess is a letter in the list
            if guess in letters:
              #pops letter used from letter list 
              indl = letters.index(guess)
              letters.pop(indl)
            
            # if guess is a letter from the vowel list
            elif guess in vowels:
              #pops letter used in vowel list
              indv = vowels.index(guess)
              vowels.pop(indv)

            # if guess matches a letter insdie the choice_w list 
            if guess in choice_w:
              for i in range(len(choice_w)):#i is the number of elements inside the random choice_w list 
                if choice_w[i] == guess: #if choice is equivalent to guess
                  choice_p[i] = guess #Here is where we assign guess to the empty underlined phrase
                  #if slot is a prize
                  if wheel[x] in prize and wheel[x] not in p3p: 
                    p3p.append(wheel[x]) #append wheel[x] (prize slot) to p1p which keeps track of prize 
                  #Adds slot number as score if the random slot is money
                  if guess not in ['A','E','I','O','U'] and wheel[x] not in prize:
                    p3s += wheels[x]   


              output(phrase[w]) #output with updated phrase
              time.sleep(2) 
              #keeps track of score for player3
              print("\n\033[1;39;36mCORRECT!\033[0;38;36m")  
              time.sleep(1)                 
              print("\nYour Total Is Now \033[1;33m$%d\033[0;38;36m And Your Prizes Include: %s" % (p3s,p3p))
              time.sleep(2)
            #if incorrect the program move to player1
            else:
                print("\nSorry \033[1;34m%s\033[0;38;36m, But That Is \033[0;31;50mIncorrect!\033[0;38;36m" % p3name)
                time.sleep(2) 
                print("\nYou're Total Remains \033[0;38;36m$%d\033[0;38;36m and your prizes are still: %s" % (p3s,p3p))
                time.sleep(2)
                print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p1name)
                time.sleep(2)
                player1() #player1 function
                break  

            if words[w] != phrase[w]: #if the empty phrase is not complete the user can spin again so long as they previously gueseed correctly
              spin = input("\nCLICK \033[1;39;36mENTER\033[0;38;36m TO SPIN: ") 
              time.sleep(1)
              os.system('clear') #clears shell 
              x = random.randint(0,9) #range for wheel list and all section 2 lists
              wheelspin()


          #If wheel[x] (random slot) is a skip the program goes to player1
          if wheel[x] == forfeit[0] and words[w] != phrase[w]:
            #keeps track of score of all players score
            print("\nSorry \033[1;34m%s\033[0;38;36m, But Your Turn Has Been \033[0;31;50mSKIPPED!\033[0;38;36m" % p3name) 
            time.sleep(2)   
            print("\nYour Total Is Still \033[0;38;36m$%d\033[0;38;36m And Your Prizes Include: %s" % (p3s,p3p))
            time.sleep(3)
            print("\n\033[1;34m%s's\033[0;38;36m Total is \033[0;38;36m$%d\033[0;38;36m And Their Prizes Include: %s" % (p2name,p2s,p2p))
            time.sleep(3)
            print("\n\033[1;34m%s's\033[0;38;36m Total is \033[0;38;36m$%d\033[0;38;36m And Their Prizes Include: %s" % (p1name,p1s,p1p))  
            time.sleep(3)
            print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p1name)  
            time.sleep(2)
            player1() #player1 function 

          #If wheel[x] (random slot) is a bankrupt the program goes erases their score and goes on to player2
          elif wheel[x] == forfeit[1] and words[w] != phrase[w]:
              time.sleep(1)
              #keeps track of score of all players
              print("\n\033[0;31;50mBANKRUPT!\033[0;38;36m YOU LOSE ALL YOUR MONEY") 
              p3s = 0 #assigns new money score
              p3p = [] #assings new prize score
              print("\nYour Total Is Now $%d And You Lost All Of Your Prizes!" % (p3s))
              time.sleep(2)
              print("\n\033[1;34m%s's\033[0;38;36m Total is $%d And Their Prizes Include: %s" % (p2name,p2s,p2p))
              time.sleep(2)
              print("\n\033[1;34m%s's\033[0;38;36m Total is $%d And Their Prizes Include: %s" % (p1name,p1s,p1p))  
              time.sleep(2)
              print("\nNow, on to \033[1;34m%s\033[0;38;36m" % p1name) 
              time.sleep(2)
              player1() #player1 function  
    
    player1() #runs player1 function
    
    def podium():
      #maintains value from player3 function 
      global p1s
      global p2s
      global p3s
      global p1p
      global p2p 
      global p3p
      
      #dababy function LETS GOO!!!
      def dababy():
        print("""
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
#################################################################z##*+################################################################################
##################################################################*:::*+##############################################################################
##############################################################zznnnnnnzz#####+########################################################################
###########################################################znxxxxnnnxnnnnnnnnzz###zz##################################################################
######################################################zzznnxxnxxxnnxnnnnnnnnnnnnnnzznnz###############################################################
###################################################znnnxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnn##############################################################
##################################################nxxxxMxxxxxxxn+i::xxxnnnnnnnnnnnnnnnnnnz############################################################
#################################################xMxxxxxxxxxxxn.` .ixxxnnnnnnnnnnnnnnnnnxxz###########################################################
################################################xMxMMxxxxxxxxxx+i`+xxxnnnnnnnnnnnnnnnnnnnnn###########################################################
###############################################xMxMxMMxxxxxxxxxx+ +xxznxnnnnnnnnnnnnnnnnnnxz##########################################################
##############################################zMxMxxMMxxxxxxxxxM#`*xn`:xnnnnnnnnnnnnnnnnnnnx##########################################################
##############################################xMxxxxMMxxxxxxxxMM# ix+``nnnnnnnnnnnnnnnnnnnnnz#########################################################
#############################################zMMxMMMMxxMMMxxxxxMz`ix:` *nnnnnnnnnnnnnnnnnnnnn#########################################################
#############################################nMxMMMMMMMMMMxxxxxMz`in```,xnnxnnnnnnnznnnnznnnn#########################################################
#############################################xMMMMMMMMMMMMxxxxxMz`i#`:: z:.nnnnnzzzznnnnznnnn#########################################################
#############################################xMMMMMMMMMMMMxxxxxMz i:`++ i.`nnnnnnnzzzzzzznnnn#########################################################
#############################################MMMMMMMMMMnxMMMxxxx# :``ii`.``znnnnnnnnzzzzzzznnz########################################################
############################################zMMMMMMMMxMxMMWMMxn,````   `  `znnnnnnnnzzzzzzznnz########################################################
############################################nMMMMMMMMMxzxWWWMMx::i.`i##i .*nnnnnnnnnzzzzzzznnnz#######################################################
############################################xMMMMMMMMMM#nMWWMxMMxx``znnz``nnnnnnnnnzzzzzznnnnnz#######################################################
############################################xMMMMMMMMx*z#.;xMMxxz*``:#z;. :innnnnnnznzzzzznnnnn#######################################################
############################################MMWMMMMMx: ..``*WMMx`````+z`````nnnnnnnzzzzzzznnnnn#######################################################
###########################################zMMWMMMMMx```.`.iWWMM+#znznxzzzzzxnnnnnnzzzzzzzznnnnz######################################################
###########################################zMMMMMMMMM::.,.+nWWMxxxxxxnxnnnnnnnnnnnnzzzzzzzznnnnz######################################################
###########################################zMMMMMMMMxn#..`*nWWMxxxxxxxxnnnxxnnnnzzzzzzzznzzzznnz######################################################
###########################################nMMMMMMMMMxn,`.+xWWxxxxxxxnnnnnnnnnnnnnnnzzzzzzzznnn#######################################################
###########################################nMMMMMMMMMMn##z#nxMxxxxxxxxnnnnnnnnnnnnnnzzzzzzznnxn*+#####################################################
###########################################nMxMMMMMMMxnzznnznMxxxnxxnxxxnnxnnnnnnnnnnzzzzzzznxn#*#####################################################
###########################################nxMMMxMMMMnnnMWMxxMMxxMMMMWMWWMMMMMMMMxxxxxnnnnnznnnzi#####################################################
###########################################nxMMMxMMMMxMMWWWWMMWWW@@@@@@MMWWWWWWWWWW@@@@WWWMMxnnnzz####################################################
###########################################nMMMxxMMMMMWW@@@@MW@@@@@@@##@#######@####@@@@@@@@@@WMMxxnz#################################################
###########################################xMMMMMWWWWWMW#@@@MW##################@########@@@@@@@@@WMxz################################################
##########################################zxMWWW@@@@@@MM####MW#############################@@@@@@@@@@Mz###############################################
########################################znMW@@@@@####@WW####WW@@@@@@@@@@@@@@@@@@@@@@#########@@@@@@@@x################################################
#######################################zxW@@@@########@M@#@@*:WW@@WWWWWWWWWWWWW@@@@@@@@@@@@@@###@@WMxz################################################
#######################################x@@@@@@@######@W,*@@@i.nWWWMMMMMMMMMMMMWWW@@@@@@@@@@@@@W@#Wz###################################################
#######################################M@@@@###@###@@@W.#@@@WiiMMMxxxxnxxxxxxxMMMMWWWMMMMWMMMMnM@n####################################################
#######################################x@@@@###@@@@@@@M.MWWWMWWxxxnnnnnznnnnnnnnxnnnznnzzzzzz##zn#####################################################
########################################zzW###@@@@@@@WWM@WMMxMMxxnnnzzzzzzzznnzzz###*++++++++++z######################################################
##########################################zW#@MWWWMMMMMMMxxxxxMxnnnnz#zz##zznzzzzz#+++#+++#++++z######################################################
############################################xWMxMxxxxnnnxnnxMMMxxnnz######zzzzzzznnzzzz##+++*+########################################################
#############################################nxxxxxxxnxMMMWMWMMxnnzz++#+++#zznnnnnnz##*++##+*+#z######################################################
#############################################zxxxxxnnxWWWWWWWMMMxxnz++#++*#znnnxnnnz#++***++++#z######################################################
##############################################xxxxxnxMMMMWWWWWMMMxnz###+++#zzznnnnnzz#+++***+*i#z#+###################################################
##############################################nxxxxxMxxxxMMMMMMMMxxnnn#####zznxMMMxnzz##++***;,:#*+###################################################
##############################################zxxxxMxxxxxxMMMMWMMMMxnnzzzz#znxMMMxnzzznzz#+**;,.:#ni:i################################################
##############################################zxxxxxxxxxMMMMWWWWWMMMxxnzz#znxxxxxnn#*+#nz##++*:,,zM*:.:+##############################################
###############################################nxxxxxxMMMMMMMMWWWWWMMxnz###zxxxMMMMMz###zz#++*+*#zz#;,,+##############################################
############################################znz+#nxxxMMMMxxnnnxMWWWMxxn#+*+#znMWW@@@MMWMxz#++zzz##+z+**zzz###z#########################+##############
##########################################*i+x*iinxxMMMMxnxxxnnMMMMMxxn#+*i*+xMxxMxn+*++++++++xnzzzzzn###zzz##########################################
#########################################*;;+n;;inxxMMMMMW@@@WxWWWMxxxnz++***#zxxxnz##++++++**zMxMnzzznnz#nz###########################z##############
#########################################i;:#zii+nxxMMW@WMMMxnznxMMxxxxz#+++++znxxxnz#+###+****xMxxnz##nxn#+##########################z+;;i###########
#######################################zzii*znnnnxxxxxxxxxxxxnxxMMMMxxnz#***+++##zzz###z#+*ii*+#WMxn#+++xxz+##########################+;,`,###########
######################################zznnzxnzzzxxxxxxxxxxMMMMMxxxxxnnnz#****+***++#####++*ii*+#MxMnz####nxn#zz#######################*:,.,###########
######################################nnnznxnnxxMxxnnnnxxxxxxnnnxxxnnxnz#+****+*i*+#####+**;i*+zM#nxnzzz##nxxxzznz###################+i:,.;###########
#####################################znnnnMxnxMMMxnnnnnzzzzzznnnnxxxxxn##+**+++*ii**+###+*i:;*+zx+#xxnnnzzxnxWnznnzz#################*i;,,+###########
####################################znnnnMxznxxWWxxxnnzzz#zzznnnxnxxxnz##+***+++**+++###+*i,,i+#n+##xMnnnzzzzxMxznzzz###############+i;;;;############
####################################zzzzxMz##zxWWxnnnzz####zznnnnnxxnn#++*ii*+##+*+###++**;,:*+#n+##zMxnxnzzzzxMxzzzzzz#z###########*i;:i#############
###################################zzz#zMx##+#MMMxxnnzz##+##znnnxxxxzz++**i;;*+++*#nnz#++*i;i+##z+###zMxxxnz#nznnMnnnnzzz###########**iii#############
##################################nnnz#xxz#++nMxxMxnz###++##nnxxxxnn#++*ii;,;;;;;i+zxxnz#+*i*+##z#####zMxxnzzzzzznxMxnzzzz#########z+**#+#############
#################################nxnn#zMnz#+#xxnMMxnz###++#zxxMxnzzznz#++***++****+#zMMnz+**+##z*######zxxnnnzz#nnzzxxxnnn#+++######***#+#############
################################zxxnzzMxnz#+nMzzxMxnn#+###znxMMxnzznxxnz##*+zxMMx+i*+zxMxz+*###z;#######znxxxnzznnnzzznnnzz++**###z#*++#*+############
###############################znnnznxMxxzz#xx##nxxxnz#zznxMMxxxxxMWWMxnnz+#znz#*iii*++zxMz+##zn#z########zxxxnznnznnzzzzzz#*i*+##z#*+#+*+############
##########++##################zzzz#zxxnnnznzMn#++nxxxnnnnxMWxnnnnxxMMMMMMMz#*i;iiiiii***+nWz##nMz##########zxxxnzzzxnz#####++*i*++##++#+**############
#########*;ii+###############zzz##+nWxnz##zxM###+zxxxxxxxMWxnnnnznzzznxxnzz##*i*i****i****Wxz#xM############zxMxnnnnnz#++++++****++##z#+**############
#########*iiii+#############zz##++zMxzn#+##Mn#####xxxxxxMWMxnzzznnnnxMMxnnMxxnnnnnnnz#++**nMzzxM#############zxxnnxxnz#++*+****+*+#++zz+ii############
##########i*iii+###########z###+*#MMzzz++#nx######nMxxxMWMxnzznnxxMWWWMnznxxnzz#+******+##zxzzxx#############zxMMxxxnz#++*******++#**+++ii############
##########+++*ii##########zz###++Mxzz#**#znz######zWMxMMWxnnnxxMxxxxnz###+++++*iii++##zxn#zzznxn###########zznMMMMxnz##++******i++#++**+*i+###########
############z+**#######zzzzz#+*+MMzz#**##zz#######zMWxMWWxxxxnnzzznnnnzzz##zzz###nxMWMxx##z#znxz########xMMWMMMMMMxz##++**#*+#*;**#++i*i*i+###########
#########+#xz#+*zz#####nz##++*+xMzz#*i##zz#########xWMxMMxMMxxxxxxMMMMxxnnnnnz#*+#zMWzz++#z#zxn########nWWMxxxxxxxz#+++*+++**##i*++++ii;i**###########
###########nnz##nn###znzz#++*+xnz##+*+#############nWWxxMxMWWW@@WWxMxnnnnz#*;,,,,;:nMn#*+#zznxz########xMxnnznxxxn#+++#++#+*++#i*+*+*ii;:ii##z########
###########znnz#zxz+#znzz+*++nnz#++**+++############MWxxxxxxxxM@nz#+#**;.:,`.`....;xx#**+zzzxx#########xMxnzznxxxn#++++#+#z+++z**+i++*i::;i+#z########
###########znnz#znz#zzzz#+++zzzz#+*i**+++###########nMMxnxxnnxxWx*;::,,``.``````..+xz+i*+zznxz##########xxxxxMMxxn#++++##+#z++#+i***#+*:::i+##########
###########znnz#znzzzzz###+znzzz+****++##znnxxz#####zxWMxxxnnnxxMzii;,,.`..`..:i,:##+ii*#zznn###########zxMMW@WMxz#+++###++z++#*i+#**+*;::i+##########
###########znzz#znzzzzz#++znzzz+*+**+###zznznnnz#####zMMxxxnnnnnxn+i+*++++#*+;,.`:n*i;i*#zznz############zxMMWMxz##+*+#zz#+##++iii+*ii**;:;*##########
###########zzzzzznzzzzz###zzzz#****+*+nzzz#+++zz######zMMxxxnznnzn#:,:,,:.,..`.`,++*iii+#znz#############zMMMMMnz++++++#z#+###+*ii***iiii;;*##########
###########zzzzzzzzznz##zzzzzz#***+zzzz##+iiii#z#######nMxxxnnznz##+,::,:,,.:.;.++*iii*+zzn#*###########zMMMMMMn######++#z#+##++*ii**iiiii;;##########
##########zzzzznzzznz#zz##z###+++##zz+++*iii*+zz########nMxxxnnzn#++i*+*+*+i*i*i*;;*ii*#znnzi.`,;i######nMMMxxxnz#####z++zz#*+*++*iiiiiiiii;+#########
##########zzzzzzzznzzzzz##z###+++####++iiii*+zz#########zzMxxxnnnzz++*+++*******;;+*i*++znnzz:``. .#####nMMxxxxnnzzzz##z++zz****++iii*iiiiii*#z#######
##########zz#z#znnzznz#zzz####++####++*i**+##zz#######+;:,zxxxnnnnzzz#+++**+****++ii**+#znnzn;`..``*#*+#zxxxxnnnnzz####z#+z#*i**++*iiiiiii**i#########
##########zz#z#znzznn##zz#####+++#+***i*+znnzz#######+.,..#xxxnnnnnnnnnz#######++*****+#zxnzn+...```.``*#zzznnnnnnnzz##+z##+*****++*;;;iii**i#########
##########zzzz#zzzzzzznn#+#zz+*+##+ii**#xMn##z##+##+;..,.:#Mxxnnnnnnnnnnnnnzzz###+****+zxxnzn*,..````` `,;*#nnznxnnnnz#+#z#*++*i**++i;;iiii***########
##########zzzzznznznzzzz###zz+####+**++nMxnz####,,;......;+MMxxnnnnnxMMMMMMMMxnz#+****#nMxnzn#,..``      ```.:*zxxnxnnz##z#********+*i;;;;;i**########
##########zzzzzzzzzzzz####nz+*###++++#zzxMxz+i;:......,.,i#MWxnnnnxxxxxxxxMxnn##+++**+zMxxnzn;,.````       ``.`,+nnnnnz####+**********;;;;;;i*+#######
##########zzzz#zz####z##zzz+*+z++++++#zzzzzz+;,......,,.;i#MWWxnnnnxxnnnnnn###+++++**#MMxxnnx#:````      ` `..` `.;#nnnnz###+****+**i*i;;;;:;**#######
##########zzz##zz##zzzznzz#+#z#++++++++#z####zi.`..,,,..;i#MWWMxxnnnnnnzzz###++*+***+xMMMxnnx::`.``  ```` `.``  `` .*nnnnz###++*+****ii;:;;::;i+######
##########zzzzzz###zz###zzz#####z#++#+*+####zz+..`..,,..;i#xMWWWxnnnnnzzz###+++*++*+nWMMMxnnMi,```   ````..```    ``.#nnnnz###++++***ii;::;:::i*######
##########zzzzzz########zn#++++++*+##+i+++++##+......,.,i*xxMWW@Wxxnnnnzzzzz####++#nWWMMMxxxx:,```   ``..``` `    `..,#nxxnzz####++**ii;;::;::;*+#####
##########zzzzz###########++++++**+###+#+*++##;.......,,;i#xMWWW@@Mnnxnnnnzzzz####nWWWMMMxxxM::```   ``.`` `  ```.,.` ,+znnnnzzzz##+**i;::::;:;i+#####
##########zzzzz############++++**+#z##z#++###i........,.iizMMWWW@@@WxxxxxnnnnnnnznWWWWMMMxxMi;,``   `````    ```,:`    `;+znnnnzznzz+*i;::;::;;i*z####
##########zzzzz######+##z+#####zzzz#zzz#+#n#:```........:**nMWWWW@@@WMxxxxxxnnnnMWWWWWWMMxxWi;,``  ``` ``   ``.:,     ` ``:+nnnzzzznz#i;::;i+i;;i#####
##########zzzz######++#zzzzzznnnz+++##z###*,.```........;*i*MMWWW@@@@@WMMxxxxxMWWWWWWWMMxxz+:,.`  ``` `    ``,,`       `````;znnzzzznz+;:::#+:..,,.*##
##########zzzz#####++##+#zzzzz##**+##zz#i,,,,,........,.:i*:+MMWWW@@@@@@WWWWWWWWWWWWMMMMM#:+,i.  ```     ```..`   ```````````iznnnzznnn*:,i*,..,:i:;##
#########zzzzz#####+##++++##+#***+zzz+*:....,,,........,:+;i,*xWWWW@@@@WWWWWWWWWWMWWWMMn;.;i;,`````   ```````    `````````````innzzzznnzi:;.``..,.i;##
#########zzzz#######+++++++##+*+++##+:.......,,,.....,,.:+ii,,:+xWWWWWWWWWWWWWWWWMWWMni,.,i:+:```   ```..`` `    ``````````````;nzz#zznn#i,```.```,;*z
#########zzz#######++++#++++++++zz#+:..........,,.....,.,+;;:,:::i+znxMWWWWWMMMxnz+i:,,..:;::,````````.,.`      `````````````.``+nzzzznni.````.````;;#
########zzzz######++++++++++###zzz+;,,..........,,,......**i,..,,,:,:::;;;;;:::,,,,,,,..,i,+i````````..``      ``````````````.` iznzzznn;.```.``...::#
########zzz####z##++++**+++##zzzz+::,,,..........,,,,...,+i::,...,,,,,,,,,,,,,,,,,,,....;*:;:...```...`       ```` `````````..` ;nnz##i,ii````.,;.`..+
########zzzz##z#++++**+**++#zzzz+:.,,,,,...........,,,..,;*i:,............,,,..........,i:*:..````...``      ````  `````````..`:#+*i:;;,::`:`.`.,.`..*
########znzzzz###++***+++++#z##*:....,,,............,,,,,i+;;,,........................:i:;:..`....``` `    ````   `````````,.`;*;;i:*,:#.`;,``````.`;
#######znnnzz####++****+++#zz#*,......,,,............,,,,;*;;:.,,,,,,........,,,,,,,,,:;:*i..,,,..````     ```     ````` ``.,.`,*:i:,+,.#,`.;.```..,`i
#######znnnz#zz#+++*****++###i,........,,.............,,,;#i:;:,....,,,,,,,,,,,,,,,,::;*;;;.,,,,.```      ```     `````````.,` .i:;i,i;,i;:`i,.``..,.#
#######nxnnznnz##++*i*+++##+;............,.............,,;i*i;:,,,........,,,,,,,,,,,,;;*;,,,:,.````     ```      `````````,.```i*;i;:;;,,*`.:,,`.,,*z
#######nxxnxxn#++++**++++++;,,....`.....................,:+#:,,,............,,,,,,,,,:#;;i,,::..```     ````     ````  ```.,.```:ii;*;;*;;i.`.:,:,,i+#
#######nxnnMxn#++**++**+++;,,,...........................:;i+;:.............,,,,,,,,:i:+*:,,:..```     ```       `````````..`    `#nxxxxxW###+*#+i*++#
#######nxnxMxn#++##++****;.,,............................,;+;;;.............,,,,,,,,,*iii:,,..````  ` `.``       `````````..`   ``+nnnxxxMxxnzn#+*+##+
######znxnMxxn#+#z##+***;.................................::*;:,............,,,,,,,,;;+*;:,,.``````` ```        ``````````..`  `` *xxxMnzzzzz*i*+#++##
#######nxxMxxn##zz###+**.`....................``...`....`.,i+;;,................,,,,*i*+;:,.```````````        ```````````.``  ```innnnzzzz#z+*i*+*+##
#####**xnxxMxnnnzzzzz+*i.``...........````.....``..```...`,,;*,,..`...........,,,,,:;*ii;,..```````.`` `     `````` ``````.`   ```:xxxxxnnz###*ii*+###
#####;#nnxxxxnnnnzz##+*;````..```.....``````....```..`````.:*+i:..............,,,,,i:+#i:..```````.`````     `````  ````````   ```,nxxnnnnz###*ii+##++
####+i*xnnnxxnznn###++*:``.```````....```````....```````.``,;*,,.```..........,,,,:+*i*i,..`````..````` ```` ````     `````   ````.znnxnz#zz##*ii**+#+
####+;;zxnnnnnznnz#+++*:.`.```````.....```````....`````````,,;+:,.``..........,,,,::i#i,..````...``````````` ```      ``````  `````#nxxn#znzzz+i***++*
#####z*:#nnnnnznxxz#++*;..````````.....`````````...````````.:i;,:.```.........,,..+ii*i,..``....```````````````       `````   ``` `*nnnzznz#z#+i***i**
####*++i:*nnnznnnz##+***...````````....``````````...```````.,,i:..````...........,i++i:.........```````````````       ````   ``````ixxxnnn###++*iiiii*
####zz+*:,;#z#zz##+++**z#i..```````.....```````````.````````,i*;:..`.............i;i+i,........````````````````       ````   ``````inxxnzz#####+*ii;i*
####z##xn*i.:;+##++++*+n#;..```````.....`````````````.``````.,:i..`.```.........,i**i;.........``..````````````      ````   ` `````innnnzzz####+**ii;i
###zxxxi;n+i*;,,i*;++#z*;:...```````....``````````````.`````.:i*i:.`````........:,*zi,................``````````      ```   ```````:nnnnnzzzzz#+**iii*
###nMxxnz*i*z::#,.ii.ii::,...```````....````````````````.```.,;i,,.`````.......,+;*i;.,.................`````````     ```   ```````.zxxxnz#zzz##++***i
###xxxnnn*+n#i#ziiz;;#;i,.....`````.....````````````````..```,,:*,.`````.......,,+ni,,..................``````````   ``     ````````#nxxnznnnnz###*iii
##zxMxxxnxx#i+#*;+#;+*,,,,....```........`````````````````.``.;i*:,``````.....,+:i+i,,..................```````````  ``     ````````+xxxxnnzzz#+++*iii
###xxxxxnnnxMM#*z*;ii:;,.,,....```...........``````````````...,,*:.```.......,:;i+*,......................``````````       `.```````+nnxnnzzznz#++*i**
##zxxxxxxxnxxnnnxn+z#*;...,.....``...........,...````````````.,:;+:.```......,i:*#i,,......,........,,,.....`````````      `.```````*nxxxxzzzz#+***ii*
##zxxxxxxMxznnnxzz##++:................``````...,,..`````````.,,;;,.``````..,,i;*i:,......,....,,,,,,,.......`````````     ..```````innnnn###zz+***ii*
##nxxxxxxxz#znnznz#+#+,`...,..,........``````````..,,.```````..,,;*,.``.....,;,+#:....,,...,,,:,,..........```````````  `  :.```.:*z#nnnzz##zzzz+++*i*
#znxxxxxxnzzznnnxnz#++.`...,..,........`````````````..,..``````.ii;:.````...,i,*i,.......,,:,,...............``````````  ` ;``.i#nxn#nnzzz##zzzz#++*ii
  """)
      #The escapade function :)
      def playagain(): #provides option to play again but abdicated at the last minute
          playagainc = input("\nWould You Like To Play Again? (Y/N)\n>>> ")
          if playagainc == "Y": #if user inputs "Y" the following will print
            print("\nGreat decision!")
            time.sleep(1)
            os.system('clear')
            time.sleep(1)
            print("Your game will start in 3")
            time.sleep(2)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("\nSIKE")
            time.sleep(0.5)
            os.system('clear')
            time.sleep(0.5)
            print("LET'S GO")
            time.sleep(1)
            dababy()
            time.sleep(5)
            os.system('clear')
            print("LEAVE IMMEDIATELY")         
      
          elif playagainc == "N": #elif user inputs "N" the following will print 
            print("\nThanks For Playing!")
            time.sleep(3)
            print("\nLET'S GO")
            time.sleep(1)
            dababy()  
            time.sleep(5)
            os.system('clear')
            print("LEAVE IMMEDIATELY")
          else:
            print("You May Have Misclicked..")
            playagain()    


     #Final resutls of the program
      time.sleep(2)
      #prints phrase 
      print("\nThe Phrase Was...") 
      output(phrase[w])#phrase 
      time.sleep(2)
      os.system('clear') #clear
      #Podium inspired by   
      print("""
██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░██████╗░░░░░░░░░
██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔════╝░░░░░░░░░
██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░╚█████╗░░░░░░░░░░
██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░░╚═══██╗░░░░░░░░░
██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██████╔╝██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░╚═╝╚═╝╚═╝""")
      time.sleep(3)
      os.system('clear')

    # ~~ Section ~~ 5: This section contains all the possibe order of scores and apporpriately assigns the scores a variable. This is needed for the regular function
      
      #If player1 is first 
      if p1s > p2s and p1s > p3s:
        firstplacescore = p1s
        firstplacename = p1name
        firstplaceprize = p1p    

       #If player2 is first
      if p2s > p1s and p2s > p3s:
          firstplacescore = p2s
          firstplacename = p2name
          firstplaceprize = p2p

       #If player3 is first 
      if p3s > p1s and p3s > p2s:
          firstplacescore = p3s
          firstplacename = p3name
          firstplaceprize = p3p

      #If player3 is first, player1 is second, and player2 is third 
      if p1s > p2s and p1s < p3s:
          secondplacescore = p1s
          secondplacename = p1name
          secondplaceprize = p1p

      #If player3 is first, player2 is second, and player1 is third
      if p2s > p1s and p2s < p3s:
          secondplacescore = p2s
          secondplacename = p2name
          secondplaceprize = p2p

      #If player2 is first, player3 is second, and playe1 is thrid
      if p3s > p1s and p3s < p2s:
          secondplacescore = p3s
          secondplacename = p3name
          secondplaceprize = p3p

      #If player1 is last
      if p1s < p2s and p1s < p3s:
          thirdplacescore = p1s
          thirdplacename = p1name
          thirdplaceprize = p1p

      #If player2 is last
      if p2s < p1s and p2s < p3s:
          thirdplacescore = p2s
          thirdplacename = p2name
          thirdplaceprize = p2p

      #If player3 is last
      if p3s < p1s and p3s < p2s:
          thirdplacescore = p3s
          thirdplacename = p3name
          thirdplaceprize = p3p

      #Podium with three possiblities: 1st place, 2nd place, and 3rd place 
      def regular():

        print("In Third Place, With A Score Of...") #print statment which heralds the score

        time.sleep(2)
        os.system('clear') #clears system 

        print("      ", end = '') #space for alignment 
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %thirdplacescore) #Displays score for thrid place
        time.sleep(2)
        print("        ", end = '') #space for alignment
        print(thirdplacename, end = '\033[0;38;36m') #Displays name for thrid place
        #prints podium size inverse to ranking
        print("""\033[33m
  ┏━━━━━━━━━━━━━━━━━━┓
  ┃       3rd        ┃
  ┃                  ┃
  ┃                  ┃
  ┃                  ┃
  ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        #print statment which heralds the prize
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        time.sleep(1)
        print(thirdplaceprize) #prints prize for thrid place
        time.sleep(4)
        os.system('clear') #system clears

       
        time.sleep(0.5)
        print("In Second Place, With A Score Of...") #print statment which heralds the score

        time.sleep(2)
        os.system('clear') #clears system 

        print("                                           ", end = '') #space for alignment
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore) #Displays score for second place
        time.sleep(2)
        print("                                             ", end = '') #space for alignment
        print(secondplacename, end = '\033[0;38;36m') #Displays name for thrid place
        #prints podium size inverse to ranking
        print("""\033[37m
                                        ┏━━━━━━━━━━━━━━━━━━┓
                                        ┃       2nd        ┃
                                        ┃                  ┃                 
                                        ┃                  ┃
                                        ┃                  ┃
                                        ┃                  ┃
                                        ┃                  ┃
                                        ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
        """, end = '')
        print("                                ", end = '') #space for alignment 
        #print statment which heralds the prize
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        time.sleep(1)
        #prints prize for thrid place
        print(secondplaceprize)
        time.sleep(4)
        os.system('clear')



      #print statment which heralds the score in a stacto manner
        time.sleep(0.5)
        print("AND", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("THE", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("FIRST", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("PLACE", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("WINNER", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("WITH", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("A", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("SCORE", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("OF", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()
        print("...", end = ' ')
        time.sleep(0.5)
        sys.stdout.flush()


        time.sleep(2)
        os.system('clear') #clears sheel 

        print("                      ", end = '')#space for alignment
        print("\033[1;39;36m Score\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore) #Displays score for first place
        time.sleep(2)
        print("                           ", end = '')#space for alignment
        print(firstplacename, end = '\033[0;38;36m') #Displays name for first place
        #prints podium size inverse to ranking
        print("""\033[93m
                    ┏━━━━━━━━━━━━━━━━━━┓
                    ┃       1st        ┃
                    ┃                  ┃
                    ┃                  ┃                  
                    ┃                  ┃          
                    ┃                  ┃                                   
                    ┃                  ┃                  
                    ┃                  ┃                  
                    ┃                  ┃                  
                    ┃                  ┃  
                    ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("               ", end = '')
        #print statment which heralds the prize
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        time.sleep(1)
        #prints prize for thrid place
        print(firstplaceprize) 
        time.sleep(4)
        os.system('clear')


      #ALL THREE PODIUMS ARE PRINTS OUT FOR VISUAL INTRIGUE
        print("""               
  \033[93m        %s                                                    
  \033[93m ┏━━━━━━━━━━━━━━━━━━┓                                                  
  \033[93m ┃       1st        ┃                                             
  \033[93m ┃                  ┃ \033[37m       %s                                
  \033[93m ┃                  ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━┓ \033[33m                              
  \033[93m ┃                  ┃ \033[37m ┃       2nd        ┃ \033[33m      %s                      
  \033[93m ┃                  ┃ \033[37m ┃                  ┃ \033[33m ┏━━━━━━━━━━━━━━━━━━┓  
  \033[93m ┃                  ┃ \033[37m ┃                  ┃ \033[33m ┃       3rd        ┃
  \033[93m ┃                  ┃ \033[37m ┃                  ┃ \033[33m ┃                  ┃     
  \033[93m ┃                  ┃ \033[37m ┃                  ┃ \033[33m ┃                  ┃
  \033[93m ┃                  ┃ \033[37m ┃                  ┃ \033[33m ┃                  ┃
  \033[93m ┗━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━┛ \033[33m ┗━━━━━━━━━━━━━━━━━━┛ 
  \033[0;38;36m
        """%(firstplacename, secondplacename, thirdplacename)) #all names are displayed 
        
        #Final remarks from the programmers Ebrahim and Aaron 
        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)

        playagain() #moves to play again function

      # ~~ Section 6 ~~ This section accounts for all the possible ties applicate to this game. The following code will be printed once but applies to all if statements 
      if p1s == p2s and p1s > p3s: #IF PLAYER 2 IS EQUAL TO PLAYER 1 AND PLAYER 1 IS GREATER THAN PLAYER 3
        #SSIGNS ALL SCORE, NAME, AND PRIZE VALUES TO NEW VARIABLES
        firstplacescore = p1s
        firstplacename = p1name
        firstplaceprize = p1p
        firstplacename2 = p2name
        firstplaceprize2 = p2p
        secondplacescore = p3s
        secondplacename = p3name
        secondplaceprize = p3p

        print("In Second Place, With A Score Of...")  #print statment which heralds the score
        time.sleep(2)
        os.system('clear') #clears shell 

        print("                      ", end = '')  #space for alignment 
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore) #Displays names for Second place
        time.sleep(2)
        print("                        ", end = '') #space for alignment
        print(secondplacename, end = '') #Displays name for second place
        #prints podium size inverse to ranking
        print("""\033[37m   
                  ┏━━━━━━━━━━━━━━━━━━┓
                  ┃       2nd        ┃
                  ┃                  ┃
                  ┃                  ┃
                  ┃                  ┃
                  ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("              ", end = '')  #space for alignment 
        #print statment which heralds the prize
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(secondplaceprize) #prints prize for second place
        time.sleep(5)
        os.system('clear') #clears shell
        time.sleep(0.5)

        print("Tied In First place, With A Score Of...") #print statment which heralds the score for two users
        time.sleep(2)
        os.system('clear') #clears shell
        print("      ", end = '') #space for alignment 
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore) #Displays score for both first place contestants 
        time.sleep(2) 
        print("     ", end = '') #space for alignment 
        #Displays inital name for first place
        print(firstplacename, end = ' & ')
        #Displays latter name for first place
        print(firstplacename2, end = '')
        #prints podium size inverse to ranking. Width increase is intended to encompass more information
        print("""\033[93m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           1st            ┃
┃                          ┃
┃                          ┃                  
┃                          ┃          
┃                          ┃                                   
┃                          ┃                  
┃                          ┃                  
┃                          ┃                  
┃                          ┃  
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
""", end = '')
        #print statment which heralds the prize
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        #Displays inital name for first place
        print(firstplaceprize, end = ' & ')
        #Displays latter name for first place
        print(firstplaceprize2)  
        time.sleep(4)
        os.system('clear') #clears shell

         #ALL TWO PODIUMS ARE PRINTS OUT FOR VISUAL INTRIGUE
        print("""               
\033[93m      %s & %s                                                   
\033[93m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓                                                  
\033[93m ┃           1st            ┃                                             
\033[93m ┃                          ┃ \033[37m       %s                                
\033[93m ┃                          ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━┓                               
\033[93m ┃                          ┃ \033[37m ┃       2nd        ┃                       
\033[93m ┃                          ┃ \033[37m ┃                  ┃  
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┃                          ┃ \033[37m ┃                  ┃   
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━┛ 
\033[0;38;36m
      """%(firstplacename,firstplacename2,secondplacename)) #all names are displayed 

        #Final remarks from the programmers Ebrahim and Aaron 
        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)
        playagain()

      # ~~ Section 6: Draw comments form the aformentioned code ~~ 
      if p1s == p2s and p1s < p3s:
        firstplacescore = p3s
        firstplacename = p3name
        firstplaceprize = p3p
        secondplacescore = p1s
        secondplacename = p1name
        secondplacename2 = p2name
        secondplaceprize = p1p
        secondplaceprize2 = p2p
        
        print("Tied In Second Place, With A Score Of...")
        time.sleep(2)
        os.system('clear')

        print("         ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore)
        time.sleep(2)
        print("        ", end = '')
        print(secondplacename,end = ' & ')
        print(secondplacename2, end = ' ')
        print("""\033[37m
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃           2nd            ┃
  ┃                          ┃
  ┃                          ┃
  ┃                          ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(secondplaceprize, end = '')
        print(" and ", end = '')
        print(secondplaceprize2)  
        time.sleep(3)
        os.system('clear')
        time.sleep(3)
        print("In first place, with a score of...")
        time.sleep(2)
        os.system('clear')

        print("                                 ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore)
        time.sleep(2)
        print("                                    ", end = '')
        print(firstplacename, end = ' ')
        print("""\033[93m
                              ┏━━━━━━━━━━━━━━━━━━┓
                              ┃       1st        ┃
                              ┃                  ┃
                              ┃                  ┃                  
                              ┃                  ┃          
                              ┃                  ┃                                   
                              ┃                  ┃                  
                              ┃                  ┃                  
                              ┃                  ┃                  
                              ┃                  ┃  
                              ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("                           ", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include... ", end = '')
        print(firstplaceprize)
        time.sleep(4)
        os.system('clear')
        print("""               
\033[93m       %s                                                   
\033[93m ┏━━━━━━━━━━━━━━━━━━┓                                                  
\033[93m ┃       1st        ┃                                             
\033[93m ┃                  ┃ \033[37m       %s & %s                                
\033[93m ┃                  ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓                               
\033[93m ┃                  ┃ \033[37m ┃           2nd            ┃                       
\033[93m ┃                  ┃ \033[37m ┃                          ┃  
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┃                  ┃ \033[37m ┃                          ┃   
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┗━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 
\033[0;38;36m
  """%(firstplacename,secondplacename,secondplacename2)) 
        time.sleep(3)


        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)
        playagain()
      
      # ~~ Section 6: Draw comments form the aformentioned code ~~ 
      if p1s == p3s and p1s > p2s:
        firstplacescore = p1s
        firstplacename = p1name
        firstplaceprize = p1p
        firstplacename2 = p3name
        firstplaceprize2 = p3p
        secondplacescore = p2s
        secondplacename = p2name
        secondplaceprize = p2p

        print("In Second Place, With A Score Of...")
        time.sleep(2)
        os.system('clear')

        print("                      ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore)
        time.sleep(2)
        print("                        ", end = '')
        print(secondplacename, end = '')
        print("""\033[37m   
                  ┏━━━━━━━━━━━━━━━━━━┓
                  ┃       2nd        ┃
                  ┃                  ┃
                  ┃                  ┃
                  ┃                  ┃
                  ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("              ", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(secondplaceprize)
        time.sleep(5)
        os.system('clear')
        time.sleep(0.5)
        print("Tied In First place, With A Score Of...")
        time.sleep(2)
        os.system('clear')
        print("      ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore)
        time.sleep(2)
        print("     ", end = '')
        print(firstplacename, end = ' & ')
        print(firstplacename2, end = '')
        print("""\033[93m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           1st            ┃
┃                          ┃
┃                          ┃                  
┃                          ┃          
┃                          ┃                                   
┃                          ┃                  
┃                          ┃                  
┃                          ┃                  
┃                          ┃  
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
""", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(firstplaceprize, end = ' & ')
        print(firstplaceprize2)  
        time.sleep(4)
        os.system('clear')
        print("""               
\033[93m      %s & %s                                                   
\033[93m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓                                                  
\033[93m ┃           1st            ┃                                             
\033[93m ┃                          ┃ \033[37m       %s                                
\033[93m ┃                          ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━┓                               
\033[93m ┃                          ┃ \033[37m ┃       2nd        ┃                       
\033[93m ┃                          ┃ \033[37m ┃                  ┃  
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┃                          ┃ \033[37m ┃                  ┃   
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━┛ 
\033[0;38;36m
      """%(firstplacename,firstplacename2,secondplacename)) 

        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)
        playagain()
      
      # ~~ Section 6: Draw comments form the aformentioned code ~~ 
      if p1s == p3s and p1s < p2s:
        firstplacescore = p2s
        firstplacename = p2name
        firstplaceprize = p2p
        secondplacescore = p1s
        secondplacename = p1name
        secondplacename2 = p3name
        secondplaceprize = p1p
        secondplaceprize2 = p3p
        
        print("Tied In Second Place, With A Score Of...")
        time.sleep(2)
        os.system('clear')

        print("         ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore)
        time.sleep(2)
        print("        ", end = '')
        print(secondplacename,end = ' & ')
        print(secondplacename2, end = ' ')
        print("""\033[37m
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃           2nd            ┃
  ┃                          ┃
  ┃                          ┃
  ┃                          ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(secondplaceprize, end = '')
        print(" and ", end = '')
        print(secondplaceprize2)  
        time.sleep(3)
        os.system('clear')
        time.sleep(3)
        print("In first place, with a score of...")
        time.sleep(2)
        os.system('clear')

        print("                                 ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore)
        time.sleep(2)
        print("                                    ", end = '')
        print(firstplacename, end = ' ')
        print("""\033[93m
                              ┏━━━━━━━━━━━━━━━━━━┓
                              ┃       1st        ┃
                              ┃                  ┃
                              ┃                  ┃                  
                              ┃                  ┃          
                              ┃                  ┃                                   
                              ┃                  ┃                  
                              ┃                  ┃                  
                              ┃                  ┃                  
                              ┃                  ┃  
                              ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("                           ", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include... ", end = '')
        print(firstplaceprize)
        time.sleep(4)
        os.system('clear')
        print("""               
\033[93m       %s                                                   
\033[93m ┏━━━━━━━━━━━━━━━━━━┓                                                  
\033[93m ┃       1st        ┃                                             
\033[93m ┃                  ┃ \033[37m       %s & %s                                
\033[93m ┃                  ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓                               
\033[93m ┃                  ┃ \033[37m ┃           2nd            ┃                       
\033[93m ┃                  ┃ \033[37m ┃                          ┃  
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┃                  ┃ \033[37m ┃                          ┃   
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┗━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 
\033[0;38;36m
  """%(firstplacename,secondplacename,secondplacename2)) 
        time.sleep(3)


        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)
        playagain()
      
      # ~~ Section 6: Draw comments form the aformentioned code ~~ 
      if p2s == p3s and p2s > p1s:
        firstplacescore = p2s
        firstplacename = p2name
        firstplaceprize = p2p
        firstplacename2 = p3name
        firstplaceprize2 = p3p
        secondplacescore = p1s
        secondplacename = p1name
        secondplaceprize = p1p

        print("In Second Place, With A Score Of...")
        time.sleep(2)
        os.system('clear')

        print("                      ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore)
        time.sleep(2)
        print("                        ", end = '')
        print(secondplacename, end = '')
        print("""\033[37m   
                  ┏━━━━━━━━━━━━━━━━━━┓
                  ┃       2nd        ┃
                  ┃                  ┃
                  ┃                  ┃
                  ┃                  ┃
                  ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("              ", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(secondplaceprize)
        time.sleep(5)
        os.system('clear')
        time.sleep(0.5)
        print("Tied In First place, With A Score Of...")
        time.sleep(2)
        os.system('clear')
        print("      ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore)
        time.sleep(2)
        print("     ", end = '')
        print(firstplacename, end = ' & ')
        print(firstplacename2, end = '')
        print("""\033[93m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           1st            ┃
┃                          ┃
┃                          ┃                  
┃                          ┃          
┃                          ┃                                   
┃                          ┃                  
┃                          ┃                  
┃                          ┃                  
┃                          ┃  
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
""", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(firstplaceprize, end = ' & ')
        print(firstplaceprize2)  
        time.sleep(4)
        os.system('clear')
        print("""               
\033[93m      %s & %s                                                   
\033[93m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓                                                  
\033[93m ┃           1st            ┃                                             
\033[93m ┃                          ┃ \033[37m       %s                                
\033[93m ┃                          ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━┓                               
\033[93m ┃                          ┃ \033[37m ┃       2nd        ┃                       
\033[93m ┃                          ┃ \033[37m ┃                  ┃  
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┃                          ┃ \033[37m ┃                  ┃   
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┃                          ┃ \033[37m ┃                  ┃ 
\033[93m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━┛ 
\033[0;38;36m
      """%(firstplacename,firstplacename2,secondplacename)) 


        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)
        playagain()
      
      # ~~ Section 6: Draw comments form the aformentioned code ~~ 
      if p2s == p3s and p2s < p1s:
        firstplacescore = p1s
        firstplacename = p1name
        firstplaceprize = p1p
        secondplacescore = p2s
        secondplacename = p2name
        secondplacename2 = p3name
        secondplaceprize = p2p
        secondplaceprize2 = p3p
        
        print("Tied In Second Place, With A Score Of...")
        time.sleep(2)
        os.system('clear')

        print("         ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %secondplacescore)
        time.sleep(2)
        print("        ", end = '')
        print(secondplacename,end = ' & ')
        print(secondplacename2, end = ' ')
        print("""\033[37m
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃           2nd            ┃
  ┃                          ┃
  ┃                          ┃
  ┃                          ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(secondplaceprize, end = '')
        print(" and ", end = '')
        print(secondplaceprize2)  
        time.sleep(3)
        os.system('clear')
        time.sleep(3)
        print("In first place, with a score of...")
        time.sleep(2)
        os.system('clear')

        print("                                 ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore)
        time.sleep(2)
        print("                                    ", end = '')
        print(firstplacename, end = ' ')
        print("""\033[93m
                              ┏━━━━━━━━━━━━━━━━━━┓
                              ┃       1st        ┃
                              ┃                  ┃
                              ┃                  ┃                  
                              ┃                  ┃          
                              ┃                  ┃                                   
                              ┃                  ┃                  
                              ┃                  ┃                  
                              ┃                  ┃                  
                              ┃                  ┃  
                              ┗━━━━━━━━━━━━━━━━━━┛\033[0;38;36m
  """, end = '')
        print("                           ", end = '')
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include... ", end = '')
        print(firstplaceprize)
        time.sleep(4)
        os.system('clear')
        print("""               
\033[93m       %s                                                   
\033[93m ┏━━━━━━━━━━━━━━━━━━┓                                                  
\033[93m ┃       1st        ┃                                             
\033[93m ┃                  ┃ \033[37m       %s & %s                                
\033[93m ┃                  ┃ \033[37m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓                               
\033[93m ┃                  ┃ \033[37m ┃           2nd            ┃                       
\033[93m ┃                  ┃ \033[37m ┃                          ┃  
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┃                  ┃ \033[37m ┃                          ┃   
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┃                  ┃ \033[37m ┃                          ┃ 
\033[93m ┗━━━━━━━━━━━━━━━━━━┛ \033[37m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 
\033[0;38;36m
  """%(firstplacename,secondplacename,secondplacename2)) 
        time.sleep(4)


        time.sleep(2.5)
        print("\nAaron: What A Great Game! Don't You Think Ebrahim?")
        time.sleep(2.5)
        print("\nEbrahim: Magnificent, If I Do Say So Myself.")
        time.sleep(2.5)
        print("\nAaron: I Think We Should Give Them A Chance To Play Again.")
        time.sleep(2.5)
        print("\nEbrahim: That's What I Was About To Say!")
        time.sleep(2.5)
        playagain()
      
      # ~~ Section 6: Draw comments form the aformentioned code ~~ 
      if p1s == p2s == p3s:
        firstplacename = p1name
        firstplacename2 = p2name
        firstplacename3 = p3name
        firstplacescore = p1s
        firstplaceprize = p1p
        firstplaceprize2 = p2p
        firstplaceprize3 = p3p
        print("Woah, A Three Way Tie!")
        time.sleep(2)
        print("This Calls For A Special Podium...")
        time.sleep(4)
        os.system('clear')
        print("Tied For First Place, With A Score Of...")
        time.sleep(3)  
        print("                                   ", end = '')
        print("\033[1;39;36mScore\033[0;38;36m = \033[1;33m$%d\033[0;38;36m" %firstplacescore)
        time.sleep(4)  
        print("""\033[93m      
                           %s, %s, and %s
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃                 1st                   ┃
                    ┃                                       ┃
                    ┃                                       ┃                  
                    ┃                                       ┃          
                    ┃                                       ┃                                   
                    ┃                                       ┃                  
                    ┃                                       ┃                  
                    ┃                                       ┃                  
                    ┃                                       ┃  
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0;38;36m             
   """ % (firstplacename,firstplacename2,firstplacename3))   
        print("", end = '')
        time.sleep(2)
        print("Their \033[1;39;36mPrizes\033[0;38;36m Include ... ", end = '')
        print(firstplaceprize, end = '')
        print(" and ", end = '')
        print(firstplaceprize2)  
        print(" and ", end = '')
        print(firstplaceprize3) 
        time.sleep(3)
        playagain()
      
      #If ~ Section 6 ~ Does not apply, the program will run the regular function
      else:
        regular() #runs regular function
      
    podium() #runs podium function
    
  guts() #runs gut function

game() #runs game function
