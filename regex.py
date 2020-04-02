# Conor Rabbitte
# Thomspon Construction Classes

class State:
  # Constructor used to define State edges and labels.
  def __init__(self, label=None, edges=None):
    # Every state has (0, 1, or 2) edges from it.
    self.edges = edges if edges else []
    # Label for the edges. None means epsilon.
    self.label = label

class Fragment:
  # Constructor used to define Fragment start and accept states.
  def __init__(self, start, accept):
    # Start state of NFA Fragment.
    self.start = start
    # Accept state of NFA Fragement.
    self.accept = accept

def shunt(infix):
  # Convert input to a stack-ish list.
  infix = list(infix)[::-1]

  # Operator
  opers = []

  # Output list.
  postfix = []

  # Operator precedence.
  prec = {'*':100, '+':90, '?':80, '.':70, '|':60, ')': 40, '(': 20}

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

  # Pop all operators to the output.
  while opers:
    postfix.append(opers.pop())

  # Returns the postfix 
  return ''.join(postfix)

# Used to compile infix into postfix
def compile(infix):
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
      # Create new start and accept state.
      start = frag2.start
      accept = frag1.accept
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
    elif c == '?':
      # Pop a single fragment off the stack.
      frag = nfa_stack.pop()
      # Create new start and accept States.
      accept = State()
      start = State(edges=[frag.start, accept])
      # Point arrows
      frag.accept.edges.append(accept)
    elif c == '*':
      # Pop a single fragment off the stack
      frag = nfa_stack.pop()
      # Create new start state (fragment start) and accept state (epsilon)
      accept = State()
      start = State(edges=[frag.start, accept])
      # Point arrows
      frag.accept.edges = [frag.start, accept]
    else:
      accept = State()
      start = State(label=c, edges=[accept])

    # Create new instance of Fragment to represent the new NFA.
    newFrag = Fragment(start, accept)
    # Push the new NFA to the NFA stack.
    nfa_stack.append(newFrag)

  # The NFA stack should have exactly one NFA on it, the answer.
  return nfa_stack.pop()

# Add a state to a set, and follow all of the e(Epsilon) arrows.
def followes(state, current):
  # Only do if when we haven't already seen the state.
  if state not in current:
    # Put the state itself into current
    current.add(state)
  # See whether state is labelled by e(psilon).
  if state.label is None:
    # Loop through the states pointed to by this state.
    for x in state.edges:
      # Follow all of their e(psilon)s too.
      followes(x, current)

# Will return true if regex is (Fully) equal to the String s, else false
def match(regex, lang):
  # Compile the regular expression into an NFA
  nfa = compile(regex)
    
  # Try to mathc the regular expression to the string s.
    
  # The current set of states.
  current = set()
  # Add the first state, and follow all e(psilon) arrows.
  followes(nfa.start, current)
  # The previous set of states.
  previous = set()

  # Loop through characters in s.
  for c in lang:
    # Kepp track of where we ere
    previous = current
    # Creates a new empty set for states we're about to be in.
    current = set()
    # Loop through the previous states.
    for state in previous:
      # Only follow arrows not labelled by e(Epsilon).
      # If Epsilon (E state) then label = None.
      if state.label is not None:
        # If the label of the state is equal to the character we've read.
        if state.label == c:
          # Add the state at the end of the arrow to the current
          followes(state.edges[0], current)

  # Ask the NFA if it matchs the String s
  return (nfa.accept in current)

# Test if the match function works!
print(match("a?", "aaaaa"))

