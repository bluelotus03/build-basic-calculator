
# This is a basic calculator program built with python
# It does not currently ensure numbers and operators are in the correct format when input, so if you want to enjoy the program, make sure you input numbers and operators that are allowed and at the right place <3

# ------------FUNCTIONS-----------------------------------
# Welcome function
def welcomeMsg():
  print("\nHello! Welcome to our basic calculator with Python <3")
  print("\nCurrently, we support the following operations for 2 numbers at a time:\nAddition, Subtraction, Division, Multiplication")

# Function to do the calculations
def calculationTime():
  
  # Takes user input for 2 numbers and an operator 
  num1 = float(input("\n\nEnter a number: "))
  operator = input("\nEnter the operation: ")
  num2 = float(input("\nEnter another number: "))

  # Perform the correct operation based on user's input
  if operator == "+":
    result = (num1) + (num2)

  elif operator == "-":
    result = (num1) - (num2)

  elif operator == "/":
    result = (num1) / (num2)

  elif operator == "*":
    result = (num1) * (num2)

  # Print both numbers, the operator, and the result 
  print("\n", num1, operator, num2, "=", result)

# Ask the user to go again and return their answer
def goAgainQ():
  goAgain = input("\nWant to go again? (Y|N) ").lower()
  return goAgain

# ------------MAIN PROGRAM-----------------------------------
# By default when the program starts, set goAgain to y for yes
goAgain = 'y'

# Print the welcome message
welcomeMsg()

# While the user does not enter n for going again question
while goAgain != 'n':
  # Call the function for calculations
  calculationTime()
  # At end of calculation results, ask user if they want to go again and assign the input returned to the yORn variable
  yORn = goAgainQ()
  # While user input is not 'y' or 'n,' tell them that's not valid input for this question and ask ask the question again
  while yORn !='y' and yORn !='n':
    print("\nSorry friend, that doesn't seem to be a Y or N")
    yORn = goAgainQ()
  # If user inputs 'n,' print goodbye msg and end program  
  if yORn == 'n':
    print("\nIt was great having you here!\nHope to see you soon! 00\n")
    break
  
