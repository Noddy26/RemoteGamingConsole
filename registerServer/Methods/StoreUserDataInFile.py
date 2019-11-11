from Configuration import Configuration
from Methods.SendEmail import SendEmail


class StoreDataInFile:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def run(self):
        SQLcommand = "INSERT INTO userdetails(userID, username, password, email, ipAddress) VALUES (NULL, '%s', '%s', '%s', NULL);" % (self.username, self.password, self.email)
        filename = Configuration.adduserdir + self.username + ".txt"
        with open(filename, 'w') as f:
            f.write(SQLcommand)
        with open(Configuration.userfilepath, 'a') as f:
            f.write("\nUser:" + self.username)
            f.write("-Email:" + self.email)
        if SendEmail(self.email, self.username).run() is True:
            return True
        return False
