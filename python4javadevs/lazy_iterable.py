import sys
import re


class MyIter:
    def __init__(self):
        self.i = 1

    def increment_i(self):
        self.i += 1
        print(f"Have increased i to {self.i}")
        return self.i

    def get_generator(self):
        return (self.increment_i() for _ in range(10)) # note: square brackets would make this eager


def load_file_as_generator(file):
    print(f"Reading {file}")
    f = open(file)
    return (line for line in f.readlines())


if __name__ == "__main__":
    print("start")
    my_gen = load_file_as_generator(sys.argv[0])
    x = next(my_gen, None)
    print("before while")
    while x is not None:
        x = re.sub("\n", "", x)
        print(x)
        x = next(my_gen, None)
    print("finished")

    my_iter = MyIter()
    xs = my_iter.get_generator()
    for _ in range(5):
        print(f"Calling next...")
        next(xs)
