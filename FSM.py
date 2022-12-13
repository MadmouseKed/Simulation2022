#Friendly helper AI
'''
Behaviours:
    Ai routine begins by spawning in the ai
    Follows player character if no other behaviour currently ongoing
    If dead, ai routine should end.
'''
class InitializationError(Exception):
    "Exception raised for incorrect initialization of the statemachine."
    pass

class FiniteStateMachine:
    #Basic machine parts
    def __init__(self):#Informing the statemachine of which parts it consists
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0): #The ability to add new states, and to tell the FSM whether the state added is an end state or not.
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)
        
    def set_start(self, name): #Defining the start state
        self.startState = name.upper()

    #Run part
    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("Must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("Expected to have at least one end_state before running")

        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                print("Reached: ", newState)
                break
            else:
                handler = self.handlers[newState.upper()]

class AiBehaviour(FiniteStateMachine):
    def __init__(self):
        self.currentState = None

    def getCurrentState(self):
        return self.currentState

    #Behaviours
    def start_AI(cmand):
        pass



    def switch_behaviour():
        pass


    def die():
        return ("Died", "")


def t_start(lst):
    head, tail = lst[0], lst[1:]
    if head == "Advance":
        newState = "transition_state"
    else:
        newState = "error_state"
    return (newState, tail)

def transition_state(lst):
    head, tail = lst[0], lst[1:]
    newState = "error_state"
    if head == "Advance":
        newState == "transition_state"
    elif head == "Succeed":
        newState = "success_state"
    elif head == "Fail":
        newState == "failure_state"
    else:
        newState == "error_state"
    return (newState, tail)

###
t = FiniteStateMachine()
t.add_state("start", t_start)
t.add_state("transition_state", transition_state)
t.add_state("success_state", None, end_state=1)
t.add_state("failure_state", None, end_state=1)
t.add_state("error_state", None, end_state=1)
t.set_start("start")

print("Succeed test")
t.run(['Advance','Succeed'])
print("Failure test")
t.run(['Advance','Fail'])
print("Error test")
t.run(['Advance','Cabbage'])