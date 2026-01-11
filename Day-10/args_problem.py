def decorator(func):
    def warpper(*args):
        print("Args", args)
        return func(*args)
    return warpper


@decorator
def add(a,b):
    return a+b
print(add(10,11))

