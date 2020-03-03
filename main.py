import random
from statistics import mean


# Lower and upper bounds of numbers to guess.
LOWER_BOUND = 1
UPPER_BOUND = 100
# Number of samples of uniform pseudo random distribution
# used to estimate algorithm efficiency.
SAMPLE_SIZE = 10000


def main(algorithm):
    """Estimate the algorithm efficiency.

    Start the game for SAMPLE_SIZE times to estimate algorithm
    efficiency - average number of attempts to guess.
    """
    print('Checkout and main changes')
    print('New main changes')
    print('Checkout and test branch changes')

    global LOWER_BOUND
    global UPPER_BOUND
    global SAMPLE_SIZE

    # Initialize the random generator.
    random.seed()

    # Fill the list of numbers to guess.
    guess_numbers = [random.randint(LOWER_BOUND, UPPER_BOUND)
                     for i in range(SAMPLE_SIZE)]

    # Start the game many times.
    attempts = []
    for number in guess_numbers:
        attempts.append(algorithm(number))

    # Calculate the average number of attempts to guess.
    result = mean(attempts)
    print(f"Your algorithm guesses a number on average in {result} attempts")
    return result


def my_algorithm(number):
    """Rules of the game and playing algorithm.

    The function generates the numbers and check either it is less
    or more or equal to the guess number.  The generation algorithm
    is based on binary search or dichotomy (devision by two).
    Returns the amount of attempts to guess the number.
    """
    global LOWER_BOUND
    global UPPER_BOUND

    # Current bounds of the number.
    lower, upper = LOWER_BOUND, UPPER_BOUND
    # List of predictions.
    predict = []
    
    while True:
        # Get new prediction.
        predict.append((lower + upper) // 2)
        
        # Check prediction.
        if number > predict[-1]:
            lower = predict[-1] + 1     # Update lower bound
        elif number < predict[-1]: 
            upper = predict[-1] - 1     # Update upper bound
        else:
            break                       # Exit if guess

    # Return amount of attempts to guess
    return(len(predict))


main(my_algorithm)
