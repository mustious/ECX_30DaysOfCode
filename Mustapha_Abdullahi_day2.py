import string
import random


def password_generator(password_len: int):
    """
    Generates a random alphanumeric password based on desired length of password

    :param password_len: desired length of password
    :var alpha_num: string of alphanumeric characters
    :type alpha_num: str
    :return: password: generated password
    :rtype: str
    """

    password = ""
    alpha_num = string.ascii_letters + string.digits

    if password_len < 8:
        print("passwork is weak... choose atleast a password of length 8")
    else:
        for element in range(0, password_len):
            password += random.choice(alpha_num)
        return password