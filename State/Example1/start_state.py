from state import State

class StartState(State):

    def do_action(self, context) -> None:
        print("Player in start state")
        context.set_state(self)
        
    def to_string(self) -> str:
        return "Start state"