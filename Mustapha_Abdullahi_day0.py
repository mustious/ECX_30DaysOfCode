def word_score(word: str):
    """"
    returns the total score based on points associated with each letter

    :param word: string which score is to be computed
    :type word: str
    :return total_score
    :rtype int
    """
    word = word.lower()
    points = {
        "1": ["a", "e", "i", "l", "n", "o", "r", "s", "t", "u"],
        "2": ["d", "g"],
        "3": ["b", "c", "m", "p"],
        "4": ["f", "h", "v", "w", "y"],
        "5": ["k"],
        "8": ["j", "x"],
        "10": ["q", "z"]
    }
    total_score = 0
    for letter in word:
        for key, item in points.items():
            if letter in item:
                total_score += int(key)

    return total_score
