import random


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
    global LOWER_BOUND
    global UPPER_BOUND
    global SAMPLE_SIZE

    # Initialize the random generator.
    random.seed()

    # Initialize the sum using further to calculate mean.
    sum_ = 0

    # Start the game SAMPLE_SIZE times.
    for i in range(SAMPLE_SIZE):
        # A number to guess is a random number.
        number = random.randint(LOWER_BOUND, UPPER_BOUND)
        
        # Run prediction algorithm and accumulate the sum.
        sum_ += algorithm(number, False)

    # Calculate the average number of attempts to guess.
    result = sum_ / SAMPLE_SIZE
    print(f'Your algorithm guesses a number on average in {result} attempts')
    return result


def my_algorithm(number, visualize=False):
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

    # Visualize algorithm.
    if visualize:
        print(f'Sequence {predict} to predict {number}')

    # Return amount of attempts to guess.
    return(len(predict))


main(my_algorithm)
