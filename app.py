secret_number = 8
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('guess '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else:
    print('Sorry, You Failed!')