from abc import ABC, abstractmethod


class MyAbClass(ABC):
    def execute(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass


class MyAbClassV1(MyAbClass):
    def step1(self):
        return 'step 1'
    def step2(self):
        return 'step 2'
    def step3(self):
        return 'step 3'

ob=MyAbClassV1()
print(ob.step1())