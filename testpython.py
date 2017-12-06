# Author: Sofie Christie

# run testpython.py
import subprocess

# Define command and arguments
command = 'Rscript'
path2script = 'dnaBarGraph.R'

def build():
    # Build subprocess command
    cmd = [command, path2script]

    # check_output will run the command and store to result
    subprocess.check_output(cmd, universal_newlines=True)

build()