import sys
usage = "Usage:\n\n-f  Pass a file containing first the persons of interest on each line and then keywords of interest on each line, with the groups of words separated by a new line\n\n-p  Follow this option with the names of persons of interest separated by spaces\n\n-k  Follow this option with the keywords of interest separated by spaces"

class Input:
    def resolveInput(self, args):
        pset = {}
        kset = {}
        persons = []
        keywords = []
        if args.__len__() < 2:
            print(usage)
            exit()

        mode = args[1]
        if mode == "-f":  # using file for persons and names
            if args.__len__() < 3:
                print("you must pass a file to use for persons/keywords when using the -f option")
            else:
                f = open(args[2])
                if f == None:
                    print("error opening file: '" + args[1] + "'")
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
        elif mode == '-p' or mode == '-k':  # we will read in persons and keywords from cmd line args
            for i in range(2, args.__len__()):
                if args[i] == '-p':
                    mode = "-p"
                    continue
                elif args[i] == '-k':
                    mode = '-k'
                    continue
                word = args[i].rstrip().lower()
                if mode == "-p":
                    persons.append(word)
                else:
                    keywords.append(word)
            if persons.__len__() == 0 or keywords.__len__() == 0:
                print("you must pass both persons and keywords following the -p and -k options respectively")
        else:
            print(usage)

        return persons, keywords