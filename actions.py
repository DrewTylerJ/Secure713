import sys
vals = {}
class FirstClass:
    def access(self):
        while True:
            accpass = input("Please enter the access code: ")
            if accpass == "admin":
                print("\nAccess Granted\n\n")
                break
            print("Incorrect password")
        dictionary = Initializer.dict(self)
        FirstClass.option(self, dictionary)

    def option(self, dictionary):
        while True:
            print("""1-Access passwords
2-Add password
3-Delete password
7-Save Data
9-Read Text File
11-Enhaned Delete [WIP]
0-Access Print Debugger\n""")
            inp = int(input("What would you like to do?: "))

            while inp not in [0, 1, 2, 3, 7, 9, 11]:
                print("invalid response\n")
                print("""1-Access passwords
2-Add password
3-Delete password
7-Save Data
9-Read Text File
11-Enhanced Delete [WIP]
0-Access Print Debugger\n""")
                inp = int(input("What would you like to do?: "))
            if inp == 1:
                Functions.view(self, dictionary)
            elif inp == 2:
                Functions.addpair(self, dictionary)
            elif inp == 3:
                Functions.deleteinfo(self, dictionary)
            elif inp == 7:
                Functions.saveinfo(self, dictionary)
            elif inp == 0:
                Functions.debug(self, dictionary)
            elif inp == 9:
                Functions.readfile(self)
            elif inp == 11:
                Functions.enhanceddelete(self, dictionary)
            else:
                Initializer.dict(self)


class Functions:


    def view(self, dictionary):
        print(dictionary)
        print(dictionary.keys())
        ReRun.cont(self, dictionary)

    def addpair(self, dictionary):
        print("Enter the name of the site you would like to add an account for: ")
        inSite = input(">")
        print("Enter the username: ")
        inUser = input(">")
        print("Enter the password: ")
        inPW = input(">")
        vals.update({inUser: inPW})
        print(dictionary)
        print(vals)
        dictionary[inSite] = vals
        print(dictionary)
        ReRun.cont(self, dictionary)


    def deleteinfo(self, dictionary):
        print("Enter the name of the site you would like to delete an account for: ")
        inSite2 = input(">")
        print("Enter the username: ")
        inUser2 = input(">")
        print("Enter the password: ")
        inPW2 = input(">")
        dcvals = list(dictionary[inSite2].values())
        for j in dcvals:
            dictionary[inSite2].pop(j)
        dictionary.pop(inSite2, None)
        ReRun.cont(self, dictionary)

    def saveinfo(self, dictionary):
        filewrite = open("password.txt", "w")
        keytest = list(dictionary.keys())
        for key, value in dictionary.items():
            newstring = ""
            for key2, value2 in dictionary[key].items():
                newstring += ":" + key2 + ":" + value2
            newstring = key + newstring
            filewrite.write(newstring + "\n")
        filewrite.close()

    def debug(self, dictionary):
        print(dictionary)
        print(dictionary.keys())
        keytest = list(dictionary.keys())
        for key, value in dictionary.items():
            newstring = ""
            for key2, value2 in dictionary[key].items():
                newstring += ":" + key2 + ":" + value2
            print(key + newstring)
            keytest2 = list(dictionary.keys())
        print(keytest[0])
        ReRun.cont(self, dictionary)

    def readfile(self):
        file4read = open("password.txt", "r")
        print(file4read.read())
        file4read.close()

    def enhanceddelete(self, dictionary):
        print("Enter the name of the site you would like to delete an account for: ")
        inSite2 = input(">")
        print("Enter the username: ")
        inUser2 = input(">")
        print("Enter the password: ")
        inPW2 = input(">")
        dcvals = list(dictionary[inSite2].values())
        for j in dcvals:
            dictionary[inSite2].pop(j)
        dictionary.pop(inSite2, None)
        ReRun.cont(self, dictionary)



class ReRun:
    def cont(self, dictionary):
        while True:
            ans = input("\nWould you like to continue? [y/n] > ")
            if ans == "n":
                sys.exit()
            elif ans == "y":
                print("\n")
                break
            else:
                print("Error try again:")
                continue
        FirstClass.option(self, dictionary)

class Initializer:
    def dict(self):
        # Open File containing websites, usernames, and passwords
        with open('password.txt', 'r') as f:
            sites = {}
            # Iterate each line of the file
            for line in f:
                # Split line into a list
                splitLine = line.split(":")
                splitLine[len(splitLine)-1] = splitLine[len(splitLine)-1].rstrip('\n')
                # Dictionary of usernames and passwords
                vals = {}
                # Add each set of usernames and passwords to vals
                for g in range(1,len(splitLine),2):
                    vals[splitLine[g]] = splitLine[g+1];
                # Add vals to main dictionary
                sites[splitLine[0]] = vals
        return sites
