import random

def welcome():
    print('Welcome to this funny game')
    print('You have to guess a number between 1 and 20')
    print()

def win(computer_number , guess):
    return computer_number == guess

def answer(computer_number, guess):
    if computer_number > guess:
        print('The number is higher')
    elif computer_number < guess:
        print('The number is lower')
    else:
        print('You guessed it!')

def get_guess():
    ans = input('Guess a number between 1 and 20: ')
    return int(ans)

def finish(number , count):
    print('Good game!')
    print(f'My number was {number} and you found it in {count} tries.')
    again = input('Do you want to play again? (yes/no): ').strip().lower()
    return again == 'yes'
 
welcome()
continue_game = True
while continue_game:
    computer_number = random.randint(1, 20)
    guess = 0
    count = 0
    while not win(computer_number, guess):
        guess = get_guess()
        count += 1
        answer(computer_number , guess)
    continue_game = finish(computer_number , count)




    