import random
print("Number guessing game")
number = random.randint(1,9)
chances = 0
while(chances<5):
    chances = chances+1
    guess = int(input("Enter your guess"))
    if(guess == number):
        print("Congratulations! You won.")
        break
    elif(guess<number):
        print("Your number is too less")
    else:
        print("Your guess was too high.")
if not chances<5:
    print("You lose. The number is", number)