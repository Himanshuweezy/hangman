import random
def get_words():
    word=["vodka",
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'duplex',
    'dwarves',
    'equip',
    'faking',
    'fishhook',
    'fixable',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    "onyx",
    "ovary",
    "oxidize"
    "oxygen",
    "pajama",
    "peekaboo",
    "phlegm",
    "pixel",
    "pizazz",
    "pneumonia",
    "polka",
    "pshaw",
    "psyche",
    "puppy",
    "puzzling",
    "quartz",
    "queue",
    "quips",
    "quixotic",
    "quiz",
    "quizzes",
    "quorum",
    "razzmatazz",
    "rhubarb",
    "rhythm",
    "rickshaw",
    "schnapps",
    "scratch",
    "shiv",
    "snazzy",
    "sphinx",
    "spritz",
    "squawk",
    "staff",
    "strength",
    "strengths"
    "stretch",
    "stronghold",
    "stymied",
    "subway",
    "swivel",
    "syndrome",
    "thriftless",
    "thumbscrew",
    "topaz",
    "transcript",
    "transgress",
    "transplant",
    "triphthong",
    "twelfth",
    "twelfths",
    "unknown",
    "unworthy",
    "unzip",
    "uptown",
    "vaporize",
    "vixen",
    "voodoo",
    "vortex",
    "voyeurism",
    "walkway",
    "waltz",
    "wave",
    "wavy",
    "waxy",
    "wellspring",
    "wheezy",
    "whiskey",
    "whizzing",
    "whomever",
    "wimpy",
    "witchcraft",
    "wizard",
    "woozy",
    "wristwatch",
    "wyvern",
    "xylophone",
    "yachtsman",
    "yippee",
    "yoked",
    "youthful",
    "yummy",
    "zephyr",
    "zigzag",
    "zigzagging",
    "zilch",
    "zipper",
    "zodiac",
    "zombie"]
    return random.choice(word)
def main ():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    words=get_words()
    tries=10
    guessed=[]
    continous=False
    print("the letters cointain ",len(words),"characters")
    print("_ "*len(words))
    while continous==False and tries>0:
        print ("you have",tries,"tries left")
        guess=input("Enter a letter or the whoile word")
    #we can have 3 conditions here
    #1 either user input letter
        if len(guess)==1:
            if guess not in alphabet:
                print("Enter a valid character please ")
            elif guess in guessed:
                print("sorry you have already guessed that letter")
            elif guess not in words:
                print("Your guess is wrong")
                guessed.append(guess)
                tries-=1
            elif guess in words:
                print("you guessed the right letter")
                guessed.append(guess)
            else:
                print("What the hell did you do ?")
        #2 oe user input word
        elif len(guess)==len(words):
            if guess==word:
                print("Damn nigga you'\re intelligent. You guessed the word in first try")
                continous=False
            else:
                print("The length of the",guess,"was right but the word is wrong")
                tries=tries-1
        else:
            print("Be careful ",guess,"has ",len(guess),"no of letters but the word given has",len(words),"no. of words")
        game_on=''
        if continous ==False:
            for i in words:
                if i in guessed:
                    game_on=game_on+i
                else:
                    game_on=game_on+"_ "
            print(game_on)
        if game_on==words:
            print("You won the game and saved the guy")
            print("CopyRight © All rights reserved: Himanshu Acharya")
            continous=True
        elif tries == 9:
            print("  --------  ")
        elif tries == 8:
            print("  --------  ")
            print("     O      ")
        elif tries == 7:
            print("  --------  ")
            print("     O      ")
            print("     |      ")
        elif tries == 6:
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        elif tries == 5:
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")
        elif tries == 4:
            print("  --------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        elif tries == 3:
            print("  --------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")
        elif tries == 2:
            print("  --------  ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        elif tries == 1:
            print("Last breaths counting, Take care!")
            print("  --------  ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        elif tries == 0:
            print("You loose")
            print("You let a kind man die")
            print("  --------  ")
            print("     O_|    ")
            print("    /|\      ")
            print("    / \     ")
            print("CopyRight © All rights reserved: Himanshu Acharya")
            continous=True


    #3 or user input word that isnot equal to word
main()
