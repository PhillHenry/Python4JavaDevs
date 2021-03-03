class ParentA:
    def __init__(self):
        log("ParentA: init")


class ParentB:
    def __init__(self):
        log("ParentB: init")


class BaseA(ParentA):
    def __init__(self):
        log("BaseA: pre super()")
        super(BaseA, self).__init__()
        log("BaseA: post super()")


class Mixin(ParentA, ParentB):
    def __init__(self):
        log("Mixin: pre super()")
        super(Mixin, self).__init__()


def log(msg):
    print("\t{}".format(msg))


if __name__ == "__main__":
    print("Creating an object of the base class:")
    a = BaseA()
    print("Creating an object of the base mix in:")
    mixed = Mixin()
