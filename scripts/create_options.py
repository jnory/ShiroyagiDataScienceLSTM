import os.path

def create():
    basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

    options = [
        "-p 4433:4433",
        "-v {}/notebooks:/jupyter".format(basedir),
        "-v {}/config/dot.jupyter:/root/.jupyter".format(basedir),
        "-v {}/config/jupyter:/root/.local/share/jupyter".format(basedir),
    ]

    key = os.path.exists(os.path.join(basedir, "config/keys/jupyter.key"))
    pem = os.path.exists(os.path.join(basedir, "config/keys/jupyter.pem"))

    if key and pem:
        options.append("-v {}/config/keys:/etc/cert".format(basedir))

    return " ".join(options).split(" ")

