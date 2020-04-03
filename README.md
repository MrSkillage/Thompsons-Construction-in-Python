# Thompson's Construction in Python

## Introducion
This is my 3rd year project in Graphy Theory.  This is a program written in python turning a regular expression into a NFA (Non-Deterministic Finite Automaton) using Thompson's Contruction Algorithm.  This is then used to check if the NFA can be used to match a string against the regular expression.

## How To Use
When you download the Git-Repo you will be presented with a number of files.  The only files necessary to run the program are input.py and regex.py.

**Note:** When you wish to use the expression 'ab' use 'a.b' instead.  The program is designed in such a way as 'ab' will not be recognised as 'a.b' *you need to explicity say* 'a.b'.  
> The regular expression '(ab)|b*' will not be recognised and cause an error.  Instead use the regular expression '(a.b)|b*'
> The regular expression 'fe?d' will not be recognised and cause an error. Instead use the regular expression 'f.e?.d'

1. Run input.py using python3 input.py in your command line.
2. You will be prompted with the following message "What's your regular Expression?" where you can input the regular expression you wish to use.
3. You will be shown what you have entered and asked is this correct.  If it is you may enter any of the follow: ['Y', 'y', 'yes', 'Yes', 'YES'].  If it is not correct you may enter any other key and it will prompt you to enter your regular expression again.
4. You will be prompted with the following message "What's your String?" where you can input the string you wish to use.
5. You will be shown what you have entered and asked is this correct, then follow step 3 again.
6. You will be shown 3 different messages.  The first is the regular expression and the string you are using divided by a ','.  The second is a Success or Failure message.  The third will show the string you used and what regular expression it has match with.

### Exmaple Usage:
1. python3 input.py
2. (a.b)|b*
3. YES
4. bbbbbbbbbbbbbbbb
5. y
6. "Success or Failure Message!"

## Research
