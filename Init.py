import csv
import subprocess

# Define command and arguments
command = 'Rscript'
path2script = 'dnaSeqHeatmap.R'

Acounter = 0
Gcounter = 0
Ccounter = 0
Tcounter = 0

# tells whether or not to run the subprocess
graph = False;

with open('SeqComparison.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["File","A","G","C","T"])

    rfile = raw_input("Do you want a heatmap or a bargraph? ")

    if(rfile == "heatmap"):
        path2script = "dnaSeqHeatmap.R"

    if(rfile == "bargraph"):
        path2script = "dnaBarGraph.R"

    while True:
    #tells python that it is opening a file
        def file(filename):

            with open(filename):
                raw_input('file: ')

        answer = raw_input("Insert a filename or insert quit once done adding files: ")
        #there are two possibilities for the user to input a file or quit if the user inputs one thing it will do one thing if they input something else it will do something else
        if answer != 'quit':
        #if the file inputted by the user (answer) is not quit it will open the file with the permission to read
            with open(answer, "r") as file:
               data = file.read().replace("\n", "")
               print(data)
        #print is used to check to see if the file was open in the with the permissions to read is not needed now
        #print file
            for index in range ( (len(data)) - 1):
                if data[index] == 'A':
                    Acounter += 1
                if data[index] == 'G':
                    Gcounter += 1
                if data[index] == 'C':
                    Ccounter += 1
                if data[index] == 'T':
                    Tcounter += 1
            spamwriter.writerow([answer,str(Acounter),str(Tcounter),str(Ccounter),str(Gcounter)])
        else:
            # after finished creating csv, graph equals true
            graph = True
            break

# call the R script to make the graph
if graph is True:
    # Build subprocess command
    cmd = [command, path2script]

    # check_output will run the command and store to result
    subprocess.check_output(cmd, universal_newlines=True)
