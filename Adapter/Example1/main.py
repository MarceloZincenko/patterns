from third_party import WhatIHave
from adapter import Adapter
from client import ClientObject

if __name__ == "__main__":
    adaptee = WhatIHave()
    adapter = Adapter(adaptee)
    client = ClientObject(adapter)
    client.do_something()