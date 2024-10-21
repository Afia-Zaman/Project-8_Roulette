import random

# Determine random numbers between (1-36)
def spin_the_wheel():
    return random.randint(1, 36)

# Determine color of a spot
def determine_color(SPUN_NUMBER):
    if (SPUN_NUMBER >= 1 and SPUN_NUMBER <= 10) or (SPUN_NUMBER >=19 and SPUN_NUMBER <=28):
        if SPUN_NUMBER % 2 == 0:
            return "black"
        else:
            return "red"
    else:
        if SPUN_NUMBER % 2 == 0:
            return "red"
        else:
            return "black"

# Determine parity of the spun number
def determine_parity(SPUN_NUMBER):
    if SPUN_NUMBER % 2 == 0:
        return "even"
    else:
        return "odd"

# Determine if the bet color has won
def color_won(SPUN_NUMBER, bet_color):
    spun_color = determine_color(SPUN_NUMBER)
    return bet_color == spun_color

# Determine if the bet number has won
def number_won(SPUN_NUMBER, bet_number):
    return bet_number == SPUN_NUMBER

# Determine if the bet parity has won
def parity_won(SPUN_NUMBER, bet_parity):
    spun_parity = determine_parity(SPUN_NUMBER)
    return bet_parity == spun_parity



