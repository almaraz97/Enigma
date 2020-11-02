import random as r

wordBank = ["ace", "act", "add", "age", "ago", "aid", "ail", "aim", "air", "ale", 'all', 'alt', 'amp', 'and', 'ant', 'any', 'ape', 'app', 'apt', 'arc', 'are', 'arm', 'art', 'ash', 'ask', 'ass', 'ate', 'awe', 'axe', 'bad', 'bag', 'bam', 'ban', 'bar', 'bat', 'bay', 'bed', 'bee', 'beg', 'bet', 'bib', 'bid', 'big', 'bin', 'bit', 'bog', 'boo', 'bop', 'bot', 'bow', 'box', 'boy', 'bra', 'bro', 'bub', 'bud', 'bug', 'bum', 'bun', 'bus', 'but', 'buy', 'bye', 'cab', 'cam', 'can', 'cap', 'car', 'cat', 'chi', 'cob', 'cod', 'cog', 'con', 'coo', 'cop', 'cot', 'cow', 'coy', 'cry', 'cub', 'cue', 'cum', 'cup', 'cut', 'dab', 'dad', 'dam', 'day', 'den', 'dev', 'dew', 'did', 'die', 'dig', 'dim', 'dip', 'dog', 'don', 'dot', 'dry', 'dub', 'dud', 'due', 'dug', 'duo', 'dye', 'ear', 'eat', 'ebb', 'eek', 'eel', 'egg', 'ego', 'eke', 'eld', 'elf', 'elk', 'elm', 'emu', 'end', 'eon', 'era', 'err', 'eve', 'eye', 'fab', 'fad', 'fag', 'fan', 'far', 'fat', 'fax', 'fed', 'fee', 'few', 'fez', 'fib', 'fig', 'fin', 'fit', 'fix', 'fiz', 'flu', 'fly', 'fob', 'foe', 'fog', 'for', 'fox', 'fry', 'fun', 'fur', 'gab', 'gag', 'gap', 'gas', 'gay', 'gel', 'gem', 'get', 'gig', 'gin', 'gob', 'god', 'goo', 'got', 'gum', 'gun', 'gut', 'guy', 'gym', 'had', 'hag', 'ham', 'has', 'hat', 'hay', 'hem', 'hen', 'her', 'hex', 'hey', 'hid', 'him', 'hip', 'his', 'hit', 'hoe', 'hog', 'hop', 'hot', 'how', 'hub', 'hue', 'hug', 'hum', 'hut', 'ice', 'icy', 'ilk', 'ill', 'ink', 'inn', 'ion', 'ire', 'irk', 'ivy', 'jab', 'jag', 'jam', 'jar', 'jaw', 'jet', 'jew', 'job', 'jog', 'jot', 'joy', 'jug', 'jut', 'keg', 'key', 'kid', 'kin', 'kit', 'koi', 'lab', 'lad', 'lag', 'lap', 'law', 'lay', 'led', 'leg', 'let', 'lid', 'lie', 'lip', 'lit', 'lob', 'log', 'loo', 'lot', 'low', 'lug', 'lux', 'lye', 'mad', 'mag', 'man', 'mat', 'max', 'may', 'men', 'met', 'mic', 'mid', 'mix', 'mob', 'mod', 'mom', 'moo', 'mop', 'mos', 'mow', 'mud', 'mug', 'nab', 'nag', 'nap', 'naw', 'nay', 'net', 'new', 'nil', 'nip', 'nit', 'nod', 'nog', 'not', 'now', 'nub', 'nun', 'nut', 'oaf', 'oak', 'oar', 'oat', 'odd', 'ode', 'off', 'oft', 'ohm', 'oil', 'old', 'ole', 'one', 'opt', 'orb', 'orc', 'ore', 'our', 'out', 'owl', 'own', 'pad', 'pal', 'pan', 'pat', 'paw', 'pay', 'pea', 'pee', 'peg', 'pen', 'pep', 'per', 'pes', 'pet', 'pew', 'phi', 'pht', 'pic', 'pie', 'pig', 'pin', 'pip', 'pit', 'ply', 'pod', 'pom', 'poo', 'pop', 'pot', 'pow', 'pro', 'pry', 'pub', 'pug', 'pun', 'pup', 'pus', 'put']
score = 1000

#Picks random word for the game, finds its unique letters, starts game
def insertToken():
    print("Welcome to Enigma Machine! \nThe goal is to guess the secret 3 letter word \nThe Enigma Machine will tell you how many letters you got correct \nGood Luck!\n")
    print("(The game is missing a number of 3 letter words starting with words beginning with Q-Z. Choose within range)\n")
    global secretWord
    secretWord = wordBank[r.randint(0, len(wordBank)-1)]
    global secretAlpha
    secretAlpha = list(set(secretWord))
    start(input())


#Checks if input is valid or win
def start(x):
    global userGuess
    global score
    q = 0
    while q is not 1:
        if x == "...":
            userGuess = secretWord
            print("Cheater!")            
            print("The secret word is: ", secretWord)
            retry()
            break;
        elif x not in wordBank:
            print("Not in word bank, try again.\n")
            start(input())
            q = 1
        elif not x.isalpha():
            print("You must enter only letters\n")
            start(input())
            q = 1
        elif x == "print score":
            print(score)
            start()
        elif len(x) < len(secretWord):
            print("Must input a 3 letter word\n")
            q = 1
            start(input())
        elif len(x) == 3:
            userGuess = x
            if userGuess == secretWord:
                print("\nYou win! \nYour grade is:")
                if score // 10 >= 75:
                    print("A+")
                elif score // 10 >= 65:
                    print("A")
                elif score // 10 >= 55:
                    print("B")
                elif score // 10 >= 45:
                        print("C")
                elif score // 10 >= 35:
                    print("D")
                elif score // 10 < 25:
                    print("F \nYou'll do better next time!")
                score = 1000
                retry()
            else:
                q = 1
                check(userGuess)            


#Checks how many letters are in common, if you've won, and tracks score
def check(userGuess):
    global score
    global secretAlpha
    k = 0
    userUnique = list(set(userGuess))
    for x in range(0, len(userUnique)):
        for y in range(0, len(secretAlpha)):
            if userGuess[x] == secretAlpha[y]: 
                k = k+1
    if k > 0:
        score = score - 50
        print("Common letters:", k, "\n")
        start(input())
    else:
        score = score - 50
        print("Common letters:", 0)
        print("")#
        start(input())

    
#Restarts game if you have already won or exits @WHEN NONT Y INPUT ALLOWS NEW GUESSES
def retry():
    print("\nDo you want to play again?\nY for yes, anything else for no")
    token = input()
    if token == 'y':
        print("\nYou're back! Guess the new secret word:")
        initialize()
