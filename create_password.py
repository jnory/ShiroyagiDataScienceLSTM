from __future__ import print_function
import os
from IPython.lib import passwd

basedir = os.path.dirname(__file__)
path = os.path.join(basedir, "dot.jupyter/passwd")
with open(path, "w") as fp:
    h = passwd()
    print(h, file=fp)
