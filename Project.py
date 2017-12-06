'''
@author Lyndsey Allison
    lines 10-
Introduction to Bioinformatics
Fall 2017
Final Project
Input files in python
'''
#use a while loop so that the user can input as many files as they want
while True:
    #tells python that it is opening a file
    def file(filename):

        with open(filename):
            raw_input('file: ')
    answer = raw_input("Insert a filename or insert quit once done adding files: ")
    #there are two possibilities for the user to input a file or quit if the user inputs one thing it will do one thing if they input something else it will do something else
    if answer != 'quit':
        #if the file inputted by the user (answer) is not quit it will open the file with the permission to read
        file = open(answer,"r")
        #print is used to check to see if the file was open in the with the permissions to read is not needed now
        #print file
    else:
        #if the user inputs quit then it will break out of the loop
        break
