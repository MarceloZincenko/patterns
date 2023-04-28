from context import Context
from start_state import StartState
from stop_state import StopState

context = Context()

startState = StartState()
startState.do_action(context)
print(context.get_state().to_string())

stopState = StopState()
stopState.do_action(context)
print(context.get_state().to_string())