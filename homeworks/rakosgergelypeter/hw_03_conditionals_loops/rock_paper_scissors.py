import random

scores= {
    "Human": 0,
    "Robot": 0,
}

choices = ["rock", "paper", "scissors"]

rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

#amit a gép választ (random)
def computer_choice():
    return random.choice(choices)

#validálja és castolja az input-ot
def round_validator(input_text):
    user_input=0
    while user_input%2==0:
        user_input=input(input_text)
        try:
            return int(user_input)
            break
        except ValueError:
            print(f"Nem jó a formátum: {user_input}")
            continue

#ez teszi lehetővé a választást
def gamer_choices():
    comp_choice=computer_choice()
    while True:
        human_choice=input("Kérem adja meg mit választ:")
        if human_choice in choices:
            break
        else:   
            continue
    return human_choice,comp_choice

#ez dönti el ki fog nyerni és növeli a pontokat
def who_is_the_winner(hum_choice,comp_choice):
    if rules[hum_choice]==comp_choice:
        print("Az ember nyert!")
        scores["Human"]+=1
    elif rules[comp_choice]==hum_choice:
        print("A gépek újra legyőzték az emberiséget!")
        scores["Robot"]+=1
    elif hum_choice==comp_choice:
        print("Döntetlen! Új tippek kellenek.")
        gamer_choices()

#ez delegálja játékot
def start_game(rounds):
    i=0
    #human_choice,computer_choice=gamer_choices()
    while i!=rounds:
        i+=1
        who_is_the_winner(*gamer_choices())
    
def main():
    round=round_validator("Kérem adja meg a körök számát:")
    start_game(round)
    print(scores)

main()