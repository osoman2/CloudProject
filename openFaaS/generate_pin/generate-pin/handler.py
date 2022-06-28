import string
import secrets

def handle(req):
    LEN = 6
    alphabet = string.digits

    while True:
        password = ''.join(secrets.choice(alphabet)
                               for i in range(LEN))
        if any(c.isdigit() for c in password):
            break

    return password
