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

### Run 3: Using command-line arguments to run the entire program.
The program can be run entirely or partially by using command-line arguments passing the regular-expression and string as arguments.  If you run python3 input.py --help ![Imgur](https://i.imgur.com/EcNmsNQ.png) you will be shown the two optional arguments that you can use inconjunction with python3 input.py.
![Imgur](https://i.imgur.com/M9KP1Hk.png)

You can then run python3 input.py --regex "(a?.b).c" --lang "abc", being sure you use double quotes "" to format your regular-expression and language-string into a String for the programs ease.
![Imgur](https://i.imgur.com/FJKsXHr.png)

Hitting enter you will then be presented with the programs finished execution without have to run through the original program like above.

![Imgur](https://i.imgur.com/kDDdCdb.png)

### Run 4: Using command-line arguments to run part of the program.
The program can be run entirely or partially by using command-line arguments passing the regular-expression and string as arguments.  If you run python3 input.py --help ![Imgur](https://i.imgur.com/EcNmsNQ.png) you will be shown the two optional arguments that you can use inconjunction with python3 input.py.
![Imgur](https://i.imgur.com/M9KP1Hk.png)

You can then run the python3 input.py --regex "(a?.b).c", being sure you use double qoutes "" to format your regular-expression into a String for the programs ease.
![Imgur](https://i.imgur.com/U0gEcfy.png)

You will then be prompted, as seen in Run 1, for the String.  You can then enter into the program 'abc' and hit enter.  You will then be shown a comformation message in whihc you can enter any of the follow answers: ['Y', 'y', 'yes', 'Yes', 'YES'].  However, if you have not entered it correctly you may enter any other key and it will prompt you to re-enter your regular expression again.

![Imgur](https://i.imgur.com/U4wSYqy.png)

Finally you will be display with the Success message at the end of the programs execution.
![Imgur](https://i.imgur.com/5IPDg8y.png)

## Testing
The testing for this program is simply done by using the assert function.  Inside of the test.py file is a dictionary list of hardcoded tests used to verify the accuracy of the regex.match function.  Each of theses tests contain 3 bits of information. The first two are the regular expression and string, respectively. The third is a boolean of either True or False used to store the expected outcome of the regex.match function. The program then runs through and asserts each of the tests found inside of the dictionary list. Then a print statement is used to show the user what has been tested and if they string has matched the regular expression.  
![Imgur](https://i.imgur.com/k51EUSM.png)

## Research
I have done some extra research on this project beyond the minimal requirements and will feature them here:
- The project required the use of 3 regular expression operators: Kleene Star (*), Concatenate (.), and OR (|).  I have add extra to this including the ? and + operators with functionality.  I used this website [here](https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html#Regexp-Operators) to help understand its functions and its precedence.
- In order to check the validity of the regular expression matching the strings tested, I used the [Regex101](https://regex101.com/).  This was very helpful in testing and used to test multiple strings that would match the regular expression.
- I used the [RealPython](https://realpython.com/) to futher my knowledge on the python language.  These subjects included but were not limited to: input & output, conditionally statments, importing files, dictionaries, and function design.
- By far the most important and usful website I used was another [Git-Repo](https://cyberzhg.github.io/toolbox/regex2nfa). The user CyberZHG was extremely helpful in understanding and visualzing an regular expression turned into a NFA.  This came in handy when trying to program the ? and  + operators as it allowed me to see a visual representation of the NFA.
- I used the [Python](https://www.python.org/dev/peps/) website to research suggested PEP guidelines.  After reading through the PEP 8 I did my best to adhere to the guidelines.


