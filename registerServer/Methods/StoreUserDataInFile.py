from registerServer.Methods.SendEmail import SendEmail


class StoreDataInFile:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def run(self):
        SQLcommand = "INSERT INTO userdetails(userID, username, password, email, ipAddress) VALUES (NULL, '%s', '%s', '%s', NULL);" % (self.username, self.password, self.email)
        filename = "UserToBeAdded//" + self.username + ".txt"
        with open(filename, 'w') as f:
            f.write(SQLcommand)
        if SendEmail.run(self.email) is True:
            return True
        return False
