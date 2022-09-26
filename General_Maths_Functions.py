def numbercheck(number):
    try:
        float(number)
    except:
        return False
    else:
        return True

def intcheck(number):
    try:
        float(number)
    except:
        return False
    else:
        return float(number).is_integer()

def intinator(number):
    if numbercheck(number):
        if float(number).is_integer():
            return int(number)
        else:
            return float(number)
    else:
        raise ValueError("Requires a 'float' or 'int' object")

def ezinput(msg):
    return input(msg).strip().lower()