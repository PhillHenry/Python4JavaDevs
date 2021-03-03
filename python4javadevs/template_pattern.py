import abc


class Parent:

    def __init__(self):
        print("__init__: Parent")

    def do_template(self):
        print("template method leads to {}".format(self.template_method()))

    @abc.abstractmethod
    def template_method(self):
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


if __name__ == "__main__":
    a = ClassA()
    a.do_template()

    b = ClassB()
    b.do_template()

    parent = Parent()
    parent.do_template()
