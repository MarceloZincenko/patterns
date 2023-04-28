from state import State

class Context(object):

    def __init__(self) -> None:
        self.state = None

    def set_state(self, state: State) -> None:
        self.state = state
    
    def get_state(self) -> State:
        return self.state