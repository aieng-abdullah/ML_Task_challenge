def warpper(func):
    def run_code():
        print("code is running")
        func()
        print("code is not running.....")

    return run_code
def func():
    print("hello")
new_func = warpper(func)
new_func()


