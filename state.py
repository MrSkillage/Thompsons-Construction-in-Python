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

class Frag:
    # Start state of NFA Fragment.
    start = None
    # Accept state of NFA Fragment.
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

# Create two new instances of class State
myInstance = State(label='a', edges=[])
myOtherInstance = State(edges=[myInstance])

# Create Frag instances
myFrag = Frag(myInstance, myOtherInstance)

# Print out the instance label and edges
print(myInstance.label)
print(myOtherInstance.edges[0])
print(myFrag)

