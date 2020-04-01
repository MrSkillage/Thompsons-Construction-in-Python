# Conor Rabbitte
# Input and Output console 

# Boolean variable used to run while loop.
i = True
# While loop to check if input is correct.
while(i):
  # Prompts the user to input regular expression.
  s = input("What's your Regular Expression? ")
  # Prints the regular expression for conformation.
  print(s)
  # Prompts user to answer conformation question.
  a = input("Is this correct? (Y/N) ")
  # If statement breaks loop depending on users conformation.
  if a == "Y" or "y":
    # Breaks loop.
    i = False

# Boolean variable used to run while loop.
i = True
# While loop to check if input is correct.
while(i):
  # Prompts the user to input language.
  x = input("What's you language? " )
  # Prints the langauge for conformation.
  print(x)
  # Prompts user to answer conformation question.
  y = input("Is this correct? (Y/N) ")
  # If statment breaks loop depending on users conformation.
  if a == "Y" or "y":
    # Breaks loop.
    i = False

# Print the final Expression and Language.
print("The Expression and Language are:", s, x)
