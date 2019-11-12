import smtplib, ssl #ssl is secure socket layer, designed to set up secure conection between client and server # smtp = Simple Mail Transfer Protocol
from Configuration import Configuration


class ConfirmationEmail:

    def __init__(self, details):

        self.user = ""
        self.email = self.getemail(details)
        self.port = 465

    def delete(self):
        smtp_server = "smtp.gmail.com"
        sender_email = Configuration.GamingEmailAddress  # Enter your address
        password = Configuration.GamingEmailPassword
        receiver = self.email
        message = """\
        Subject: Confirmation of user """ + self.user + """
        Hi """ + self.user + """ You have not been Granted access to Gaming Server for Further details email Configuration.GamingEmailAddress"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, self.port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, message)
            return True

    def add(self):
        smtp_server = "smtp.gmail.com"
        sender_email = "gamingserver.project@gmail.com"  # Enter your address
        password = "GamingServer2019"
        receiver = self.email
        message = """\
                Subject: Confirmation of user """ + self.user + """
                Hi """ + self.user + """ You have been Granted access to Gaming Server, Go to link below, login and Download our remote Gaming Software.\n
                Link -> http://""" + Configuration.ipAddress + """:""" + Configuration.portNumber + """/"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, self.port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, message)
            return True

    def getemail(self, details):
        data = details.split("-")
        user = data[0].split(":")
        self.setuser(user[1])
        email = data[1].split(":")
        return email[1]

    def setuser(self, user):
        self.user = user
