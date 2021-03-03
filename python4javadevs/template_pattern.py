import abc
from abc import ABC


class Parent(ABC):
    # __metaclass__ = abc.ABCMeta // this appears only to be  necessary Python <= 3.4

    def __init__(self):
        print("__init__: Parent")

    def do_template(self):
        print("template method leads to {}".format(self.template_method()))

    @abc.abstractmethod
    def template_method(self):
        """This should not be subclassed if not over riden if ABC is doing its work"""
        return


class ClassA(Parent):

    def __init__(self):
        super(ClassA, self).__init__()

    def template_method(self):
        return "ClassA.template_method"


class ClassB(Parent):

    def __init__(self):
        super(ClassB, self).__init__()

    def template_method(self):
        return "ClassB.template_method"


class DoesNotInstantiateThanksToABC(Parent):

    def __init__(self):
        print("DoesNotInstantiateThanksToABC: __init__")
        super(DoesNotInstantiateThanksToABC, self).__init__()


if __name__ == "__main__":
    a = ClassA()
    a.do_template()

    b = ClassB()
    b.do_template()

    parent = Parent()  # blows up in Python 3.6.9
    parent.do_template()
    parent.template_method()

    fails = DoesNotInstantiateThanksToABC()
