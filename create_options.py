import os.path


basedir = os.path.dirname(os.path.abspath(__file__))

options = [
    "-p 4433:4433",
    "-v {}/notebooks:/jupyter".format(basedir),
    "-v {}/dot.jupyter:/root/.jupyter".format(basedir),
]

key = os.path.exists(os.path.join(basedir, "keys/jupyter.key"))
pem = os.path.exists(os.path.join(basedir, "keys/jupyter.pem"))

if key and pem:
    options.append("-v {}/keys:/etc/cert".format(basedir))

print(" ".join(options))

