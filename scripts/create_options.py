from __future__ import print_function
import os.path


def create(port=True):
    basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

    options = [
        "-v {}/config/dot.theano:/root/.theano".format(basedir),
        "-v {}/notebooks:/jupyter".format(basedir),
        "-v {}/config/dot.jupyter:/root/.jupyter".format(basedir),
        "-v {}/config/jupyter:/root/.local/share/jupyter".format(basedir),
    ]
    if port:
        options.append("-p 4433:4433")

    key = os.path.exists(os.path.join(basedir, "config/keys/jupyter.key"))
    pem = os.path.exists(os.path.join(basedir, "config/keys/jupyter.pem"))

    if key and pem:
        options.append("-v {}/config/keys:/etc/cert".format(basedir))

    return " ".join(options).split(" ")


if __name__ == "__main__":
    print(" ".join(create(port=False)))
