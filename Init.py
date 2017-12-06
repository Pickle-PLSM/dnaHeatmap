import csv
import subprocess

Acounter = 0
Gcounter = 0
Ccounter = 0
Tcounter = 0
command = 'Rscript'
path2script = 'dnaSeqHeatmap.R'

with open('SeqComparison.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow([''] + ['A'] + ['G'] + ['C'] + ['T'])
    spamwriter.writerow(['','A','G','C','T'])
''' @author Lyndsey Allison 
	inputing files into python'''
    #the while loop allows the user to input as many files as they want 
    while True:
    #tells python that it is opening a file
        def file(filename):

            with open(filename):
                raw_input('file: ')
        answer = raw_input("Insert a filename or insert quit once done adding files: ")
    '''there are two possibilities for the user to input a file or quit if the user inputs one thing 
    it will do one thing if they input something else it will do something else'''
        if answer != 'quit':
        #if the file inputted by the user (answer) is not quit it will open the file with the permission to read
            with open(answer, "r") as file:
		#the file need to be read into new lines to get rid the white spaces
	    	data = file.read().replace('\n', '') 
		#print the file content 
		print data
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
            #def build():
             ##  subprocess.check_output(cmd, universal_newlines=True)

            #build()
		break
