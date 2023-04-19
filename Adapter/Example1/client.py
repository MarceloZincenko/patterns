from whatiwant import WhatIWant

class ClientObject():
    def __init__(self, what_i_want: WhatIWant) -> None:
        self.what_i_want = what_i_want
    
    def do_something(self):
        self.what_i_want.required_function()