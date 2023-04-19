from third_party import WhatIHave
from whatiwant import WhatIWant

class Adapter(WhatIHave, WhatIWant):
    def __init__(self, what_i_have: WhatIHave) -> None:
        self.what_i_have = what_i_have

    def provided_function_1(self):
        self.what_i_have.provided_function_1
    
    def provided_function_2(self):
        self.what_i_have.provided_function_2
    
    def required_function(self):
        self.provided_function_1()
        self.provided_function_2()