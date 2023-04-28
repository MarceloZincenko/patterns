from state import State

class StopState(State):

    def do_action(self, context) -> None:
        print("Player in stop state")
        context.set_state(self)
        
    def to_string(self) -> str:
        return "Stop state"