import smtplib, ssl #ssl is secure socket layer, designed to set up secure conection between client and server # smtp = Simple Mail Transfer Protocol
from Configuration import Configuration


class SendEmail:

    def __init__(self, email, user):
        print(email)
        self.user = user
        self.email = email
        self.port = 465

    def run(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = Configuration.GamingEmailAddress
        password = Configuration.GamingEmailPassword
        receiver = Configuration.AdminemailAddress
        message = """\
        Subject: Confirmation of user """ + self.user + """
        User """ + self.user + """  """ + self.email + """ Wants to register for Gaming Server tap link to grant access\n
        \r\nLink -> http://""" + Configuration.ipAddress + """:""" + str(Configuration.portNumber) + """/"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, message)
            return True




