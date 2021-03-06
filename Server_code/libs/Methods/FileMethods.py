import fileinput
import os
import re
from libs.variables.Configuration import Configuration


class FileMethods:

    @staticmethod
    def readfile(filename):
        with open(filename, 'r') as f:
            data = f.read()
            f.close()
        return data

    @staticmethod
    def replaceHTML(fileName, data, replacementText):
        os.system("sudo chmod 327 " + fileName)
        count = 0
        newdata = data.split("\n")
        textToReplace = '<h1><button class="Add1">Add User</button> hello</h1>'
        os.system("cp " + fileName + " " + fileName + ".bck")
        for each in newdata:
            if each:
                count = count + 1
                string = '<h1><input type="submit" name="action" value="add%s"><input type="submit" name="action" value="delete%s"> %s</h1><br>\n' % (count, count, each)
                replacementText += string
            else:
                Configuration.CheckforemptyString = True

        if Configuration.CheckforemptyString is True:
            Configuration.CheckforemptyString = False
            string = "<p><strong>Their are currently no users to be added.</strong></p>"
            replacementText += string
        count = 0
        for line in fileinput.FileInput(fileName, inplace=1):
            line = line.replace(textToReplace, replacementText)
            print(line)

    @staticmethod
    def returnHTMLpageBack(admin, adminbackup):
        try:
            if os.path.exists(adminbackup):
                if os.path.exists(admin):
                    os.system("sudo rm -rf " + admin)
                print("sudo mv %s %s" % (adminbackup, admin))
                os.system("sudo mv %s %s" % (adminbackup, admin))

                print("both files changed")
        except:
            print("files not changed")

    @staticmethod
    def removefile(fileName):
        userdetails = ""
        os.system("sudo rm -rf %s%s" % (Configuration.adduserdir, fileName + ".txt"))
        with open(Configuration.userfilepath) as f:
            for line in f:
                if line.__contains__(fileName):
                    userdetails = line
        for line in fileinput.FileInput(Configuration.userfilepath, inplace=1):
            line = line.replace(userdetails, "")
            print(line)
        print("sudo sed -i '/^$/d' " + Configuration.userfilepath)
        os.system("sudo sed -i '/^$/d' " + Configuration.userfilepath)

    @staticmethod
    def addUserDataToHtml(data):
        endlist = []
        fileName = Configuration.userhtml
        textToReplace = '<td>Peter</td>'
        os.system("sudo cp " + fileName + " " + fileName + ".bck")
        UserCount = 0
        count = 0
        for each in data:
            UserCount = UserCount + 1
            endlist.append("<tr>")
            change = str(each).replace("(", "").replace(")", "").replace("'", "")
            listuser = change.split(",")
            for item in listuser:
                count = count + 1
                if count == 6:
                    count = 0
                if count == 1:
                    endlist.append('<td><input type="checkbox" name="check" value="user' + item +'">%s<br></td>' % item)
                if item.replace(" ", "") == "True":
                    endlist.append('<td><span class="dotgreen"></span></td>')
                if item.replace(" ", "") == "False":
                    endlist.append('<td><span class="dotred"></span></td>')
                if item.replace(" ", "") != "False" and count is not 1:
                    if item.replace(" ", "") != "True":
                        endlist.append("<td>%s</td>" % item)
            endlist.append("</tr>")
        toString = str(endlist).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        print(toString)
        replacementText = toString
        for line in fileinput.FileInput(fileName, inplace=1):
            line = line.replace(textToReplace, replacementText)
            print(line)

