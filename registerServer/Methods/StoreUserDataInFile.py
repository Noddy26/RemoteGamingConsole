import base64
import os

from Configuration import Configuration
from Methods.SendEmail import SendEmail


class StoreDataInFile:

    def __init__(self, username, password, email):
        self.username = username
        self.passw = password
        self.password = str(self.encryptpassword()).replace("'", "_")
        print(self.password)
        self.email = email

    def run(self):
        SQLcommand = "INSERT INTO %s(UserID, username, password, Email, ipAddress, login) VALUES (NULL, '%s', '%s', '%s', '', 'False');" \
                     % (Configuration.sqlusertable, self.username, self.password, self.email)
        filename = Configuration.adduserdir + self.username + ".txt"
        with open(filename, 'w') as f:
            f.write(SQLcommand)
        with open(Configuration.userfilepath, 'a') as f:
            f.write("\rUser:" + self.username)
            f.write("-Email:" + self.email)
        os.system('sudo sed -e "s/\\r//g" -i ' + Configuration.userfilepath)
        os.system("sudo sed -i '/^$/d' " + Configuration.userfilepath)
        if SendEmail(self.email, self.username).run() is True:
            return True
        return False

    def encryptpassword(self):
        return base64.b64encode(self.passw.encode("utf-8"))
