#Friendly helper AI
'''
Behaviours:
    Follows player character
    Helps player fight in combat
    Helps player by healing player
    Obeys player directions
    AI Pauses on pausing, then resumes.

'''
class StateMachine:
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
        
    def set_start(self, name): #Defining tthe start state
        self.startState = name.upper()
    #Behaviours
    def switch_behaviour():
        pass

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



