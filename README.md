# Thompson's Construction in Python

## Introducion
This is my 3rd year project in Graphy Theory.  This is a program written in python turning a regular expression into a NFA (Non-Deterministic Finite Automaton) using Thompson's Contruction Algorithm.  This is then used to check if the NFA can be used to match a string against the regular expression.

## How To Use
When you download the Git-Repo you will be presented with a number of files.  The only files necessary to run the program are input.py and regex.py.

**Note:** When you wish to use the expression 'ab' use 'a.b' instead.  The program is designed in such a way as 'ab' will not be recognised as 'a.b' *you need to explicity say* 'a.b'.  
> The regular expression '(ab)|b*' will not be recognised and cause an error.  Instead use the regular expression '(a.b)|b*'
> The regular expression 'fe?d' will not be recognised and cause an error. Instead use the regular expression 'f.e?.d'

### Run 1: Simple run with Success

Run input.py using python3 input.py in your command line.
![Imgur](https://i.imgur.com/SipeKsH.png)

You will be prompted with the following message "What's your regular Expression?" where you can input the regular expression (a.b)|b*.  You will be shown what you have entered and asked is this correct.  Then enter any of the follow answers: ['Y', 'y', 'yes', 'Yes', 'YES'].  However, if you have not entered it correctly you may enter any other key and it will prompt you to re-enter your regular expression again.
![Imgur](https://i.imgur.com/JYcg7jl.png)

You will be prompted with the following message "What's your String?" where you can input the string bbbb.  You will be shown what you have entered and asked is this correct, as stated previously above.
![Imgur](https://i.imgur.com/A2tP4fo.png)

You will be shown 3 different messages.  The first is the regular expression and the string you are using divided by a ','.  The second is a Success message.  The third will show the string you used and what regular expression it has matched with.
![Imgur](https://i.imgur.com/Vi3dHKm.png)

### Run 2: Simple run with Failure

Run input.py using python3 input.py in your command line.
![Imgur](https://i.imgur.com/SipeKsH.png)

You will be prompted with the following message "What's your regular Expression?" where you can input the regular expression (a.b)|b*.  You will be shown what you have entered and asked is this correct.  Then enter any of the follow answers: ['Y', 'y', 'yes', 'Yes', 'YES'].  However, if you have not entered it correctly you may enter any other key and it will prompt you to re-enter your regular expression again.
![Imgur](https://i.imgur.com/JYcg7jl.png)

You will be prompted with the following message "What's your String?" where you can input the string aabb.  You will be shown what you have entered and asked is this correct, as stated previously above.
![Imgur](https://i.imgur.com/8Vkrrsb.png)

You will be shown 3 different messages.  The first is the regular expression and the string you are using divided by a ','.  The second is a Failure message.  The third will show the string you used and what regular expression it has not matched with.
![Imgur](https://i.imgur.com/0OtD8DC.png)

## Testing


## Research
I have done some extra research on this project beyond the minimal requirements and will feature them here:
- The project required the use of 3 regular expression operators: Kleene Star (*), Concatenate (.), and OR (|).  I have add extra to this including the ? and + operators with functionality.  I used this website [here](https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html#Regexp-Operators) to help understand its functions and its precedence.
- In order to check the validity of the regular expression matching the strings tested, I used the [Regex101](https://regex101.com/).  This was very helpful in testing and used to test multiple strings that would match the regular expression.
- I used the [RealPython](https://realpython.com/) to futher my knowledge on the python language.  These subjects included but were not limited to: input & output, conditionally statments, importing files, dictionaries, and function design.
- By far the most important and usful website I used was another [Git-Repo](https://cyberzhg.github.io/toolbox/regex2nfa). The user CyberZHG was extremely helpful in understanding and visualzing an regular expression turned into a NFA.  This came in handy when trying to program the ? and  + operators as it allowed me to see a visual representation of the NFA.
- I used the [Python](https://www.python.org/dev/peps/) website to research suggested PEP guidelines.  After reading through the PEP 8 I did my best to adhere to the guidelines.


