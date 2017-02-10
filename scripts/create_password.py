from __future__ import print_function
import os
from IPython.lib import passwd

basedir = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)), "..")
path = os.path.join(basedir, "config/dot.jupyter/passwd")
with open(path, "w") as fp:
    h = passwd()
    print(h, file=fp)
