import pyjokes
SORRY_MESSAGE = "Sorry! I can only tell jokes. Type 'joke' to hear one."
def bot():
    user_input = input("What you want: ").strip().lower() 
    if "joke" in user_input:  
        for _ in range(5):
            print(pyjokes.get_joke())
    else:
        print(SORRY_MESSAGE)

bot()
