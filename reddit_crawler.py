import requests
import json
import sys
usage = "Usage:\n\n-f  Pass a file containing first the persons of interest on each line and then keywords of interest on each line, with the groups of words separated by a new line\n\n-p  Follow this option with the names of persons of interest separated by spaces\n\n-k  Follow this option with the keywords of interest separated by spaces"

persons = []
options = []
keywords = []

if sys.argv.__len__() < 2:
    print(usage)
    exit()

mode = sys.argv[1]
if mode == "-f": #using file for persons and names
    if sys.argv.__len__() < 3:
        print("you must pass a file to use for persons/keywords when using the -f option")
    else:
        f = open(sys.argv[2])
        if f == None:
            print("error opening file: '" + sys.argv[1]+"'")
        else:
            readPersons = False
            for line in f:
                if line == "\n":
                    readPersons = True
                    continue
                elif not readPersons:
                    persons.append(line)
                else:
                    keywords.append(line)
elif mode == '-p' or mode == '-k': #we will read in persons and keywords from cmd line args
    for i in range(2, sys.argv.__len__()):
        if sys.argv[i] == '-p':
            mode = "-p"
            continue
        elif sys.argv[i] == '-k':
            mode = '-k'
            continue
        if mode == "-p":
            persons.append(sys.argv[i])
        else:
            keywords.append(sys.argv[i])
    if persons.__len__() == 0 or keywords.__len__() == 0:
        print("you must pass both persons and keywords following the -p and -k options respectively")
else:
    print(usage)
print("persons:")
print(persons)
print("\nkeywords")
print(keywords)

