import smtplib, ssl
#ssl is secure socket layer, designed to set up secure conection between client and server
# smtp = Simple Mail Transfer Protocol
from Configuration import Configuration


class ConfirmationEmail:

    def __init__(self, details):

        self.user = ""
        self.email = self._getemail(details)
        self.port = 465

    def delete(self):
        smtp_server = "smtp.gmail.com"
        sender_email = Configuration.GamingEmailAddress  # Enter your address
        password = Configuration.GamingEmailPassword
        receiver = self.email
        message = """\
        Subject: Confirmation of user """ + self.user + """
        Hi """ + self.user + """\r\nYou have not been Granted access to Gaming Server for Further details email %s""" \
                  % Configuration.GamingEmailAddress

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, self.port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, message)
            return True

    def add(self):
        smtp_server = "smtp.gmail.com"
        sender_email = Configuration.GamingEmailPassword  # Enter your address
        password = Configuration.GamingEmailPassword
        receiver = self.email
        message = """\
                Subject: Confirmation of user """ + self.user + """
                Hi """ + self.user + """\r\nYou have been Granted access to Gaming Server, Go to link below, 
                login and Download our remote Gaming Software.
                \r\nLink -> http://""" + Configuration.ipAddress + """:""" + str(Configuration.portNumber) + """/"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, self.port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, message)
            return True

    def _getemail(self, details):
        data = details.split("-")
        user = data[0].split(":")
        self._setuser(user[1])
        email = data[1].split(":")
        return email[1]

    def _setuser(self, user):
        self.user = user
