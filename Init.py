#Authors: Patrick Rynkiewicz, Sofie Christie, Melody Kabbai, and Lyndsey Allison
import csv
import subprocess

# Define command and arguments
command = 'Rscript' # type of script for subprocess to run
path2script = ''  # will become path to script user selects

#counters for possible nucleotide bases
Acounter = 0
Gcounter = 0
Ccounter = 0
Tcounter = 0

# tells whether or not to run the subprocess
graph = False

with open('SeqComparison.csv', 'wb') as csvfile:    #following will be written to a csv
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["File","A","G","C","T"])     #the header (first row) will denote bases

    rfile = raw_input("Do you want a heatmap or a bargraph? ") #user choice of formatted output

    if(rfile == "heatmap"):
        path2script = "dnaSeqHeatmap.R"

    if(rfile == "bargraph"):
        path2script = "dnaBarGraph.R"

    while True:
    #tells python that it is opening a file
        def file(filename):

            with open(filename):
                raw_input('file: ')

        answer = raw_input("Insert a filename or insert quit once done adding files: ") #process text file name input or exit while loop if user selects quit
        if answer != 'quit':
        #if the file inputted by the user (answer) is not quit it will open the file with the permission to read
            with open(answer, "r") as file:
               data = file.read().replace("\n", "")    #get rid of those pesky newline characters and save input as a string
               print(data)
        #print is used to check to see if the file was open in the with the permissions to read is not needed now
        #print file
            for index in range ( (len(data)) - 1):   #data analysis, nucleotide counters will increase based on string content
                if data[index] == 'A':
                    Acounter += 1
                if data[index] == 'G':
                    Gcounter += 1
                if data[index] == 'C':
                    Ccounter += 1
                if data[index] == 'T':
                    Tcounter += 1
            spamwriter.writerow([answer,str(Acounter),str(Tcounter),str(Ccounter),str(Gcounter)])   #write new row to csv when text file of question is processed
        else:
            # after finished creating csv, graph equals true
            graph = True
            break

# call the R script to make the graph/heatmap
if graph is True:
    # Build subprocess command
    cmd = [command, path2script]

    # check_output will run the command and store to result
    subprocess.check_output(cmd, universal_newlines=True)

#blessed
