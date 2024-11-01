import random

correctNumber = random.randint(1, 20)
print("Choose a number between 1 and 20")
guessNumber = 1
guess = 0

for guessNumber in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < correctNumber:
        print('Your guess is too low')
    elif guess > correctNumber:
        print('Your guess is too high')
    else:
        break

if guess == correctNumber:
   print('Good job! You guessed my number in ' + str(guessNumber) + ' guesses!')
else:
   print('You Lose! The correct number to win was ' +str(correctNumber))