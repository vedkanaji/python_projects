import random
import string
print('Welcome to random password generator')
def get_password(n):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    strong_password = lower + upper + digit + symbol
    password = ''.join(random.sample(strong_password, n))
    print('Your password is ', password)


get_password(8)




