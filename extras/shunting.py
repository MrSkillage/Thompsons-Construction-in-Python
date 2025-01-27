# Conor Rabbitte G00365218
# The Shunting Yard Algorithm for regular expressions.

# The input
infix = "(a|a.b)c*(b?d)e+"
print("Input is: ", infix)
# Expected output "ab|c*."
print("Expected:  ab|c*.")

# Convert input to a stack-ish list.
infix = list(infix)[::-1]

# Operator
opers = []

# Output list.
postfix = []

# Operator precedence.
prec = {'*':100, '+':90, '?':80, '.':70, '|':60, ')':20, '(':10}

# Loop through the input one character at a time.
while infix:
    # Pop a character from the input.
    c = infix.pop()

    # Decide what to do based on the character.
    if c == '(':
        # Push an open bracket to the opers stack
        opers.append(c)
    elif c == ')':
        # Pop the operators stack until you find an (.
        while opers[-1] != '(':
            postfix.append(opers.pop())
        # Get rid of the '('
        opers.pop()
    elif c in prec:
        # Push any operators on the opers stack with higher prec to the output.
        while opers and prec[c] < prec[opers[-1]]:
            postfix.append(opers.pop())
        # Push c to the operator stack
        opers.append(c)
    else:
        # Typically, we just push the character to the output.
        postfix.append(c);

# Pop all poerators to the output.
while opers:
    postfix.append(opers.pop())

# Convert ouput list to string.
postfix = ''.join(postfix)

# Print the result.
print("Output is: ", postfix)

