from get_data.from_sql.queries.select import get_person, get_email
from validate_email import validate_email

def isValidString(text):
    if (not text) or text == "":
        return False

    try:
        for char in text:
            if char not in ['_', '.'] and not char.isalnum():
                return False
    except:
        return False

    return True

def isNotExistPerson(username):
    try:
        if username == get_person(username)[0]:
            return False
    except:
        pass
    return True

def isValidPassword(pwd):
    try:
        if len(pwd) < 8:
            return False
        if not isValidString(pwd):
            return False
    except:
        return False
    return True

def isValidEmail(email):
    try:
        parsedEmail = validate_email(email)
    except:
        return False
    return parsedEmail

def isNotExistEmail(email):
    try:
        email_queried = get_email(email)
    except:
        return False
    try:
        if email == email_queried[0]:
            return False
    except:
        pass

    return True
