
def robot(pos):
    if pos % 3 == 0 and pos % 5 == 0:
        return "fizzbuzz"

    if pos % 5 == 0:
        return "buzz"
    
    if pos % 3 == 0:
        return "fizz"
    
    return str(pos)