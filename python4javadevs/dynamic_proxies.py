import types

class MyClass():
    def __init__(self):
        print("MyClass constructor")

    def fn_to_proxy(self):
        print("QED")


def proxy_fn(model):
    print("Proxy calling underlying function")
    model.fn_to_proxy()


def create_and_invoke_proxy():
    model = MyClass()
    model.proxied = types.MethodType(proxy_fn, model)
    model.proxied()


if __name__ == "__main__":
    create_and_invoke_proxy()