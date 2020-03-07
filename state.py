# Conor Rabbitte
# Thomspon Construction Classes

class State:
    # Every state has (0, 1, or 2) edges from it
    edges = []
    
    # Label for the arrows. None means epsilon.
    label = None

     # Constructor for the class.
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

class Fragment:
    # Start state of NFA Fragment.
    start = None
    # Accept state of NFA Fragment.
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    # Convert input to a stack-ish list.
    infix = list(infix)[::-1]

    # Operator
    opers = []

    # Output list.
    postfix = []

    # Operator precedence.
    prec = {'*' : 100, '.' : 80, '|' : 60, ')' : 12, '(' : 11}

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

    # Returns the postfix 
    return ''.join(postfix)

# Used to compile infix into postfix
def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # Pop two fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Point frag2's accpet state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            # Create new instance of fragment to represent new NFA
            newFrag = Fragment(frag2.start, frag1.accept)
            # Push new NFA back to nfa_stack
            nfa_stack.append(newFrag)
        elif c == '|':
            # Pop two fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            # Point the old accept States at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            # Create new instance of fragment to represent new NFA
            newFrag = Fragment(start, accept)
            # Push new NFA back to nfa_stack
            nfa_stack.append(newFrag)
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new start and accpet States
            accpet = State()
            start = State(edges=[frag.start, accpet])
            # Point arrows
            frag.accept.edges = [frag.start, accpet]
            # Create new instance of the Fragment to represent NFA
            newFrag = Fragment(start, accept)
            # Push new NFA back to nfa_stack
            nfa_stack.append(newFrag)
        else:
            accept = State()
            start = State(label=c, edges=[accept])
            newFrag = Fragment(start, accept)
            nfa_stack.append(newFrag)

    # The NFA stack should have exactly one NFA on it, the answer.
    return nfa_stack.pop()

# Will return true if regex is (Fully) equal to the String s, else false
def match(regex, s):
    # Compile the regular expression into an NFA
    nfa = regex_compile(regex)
    # Ask the NFA if it matchs the String s
    return nfa

# Test if the match function works!
print(match("a.b|b*", "bbbbbbb"))

