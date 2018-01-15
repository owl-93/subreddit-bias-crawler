import requests
import json
import sys
usage = "Usage:\n\n-f  Pass a file containing first the persons of interest on each line and then keywords of interest on each line, with the groups of words separated by a new line\n\n-p  Follow this option with the names of persons of interest separated by spaces\n\n-k  Follow this option with the keywords of interest separated by spaces"

persons = []
pset = {}
options = []
keywords = []
kset = {}
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
                word = line.rstrip().lower()
                if line == "\n":
                    readPersons = True
                    continue
                elif not readPersons and not (word in pset.keys()):
                    persons.append(line.rstrip().lower())
                    pset[word] = True
                elif readPersons and not (word in kset.keys()):
                    keywords.append(line.rstrip().lower())
                    kset[word] = True
                else:
                    continue
elif mode == '-p' or mode == '-k': #we will read in persons and keywords from cmd line args
    for i in range(2, sys.argv.__len__()):
        if sys.argv[i] == '-p':
            mode = "-p"
            continue
        elif sys.argv[i] == '-k':
            mode = '-k'
            continue
        word = sys.argv[i].rstrip().lower()
        if mode == "-p":
            persons.append(word)
        else:
            keywords.append(word)
    if persons.__len__() == 0 or keywords.__len__() == 0:
        print("you must pass both persons and keywords following the -p and -k options respectively")
else:
    print(usage)


print("persons:")
print(persons)
print("\nkeywords")
print(keywords)

print(persons[0] == "trump")


