import fileinput
import os, sys

class FileMethods:

    @staticmethod
    def readfile(filename):
        with open(filename, 'r') as f:
            data = f.read()
            f.close()
        return data

    @staticmethod
    def replaceHTML(file, data, replacementText):
        count = 0
        newdata = data.split("\n")
        textToReplace = '<h1><button class="Add1">Add User</button> hello</h1>'
        os.system("sudo cp " + file + " " + file + ".bck")
        for each in newdata:
            count = count + 1
            string = '<h1><button class ="Add%s" > Add User </button><button class ="Delete1%s">Delete User </button> %s</h1><br>\n' % (count, count, each)
            replacementText += string
        count = 0
        with fileinput.FileInput(file) as file:
            for line in file:
                print(line.replace(textToReplace, replacementText), end='')

    @staticmethod
    def returnHTMLpageBack(admin, adminbackup):
        try:
            if os.path.exists(adminbackup):
                print(admin)
                print(adminbackup)
                if os.path.exists(admin):
                    os.remove(admin)
                print("sudo mv %s %s" % (adminbackup, admin))
                os.system("sudo mv %s %s" % (adminbackup, admin))

                print("both files changed")
        except:
            print("files not changed")
