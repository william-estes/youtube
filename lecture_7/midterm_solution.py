def determine_letter_grade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80: 
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'
    

def calculate_average(scores):
    return sum(scores) / len(scores)


def main():
    go_again = True
    while go_again:
        scores = []
        for x in range(5):
            score = int(input(f'Please enter score {x + 1}: '))
            scores.append(score)
        print('SCORE\t|| GRADE')
        for s in scores:
            print(f'{s}%\t|| {determine_letter_grade(s)}')
        avg = calculate_average(scores)
        print(f'The average of the grades is a {avg}% with a letter grade of {determine_letter_grade(avg)}')
        go_again = input('Go again? 1 for yes, anything else for no: ') == '1'

main()