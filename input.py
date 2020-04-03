# Conor Rabbitte
# Input and Output console 

import regex

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
  if a in ['Y', 'y', 'yes', 'Yes', 'YES']:
    # Breaks loop.
    i = False

# Boolean variable used to run while loop.
j = True
# While loop to check if input is correct.
while(j):
  # Prompts the user to input language.
  x = input("What's you language? " )
  # Prints the langauge for conformation.
  print(x)
  # Prompts user to answer conformation question.
  y = input("Is this correct? (Y/N) ")
  # If statment breaks loop depending on users conformation.
  if y in ['Y', 'y', 'yes', 'Yes', 'YES']:
    # Breaks loop.
    j = False

# Print the final Expression and Language.
print("The Expression and Language are:", s, x)
# Runs the regex method match using the input gathered and stored in s and x.
# Print message if regular expression matches.
if(regex.match(s, x) is True):
  print("Successful Match!")
  print("Language:", x, "is found using the Regular Expression:", s)
# Print message id regular expression does not match.
elif(regex.match(s, x) is not True):
  print("Failed Match!")
  print("Language:", x, "cannot be found using the Regular Expression:", s)

