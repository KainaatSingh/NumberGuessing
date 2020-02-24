import random
import sys
from argparse import ArgumentParser

def number_generator(min_size, max_size):
    true_number = random.randint(min_size, max_size)
    return true_number

def guess_compare(guess_number, true_number, min_size, max_size):
    if guess_number < min_size or guess_number > max_size:
        print('Your guess is out of range. Try Again!')
    elif guess_number < true_number:
        print('Your guess is lower than the number.\n Go Higher!')
    elif guess_number > true_number:
        print('Your guess is greater than the number.\n Go Lower!')
    else:
        print('CONGRATULATIONS. You Won!')
        sys.exit(0)

def start_game(tries, min_size, max_size):
    true_number = number_generator(min_size, max_size)
    
    for i in range(tries):
        guess_number = input('Enter your guess %d\n', i+1)
        guess_compare(guess_number, true_number, min_size, max_size)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-t', action="store", dest="tries", default=3, help="Define the number of guesses you want", type=int)
    parser.add_argument('-min', action="store", dest="min_size", default=0, help="Define the minimum of the number", type=int)
    parser.add_argument('-max', action="store", dest="max_size", default=sys.maxsize, help="Define the minimum of the number", type=int)

    args = parser.parse_args()

    start_game(args.tries, args.min_size, args.max_size)



