import re


def is_Nigerian(phone_num: str):
    """
    Funtion tests where a phone number is a nigeria phone
    by testing wheter it starts with the following characters: "+234", "234", "070", "080"

    :param phone_num: phone number to be tested if nigerian
    :var pattern: a regex pattern for nigerian numbers
    :type pattern: str
    :var test: result of re.Match class
    :return: bool
    :rtype: bool
    """
    pattern = r"^([\+]*234)|(0[78]0)"
    print(type(pattern))
    test = re.match(pattern, phone_num)
    print(type(test))
    if test:
        return bool(test)
    return bool(test)
