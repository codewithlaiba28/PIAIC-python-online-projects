import random
print("Welcome to the High-Low Game!")
print("_" *100)
score=0

for i in range(1 , 5 +1):
    print(f"Round {i}")
    my_random_number:int = random.randint(1,100)
    computer_random_number:int = random.randint(1,100)
    print(f"Your number is {my_random_number}")
    user_guess=input("Do you think your number is higher or lower than the computer's?:") .strip() .lower()

    if(user_guess == "higher" and my_random_number > computer_random_number) or(user_guess == "lower" and my_random_number < computer_random_number):
        print(f"You were right! The computer's number was {computer_random_number}")
        score += 1
        
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_random_number}")  
    print(f"Your score is now {score} \n")
if score <=5 and score >=3:
    print(f"Your score is now {score}") 
    print("Wow! You played perfectly!")
elif score ==2:
    print("Your score is now 2")
    print("Good job, you played really well!") 
else:
    print("Your score is now 1")
    print("Better luck next time!")          
print("Thanks for playing!")          

