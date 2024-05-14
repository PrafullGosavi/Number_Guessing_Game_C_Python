
import random
num = random.randint(1,100)
nguesses = 0
guess = int(input("enter any number"))
while num != guess:
    if guess<num:
        print("too low")
        guess = int(input("enter the highest number"))
    elif guess>num:
        print("tooo high")
        guess = int(input("enter the lowest number"))
    nguesses += 1
    
print("you guess it right")
print("the number of guesses",nguesses)