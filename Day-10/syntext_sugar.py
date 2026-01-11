def decorator(func):
    def warpper():

        print("before")
        func()
        print("after")
        
    return warpper





@decorator
def say_hi():
    print("hi")

say_hi()