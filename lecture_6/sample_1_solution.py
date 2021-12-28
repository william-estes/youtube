import random

COLORS = ('RED', 'GREEN', 'BLUE', 'ORANGE', 'YELLOW')


def get_user_color():
    user_choice = ''
    print(f'Available colors: {COLORS}')
    while user_choice not in COLORS:
        user_choice = input('Please enter a color: ').upper()
    return user_choice


def main():
    correct_guesses = 0
    for x in range(10):
        print(f'\nRound {x + 1}...')
        comp_color = COLORS[random.randint(0, len(COLORS) - 1)]
        user_color = get_user_color()
        print(f'Computer selected {comp_color}')
        if comp_color == user_color:
            correct_guesses += 1
    print(f'\nUser guessed correctly {correct_guesses} times')

main()