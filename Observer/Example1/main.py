from abc import ABCMeta, abstractmethod

class Observer:
    pass

class Subject(object):
    def __init__(self) -> None:
        self.state = None
        self.observers = []
    
    def get_state(self) -> int:
        return self.state
    
    def set_state(self, state: int) -> None:
        self.state = state
        self.notifyAllObservers()

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notifyAllObservers(self) -> None:
        for observer in self.observers:
            observer.update()

class Observer(object, metaclass = ABCMeta):
    def __init__(self, subject: Subject) -> None:
        self.subject = subject
    
    @abstractmethod
    def update(self) -> None:
        pass

class BinaryObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        super().__init__(subject)
        self.subject.attach(self)
    
    def update(self) -> None:
        print("".join(["Binary String: ", str(self.subject.get_state())]))

class OctalObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        super().__init__(subject)
        self.subject.attach(self)
    
    def update(self) -> None:
        print("".join(["Octal String: ", str(self.subject.get_state())]))

class HexaObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        super().__init__(subject)
        self.subject.attach(self)
    
    def update(self) -> None:
        print("".join(["Hexa String: ", str(self.subject.get_state())]))


if __name__ == '__main__':
    subject = Subject()
    hexa = HexaObserver(subject)
    oct = OctalObserver(subject)
    bi = BinaryObserver(subject)
    subject.set_state(15)
    subject.set_state(10)
