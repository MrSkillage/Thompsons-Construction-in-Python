# Conor Rabbitte
# Input and Output console 

import regex
import argparse

# Checks to see that we are in the main method
if __name__ == '__main__':
  # cmds stores the argparse Arguements
  cmds = argparse.ArgumentParser()
  # Add a new arugment to cmds called REGEX
  cmds.add_argument("--regex", help="This is used to take in " + 
          "the Regular Expression parameter for the algorithm.")
  # Add a new ardument to cmds called LANG
  cmds.add_argument("--lang", help="This is used to take in " +
          "the Language parameter for the algorithm.")
  # args is equal to the cmds arguments
  args = cmds.parse_args()

# If statement checks if args has been passed an optional regex
if args.regex is not None:
    # Set variable s to the regex argument
    s = args.regex
    # Print s
    print(s)

# Else if statment checks if optional regex hasn't been passed
elif args.regex is None:
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

# If statement checks if args has been passed an optional lang
if args.lang is not None:
    # Set variable x to the language argument
    x = args.lang
    # Print x
    print(x)

# Else if statement checks if optional language hasn't been passed
elif args.lang is None:
  # Boolean variable used to run while loop.
  j = True
  # While loop to check if input is correct.
  while(j):
    # Prompts the user to input language.
    x = input("What's your String? " )
    # Prints the langauge for conformation.
    print(x)
    # Prompts user to answer conformation question.
    y = input("Is this correct? (Y/N) ")
    # If statment breaks loop depending on users conformation.
    if y in ['Y', 'y', 'yes', 'Yes', 'YES']:
      # Breaks loop.
      j = False

# Print the final Expression and Language.
print("The Regular Expression and String are:", s, ",", x)
# Runs the regex method match using the input gathered and stored in s and x.
# Print message if regular expression matches.
if(regex.match(s, x) is True):
  print("Successful Match!")
  print("String:", x, "is found using the Regular Expression:", s)
# Print message id regular expression does not match.
elif(regex.match(s, x) is not True):
  print("Failed Match!")
  print("String:", x, "cannot be found using the Regular Expression:", s)

