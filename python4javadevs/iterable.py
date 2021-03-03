class MyIterable(tuple):

    index = 0

    def __init__(self, xs):
        print("MyIterable")
        self.xs = xs

    def __next__(self):
        x = self.xs[self.index]
        self.index = 1 + self.index
        return x


if __name__ == "__main__":
    xs = MyIterable([1,2,3,4])
    for x in xs:
        print(x)
    print("fin")
