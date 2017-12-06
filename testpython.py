# run testpython.py
import subprocess

# Define command and arguments
command = 'Rscript'
path2script = 'dnaBarGraph.R'

def build(args):
    # Build subprocess command
    cmd = [command, path2script] + args

    # check_output will run the command and store to result
    subprocess.check_output(cmd, universal_newlines=True)

# Variable number of args in a list
seqcount1 = [['2', '7', '9', '1'],['1', '15', '5', '10'],['6', '2', '9', '13']]

build(seqcount1[0])