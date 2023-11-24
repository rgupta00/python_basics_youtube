'''
    A           B
        C
'''
class A(object):
    def __init__(self, a):
        self.a=a
    def method1(self):
        print('method of class A: ',self.a)

class B(object):
    def __init__(self, b):
        self.b = b
    def method1(self):
        print('method of class B: ',self.b)


class C(B,A):
    def __init__(self,a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c=c

ob=C(2,3,4)
ob.method1()




