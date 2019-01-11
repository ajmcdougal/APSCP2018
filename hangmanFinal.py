health = 10
import random
print "Welcome to Hangman! You can grab a friend, or play on your own!"

'''


Just trying to hide the answers for you guys.



Just hit the run button.






The rest of the code is all the way down there.


Also, fair warning, all 5 of the single-player answers are memes. 

memes I declined to put in:
yobama
smash bros splash screen
gnome - YOU'VE BEEN GNOMED
hIt Or MiSs
ligma (don't look it up)
here comes dat boi
it's pewdiepieeeeeeee


also, don't forget to subscribe to pewdiepie, guys. Almost forgot to tell you.

'''

if raw_input('Type \'solo\' to play on your own, or anything else to play with a friend: ') == "solo":
   draw = random.randint(0,5)
   if draw == 1:
        secret = "thanos car" #thanos car thanos car
   elif draw == 2:
       secret = "big chungus" #that'll hold 'em hehehehe
   elif draw == 3:
       secret = "sans" # y o u ' r e   g o n n a   h a v e   a   b a d   t i m e
   elif draw == 4:
       secret = "lemons" #you don't make lemonade, you make life take the lemons back!!
   else:
       secret = "flex tape" #THAT'S A LOT OF DAMAGE
else:
    secret = raw_input("Put in the secret word: ")
    print " " #this is to (hopefully) make sure the guessing player can't see the answer.
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    print " "
    
print "Alright, now time to begin guessing!"
revealed = []
guessed = set() #I found this little trick online where putting the list as a set will remove duplicates.
while "".join(revealed) != secret:
    guess = raw_input('Type in the letter you guess: ')
    for x in secret:
        if guess == x:
            print "Your guess was correct! Guess again!"
            guessed.add(guess)
    if guess not in secret: #the stuff below this is to determine which part of the hangman is drawn.
            if health == 10:
                draw = "gallows\' base"
            elif health == 9:
                draw = "gallows\' verticle beam"
            elif health == 8:
                draw = "gallows\' horizontal beam"
            elif health == 7:
                draw = "gallows\' support beam"
            elif health == 6:
                draw = "rope"
            elif health == 5:
                draw = "head"
            elif health == 4:
                draw = "torso"
            elif health == 3:
                draw = "left arm"
            elif health == 2:
                draw = "right arm"
            elif health == 1:
                draw = "left leg"
            else:
                draw = "right leg"
            health -= 1 #this will remove one health from the player
            if health < 1: #this will determine if the player is dead yet
                print "Oh no! You've been hanged!"
                print "First time?" #another meme
                import sys
                sys.exit('Game over.') #Ha. You lose. Beautiful.
            
            print "That guess was incorrect. The " + draw + " was drawn."
            
    revealed = []
    for x in secret:    #recycled from week 14 project. Sweeeeeet.
        if x == " ":
                revealed.append(" ")
        elif x not in guessed:
            revealed.append('-')
        else:
            for y in guessed:
                if x == y:
                    revealed.append(y)
    print "".join(revealed) #I love this trick. You can turn lists into strings!

print "Congratulations! You have escaped your hanging!"