import random
import math
# take min and max range of the input values
min_range = int(input("Enter the minimam range value:"))
max_range = int(input("Enter the maximum range value:"))
 
# generating guessing number randomly between the min and max range of values.
guess_number = random.randint(min_range, max_range)
print("The required number to be guessed is:",guess_number)
print("\n\tYou've only ",
       round(math.log(max_range - min_range + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guessing chances.
number_chances = 0
 
# for calculation of minimum number of guesses depends upon range
while number_chances < math.log(max_range - min_range + 1, 2):
    number_chances += 1
 
    # taking guessing number as input
    correct_guess = int(input("Guess a number:- "))
 
    # Condition testing
    if guess_number == correct_guess:
        print("Congratulations you did it in ",
              number_chances, " try")
        # Once guessed, loop will break
        break
    elif guess_number > correct_guess:
        print("You guessed too small!")
    elif guess_number < correct_guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if number_chances >= math.log(max_range - min_range + 1, 2):
    print("\nThe required number to be guessed is %d" % guess_number)
    print("\tTry again!")
 