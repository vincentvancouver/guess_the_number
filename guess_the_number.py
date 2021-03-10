
def game():
    import random
    while True:
        x = input('You have 5 attempts to guess the number.\nWould you like to play? (y/n) ')
        while x == 'y':
            num1 = random.randint(1, 100)
            count = 5
            while count >= 1:
                if count > 1:
                    print(f'You have {count} guesses left')
                else:
                    print(f'You have {count} guess left')
                usr = int(input('Guess the number between 1 - 100 '))
                count -= 1
                if usr == num1:
                    print('Well done, you guessed correctly!')
                    if input('Would you like to play again/ (y/n) ') == 'y':
                        x = 'y'
                        break
                    else:
                        x = 'n'
                        break
                elif count == 0:
                    print(f'\nBad luck.\nThe answer was {num1}\n')
                    if input('Would you like to play again/ (y/n) ') == 'y':
                        continue
                    else:
                        x = 'n'
                elif usr in range(num1-5, num1+6):
                    print('You are within 10\n')
                    if usr > num1:
                        print('Lower\n')
                    else:
                        print('Higher\n')
                    continue
                else:
                    if usr > num1:
                        print('Lower\n')
                    else:
                        print('Higher\n')
                    continue
        if x == 'n':
            print('OK then.')
            break
        else:
            continue

game()