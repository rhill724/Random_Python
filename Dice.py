import random
import secrets

two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

def seedGen():
    seed = secrets.randbelow(10000000)
    random.seed(seed)
    
    
def rollDice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    roll = die1 + die2
    return roll
    

i = 1
for i in range(40000):
    seedGen()
    roll = rollDice()
    if roll == 2:
        two = two + 1
    if roll == 3:
        three = three + 1
    if roll == 4:
        four = four + 1
    if roll == 5:
        five = five + 1
    if roll == 6:
        six = six + 1
    if roll == 7:
        seven = seven + 1
    if roll == 8:
        eight = eight + 1
    if roll == 9:
        nine = nine + 1
    if roll == 10:
        ten = ten + 1
    if roll == 11:
        eleven = eleven + 1
    if roll == 12:
        twelve = twelve + 1
        
strRoll = str(two) + ',' + str(three) + ',' + str(four) + ',' + str(five) + ',' + str(six) + ',' + str(seven) + ',' + str(eight) \
+ ',' + str(nine) + ',' + str(ten) + ',' + str(eleven) + ',' + str(twelve)

print(strRoll)
print("2,3,4,5,6,7,8,9,10,11,12")

    
    
    
    
