# Visualization of DNA Content
## How To: **Interpret DNA Sequences With Heatmaps and Graphs**
*By: Lyndsey, Patrick, Sofie, and Melody*

### Step 1: File Input

We obtained files of genes from different animals from the NCBI Database. We chose the FASTA file. A FASTA file is text file of nucleotides. Below are the names of the five different files we have chosen for the example that can be inputted into our code to be graphed and heatmaped. The five different sequences are genes from different animals. The sequences of nucleotides were copied and put into text files in the python project directory (Final Project). Text files are saved with the filename.txt and python files are defined by filename.py.

* Seq1: Dog
* Seq2: Cat
* Seq3: Zebra
* Seq4: Hippopotamus
* Seq5: Horse

The files were put in the same directory as the python file that inputs the files into the code (Init.py) so that the files can be called into the python file.



For file input a while loop is used so that the user can input as many files as they want and then stop once they were done adding files. First the variable file must be defined (filename) along with the command “with open” so that python knows it need to open a file. The command to get the input from the user is “raw_input” as seen above which is followed by a string that explains to the user what to do.  A variable in this case called “answer” is set equal to “raw_input” so that whatever the user inputs it will be saved as the variable answer so that it can be called to use later in the code. The string that the user is given stated to insert a filename or insert quit once done adding files. This is executed in the coding using an if else statement. If answers (what the user inputted) is not quit then the file answer will be open. When opening the file the permissions must be defined (whether they can read, write, or executed). For this project the file only needs the permission to read because we have no need to write anything in the file or execute it we are only taking the information from the file and interpreting it in a graph and heatmap. The file content is then saved as data and takes out any of the white space because white space would obstruct the analysis. Then the file content is then printed out to make sure there is no white space within the file.  If the user input was quit then the loop would break (exit from the loop) and ask for no more files to be inputted.

### Step 2: Analysis

From the file, an analysis of the base counts of each nucleotide was implemented. A string data type named “data” was used to hold the inputed DNA sequences. Then a character data type, named “base” was used to locate the individual DNA bases, adenine, cytosine, guanine and thymine, denoted as ‘A’, ‘C’, ‘G’, ‘T’ in the file being read in from the user. The python index function was used within a for loop to search within the length, denoted in python as len of the sequence variable data. “-1” was used for the range to avoid an out of bounds error. A double equal sign was used to compare the index of the base in the sequence inputed to the base variable. If a match was found the appropriate counter was increased by one. Separate A, G, C, and T counters denoted as Acounter, Tcounter, Ccounter, and Gcounter were used to get the frequency of each individual base within the file. Once all index positions had been iterated through, a print function was used to print the number of each base within the sequence. A concatenated string was used for increased readability.

```
data = "";

Acounter = 0
Tcounter = 0
Ccounter = 0
Gcounter = 0

for index in range ( (len(data)) - 1):

   if data[index] == 'A':
       Acounter +=1
   if data[index] == 'T':
       Tcounter +=1
   if data[index] == 'C':
       Ccounter +=1
   if data[index] == 'G':
       Gcounter += 1

print ("T count is " + str(Tcounter))
print ("A count is " + str(Acounter))
print ("C count is " + str(Ccounter))
print ("G count is " + str(Gcounter))
```

### Step 3: Piping data to R
For the heatmap, the group decided to go with an intermediate step for importing data to R, namely creating a csv file from analyzed data in Python. The csv python module was imported and the output file, named SeqComparison.csv, was initialized with the first row already containing only labels A, G, C, and T. Later, within the while loop, each read in file’s counters for bases were written to the next respective line of the csv file.


To call R,  we imported a library call subprocess. This library calls commands inside of python.
import subprocess

We then define the command line arguments.
command = 'Rscript'

`path2script = 'dnaSeqHeatmap.R'`

Then build the subprocess command with those variables.
`cmd = [command, path2script]`

To run R, used the check_output function and store the result.

`subprocess.check_output(cmd, universal_newlines=True)`

### Step 4: Graphing

#### Bar Graph:

After python has created the CSV file,
This step is done in R. To draw the bar graph, we use the ggplots and reshape2 library. ggplots allows for cleaner graphing capabilities and reshapes formats the csv data so it fits into the function. To actually output the graph, you need to create an image file within R that plots whatever is below. Then you format the data with the ‘melt’ funtion and get the ID, which is column 1 in the csv. The ggplot function takes in two parameters, the data, and the aes function, which takes in the parameters for the bargraph. Then you can add the graph and labels to the function (literally).

```
# Author: Sofie Christie
# Description: Create a stacked bar graph based off a csv created in python

# print graph to png
png(file="bargraph.png")

# read in the csv
df <- read.csv("SeqComparison.csv", header = TRUE)

# import the ggplot2 library for better graphing capabilities
library(ggplot2)
# import the reshape2 library to better format the data
library(reshape2)

df <- melt(df, id = 'File')
ggplot(
   data = df,
   aes(
      # input parameters
      y = value,
      x = File,
      group = variable,
      shape = variable,
      fill = variable
   )
) +
# add graph and labels
geom_bar(stat = "identity") + labs(y="Count", fill="Base", title="ATGC Content Relative to Different Sequences")
```

#### Heatmap:

With an outputted SeqComparison.csv from the Init.py file, the file was read into R with the read.csv method and saved as an unformatted variable, seqs. Data in the csv file was “cleaned up” by setting the first row in the file (containing only A, G, C, and T) to be the row name labels in the final heatmap. With only file names and numerical data, the resulting data was formatted into a matrix. Finally, the heatmap function was called on the data matrix and formatted, then output as a png file.

```
Integrating code:
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
```

File input, analysis, and csv output modules as well as R integration for graphs was concatenated into one functioning module (Init.py). Init.py does every function of the project. With the current implementation, the csv file would not be completed until Init.py finished running. However, it was determined that raw formatted data in the form of a csv was valuable to the user and therefore running dnaSeqHeatmap. R separately was acceptable. The R files for the bar graph and heatmap are separate, so we allow the user to decide if they want a bargraph or heatmap through user input, and that changes the ‘command’ variable to build to the subprocess command.
