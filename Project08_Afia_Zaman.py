import Roulette

def main():
   SPUN_NUMBER = Roulette.spin_the_wheel()

# Ask the user what kind of bet they want to make
   BET = input("What type of bet (color/number/parity)? ")

# Check if the bet color has won and print it
   if BET == "color":
      bet_color = input("What color (black/red)? ")
      if bet_color == Roulette.color_won(SPUN_NUMBER, bet_color):
         print("\nYou won the color bet on", bet_color)
      else:
         print("\nDefeated! Better luck next time.")

# Check if the bet number has won and print it
   elif BET == "number":
      bet_number = int(input("What number are you guessing? (1-36) "))
      if bet_number == Roulette.number_won(SPUN_NUMBER, bet_number):
         print("\nYou won the number bet on", bet_number)
      else:
         print("\nDefeated! Better luck next time.")

# Check if the bet parity has won and print it
   elif BET == "parity":
      bet_parity = input("What parity(odd/even)? ")
      if bet_parity == Roulette.parity_won(SPUN_NUMBER, bet_parity):
         print("\nYou won the parity bet on", bet_parity)
      else:
          print("\nDefeated! Better luck next time.")

main()

