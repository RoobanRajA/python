import random;

choices=('r','p','s');

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s):").lower();

        if user_choice in choices:
            return user_choice;
        else:
            print("Invalid choice!");
            
def display_choice(user_choice,computer_choice):
    print(f'You choose {user_choice}');
    print(f'Computer choose {computer_choice}');

def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Tie!");
    elif(
        (user_choice =='r' and computer_choice =='s') or
        (user_choice =='p' and computer_choice =='r') or
        (user_choice =='s' and computer_choice =='p')):
        print("You win");
    else:
        print("You lose");

def game_play():
    while True:
        user_choice=get_user_choice();
        computer_choice=random.choice(choices);
        
        display_choice(user_choice,computer_choice);
        
        winner(user_choice,computer_choice);
        
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break;
        
game_play();