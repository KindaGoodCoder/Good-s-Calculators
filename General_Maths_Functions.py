def numbercheck(number):
    try:
        float(number)
    except:
        return False
    return True

def intcheck(number):
    try:
        float(number)
    except:
        return False
    return float(number).is_integer()

def floatcheck(number):
    return True if numbercheck(number) and not intcheck(number) else False        

def intinator(number,roundby=2):
    number = round(float(number),roundby)
    if number.is_integer():
        return int(number)
    return number

def ezinput(msg):
    return input(msg).strip().lower()