class ParentA:

    # Use __new__ when you need to control the creation of a new instance.
    #
    # Use __init__ when you need to control initialization of a new instance.
    #
    # __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
    #
    # In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been creat
    # https://stackoverflow.com/questions/674304/why-is-init-always-called-after-new
    def __new__(cls):
        print("NEW")
        # return super(ParentA, cls).__new__(cls)
        return super().__new__(cls)  # super() is simpler in Python 3

    def __init__(self):
        log("ParentA: init")


class ParentB:
    def __init__(self):
        log("ParentB: init")


class ParentC:
    # def __init__(self, a_field):
    #     log(f"ParentC: init {a_field}")
    def __init__(self):
        log(f"ParentC: init")


class ClassA(ParentA):
    def __init__(self):
        log("BaseA: pre super()")
        # super(ClassA, self).__init__()
        super().__init__()  # super() is simpler in Python 3
        log("BaseA: post super()")


class MixinAThenB(ParentA, ParentB):
    def __init__(self):
        log("Mixin: pre super()")
        # super(MixinAThenB, self).__init__()
        super().__init__()  # super() is simpler in Python 3


class MixinBThenA(ParentB, ParentA):
    def __init__(self):
        log("Mixin: pre super()")
        # super(MixinBThenA, self).__init__()
        # https://stackoverflow.com/questions/52140360/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type
        super().__init__()  # super() is simpler in Python 3


class ClassWithField(ParentC):
    def __init__(self, a_field="constructor_field"):
        super(ClassWithField, self).__init__()
        log(f"ClassWithField {a_field}")
        kwargs = self._input_kwargs
        self.setParams(**kwargs)

    def setParams(self, a_field="setParams field"):
        kwargs = self._input_kwargs
        return self._set(**kwargs)


def log(msg):
    print("\t{}".format(msg))


def print_order_of_resolution_for(c):
    print("\nThe Methord Resolution Order (MRO) of {}:".format(c.__name__))
    for i, clazz in enumerate(c.__mro__):
        print("{}: {}".format(i, clazz))


if __name__ == "__main__":
    print("Creating an object of the base class:")
    a = ClassA()
    # "Python will try to maintain the order in which each class appears on the inheritance list, starting with the child class itself.
    # ... if Python cannot find a coherent method resolution order, it'll raise an exception, instead of falling back to behavior which might surprise the user.
    # https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
    print("Creating an object of the base mix in (extending A then B):")
    mixed = MixinAThenB()
    print("Creating an object of the base mix in (extending B then A):")
    mixed = MixinBThenA()

    print_order_of_resolution_for(MixinBThenA)

    with_field = ClassWithField(a_field="a field")
    print(f"with_field.a_field = {with_field.a_field}")
