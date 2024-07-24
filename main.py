import random


def guess():
    x = int(input("range of number from 1 to "))
    random_number = random.randint(1, x)
    # print( f"random_number: {random_number}")
    guess = 0
    while (guess != random_number):
        guess = int(input(f" guess a number between 1 and {x}:" ))
        if(guess < random_number):
            print(" guess number is less than randomnumber")
        else:
            print("guess number is greater than random number")
    print("you correctly guessed random numeber:", random_number)

def computer_guess():
    print("Lets play computer guess game")
    low = int(input("enter lowest no: "))
    high = int(input("enter highest no: "))
    magic_number = int(input(f"user please enter magic number between {low} to {high} "))
    guess_number = random.randint(low, high)
    while(guess_number != magic_number):
        if(magic_number > guess_number):
            print(f'Sorry, guess number {guess_number} is low')
            guess_number = random.randint(guess_number, high)
        else:
            print(f"Sorry, guess number {guess_number} is too high")
            guess_number = random.randint(low, guess_number)
    print(f"congratulation computer you have guessed correct magic number : {magic_number}")

def computer_guess1():
    print("Lets play computer guess game")
    low = int(input("enter lowest no: "))
    high = int(input("enter highest no: "))
    magic_number = int(input(f"user please enter magic number between {low} to {high}: "))
    guess_number = random.randint(low, high)
    feedback = " "
    while(feedback != "C"):
       feedback = input(f"guess number {guess_number} is it High (H), low (L) or correct (C) ")
       if(feedback == "L"):
        low = guess_number 
       elif(feedback == "H"):
        high = guess_number   
       elif(feedback == "C"):
        print(f"correctly guessed")
       guess_number = random.randint(low,high) 
    print(f"congratulation computer you have guessed correct magic number : {magic_number}")


    
# guess()
computer_guess1()
