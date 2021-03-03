class ParentA:
    def __init__(self):
        log("ParentA: init")


class ParentB:
    def __init__(self):
        log("ParentB: init")


class ClassA(ParentA):
    def __init__(self):
        log("BaseA: pre super()")
        super(ClassA, self).__init__()
        log("BaseA: post super()")


class MixinAThenB(ParentA, ParentB):
    def __init__(self):
        log("Mixin: pre super()")
        super(MixinAThenB, self).__init__()


class MixinBThenA(ParentB, ParentA):
    def __init__(self):
        log("Mixin: pre super()")
        super(MixinBThenA, self).__init__()


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
