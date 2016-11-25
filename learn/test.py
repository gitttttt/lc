import sys, pickle
class test:
    def __enter__(self):
        print("enter")
    def __exit__(self,*args):
        print("exit")
        return False

with open() as f:
    10/0
pickle.dump()