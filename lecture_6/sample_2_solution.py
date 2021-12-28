import random

CHOICES = ('ROCK', 'PAPER', 'SCISSORS')


def get_user_choice():
    user_choice = ''
    while user_choice not in CHOICES:
        user_choice = input('Please enter rock, paper, or scissors: ').upper()
    return user_choice


def determine_winner(comp_choice, user_choice):
    if comp_choice == user_choice:
        print('Tied! Play again!')
    elif comp_choice == 'ROCK':
        if user_choice == 'PAPER':
            print('You have won!')
        elif user_choice == 'SCISSORS':
            print('You have lost!')
    elif comp_choice == 'PAPER':
        if user_choice == 'SCISSORS':
            print('You have won!')
        elif user_choice == 'ROCK':
            print('You have lost!')
    else:
        if user_choice == 'ROCK':
            print('You have won!')
        elif user_choice == 'PAPER':
            print('You have lost!')


def main():
    play_again = True
    while play_again:
        comp_choice = random.choice(CHOICES)
        user_choice = get_user_choice()
        print(f'Computer has chosen {comp_choice}')
        determine_winner(comp_choice, user_choice)
        play_again = input('Play again? 1 = yes, anything else for no: ') == '1'


main()