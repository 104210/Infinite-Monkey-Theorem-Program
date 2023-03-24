from random import choice, randint
from string import ascii_letters, digits, punctuation

chars = ascii_letters + digits + punctuation

while True:
    # Length of resulting code.
    length = randint(1, 100)

    string_code = "".join([choice(chars) for i in range(length)])

    # Theoretically, if this program were to run for an infinite
    # amount of time, then every Python program (with lines less
    # than or equal to 100 characters) will be executed.
    try:
        exec(string_code)
    except:
        pass