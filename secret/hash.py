import hmac
from hashlib import sha256
from secret.confidential import TOKEN

def generate_new_token(pwdSize=100):
    import string
    import random
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase

    token = ''.join((random.choice(chars)) for x in range(pwdSize))
    return token

def encoded(content):
    return hmac.HMAC(str.encode(TOKEN), str.encode(content), digestmod=sha256).hexdigest()
