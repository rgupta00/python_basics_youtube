'''
u can use ab calss to mention that u want similer to interface
'''
from abc import ABC, abstractmethod


class GamingConsole(ABC):
    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass


class SimpleGamingConsole(GamingConsole):
    def up(self):
        return 'move up using simple gaming console'

    def down(self):
        return 'move down using simple gaming console'

    def left(self):
        return 'move left using simple gaming console'

    def right(self):
        return 'move right using simple gaming console'

ob=SimpleGamingConsole()
print(ob.down())