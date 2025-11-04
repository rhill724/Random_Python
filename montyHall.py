import random, secrets

# variables to count our wins and losses
wins = 0
losses = 0
# this is just to make our psuedo-random numbers more random
def seedGen():
    seed = secrets.randbelow(10000000)
    random.seed(seed)   
# this is our random number generator returns a value 0-2.
# not 1-3 because arrays count from 0 
def chooseDoor():
    seedGen()
    choosenDoor = random.randrange(0,3)
    return choosenDoor
# plays is how many simulations we want to run  
i = 1
plays = 100001
for i in range(plays):
    doors = ['goat','goat','goat'] # we create an array of 3 doors
    num = chooseDoor()
    doors[num] = 'prize' # we add our prize to one of the doors choosen at random
    num = chooseDoor()
    door = doors[num]   # our contestent now selects a door at random
    if door == 'prize': # if we select the prize door on our first guess then changing our answer causes us to lose
        losses += 1
    else:               # if we choose either of the wrong doors and are shown the other wrong door then changing our guess means we win
        wins += 1       # without even running this we can see that 2/3 of the time it is better to switch our guess
        
print( "Wins = " + str(wins/plays) + " Losses = " + str(losses/plays))
