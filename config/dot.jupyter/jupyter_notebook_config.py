import os
with open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "passwd")) as fp:
    p = fp.read().strip()

c.NotebookApp.certfile = '/etc/cert/jupyter.pem'
c.NotebookApp.keyfile = '/etc/cert/jupyter.key'
c.NotebookApp.ip = '*'
c.NotebookApp.password = p
c.NotebookApp.open_browser = False
c.NotebookApp.port = 4433
c.NotebookApp.notebook_dir = "/jupyter"
