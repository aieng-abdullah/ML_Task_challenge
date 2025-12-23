import time
import os


def make_submissin():
    while True:
        if os.cpu_count:
            print(f"os asses donr",{os.cpu_count})
            break
        else:
            make_submissin()


make_submissin()