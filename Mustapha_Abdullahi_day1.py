def guessingGame(num_guesses: int, target_num: int):
    """
    Based on the guessing game which allow for a number of guesses to
    get as close to the answer as possible

    :param num_guesses: number of guess permissible
    :param target_num: actual value
    :var guess_num: current guess
    :rtype guess_num: int
    :var diff: difference between the final guess and actual value
    :rtype diff: int
    :return: diff:
    """

    for i in range(0, num_guesses):
        guess_num = input("Guess the number I'm thinking about? ")
        diff = target_num - int(guess_num)

        if diff == 0:
            print("You guess right!")
            return diff
        elif diff > 0:
            print("Thinking... it is higher than your guess")

        else:
            print("Thinking... it is lower than your guess")

    return diff