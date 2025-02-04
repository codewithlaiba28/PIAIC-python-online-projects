import random
def guess_my_number():
    print("Guess My Number")
    my_number = random.randint(1,99)
    user = int(input("I am thinking of a number between 0 and 99... Enter a guess:" ))
    while user!=my_number:
        if user > my_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low") 
        user = int(input("Enter a guess: "))
    print(f"Congrats! The number was: {my_number}")
guess_my_number()    