import random
jackpot = random.randint(1,100)

guess = int(input("guess the number"))
attampt = 1
while guess != jackpot:
   
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input("guess agin"))
    attampt+=1
print(jackpot)
print("guess is correct")
print("your attampt",attampt)