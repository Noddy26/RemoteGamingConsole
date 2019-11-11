from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl #ssl is secure socket layer, designed to set up secure conection between client and server # smtp = Simple Mail Transfer Protocol

class SendEmail:

    def __init__(self, email, user):
        print(email)
        self.user = user
        self.email = email
        self.port = 465

    def run(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "gamingserver.project@gmail.com"  # Enter your address
        password = "GamingServer2019"
        receiver = self.email
        message = """\
        Subject: Confirmation of user """ + self.user + """
        User """ + self.user + """  """ + self.email + """ Whats to register for Gaming Server tap link to grant access\n
        Link -> http://192.168.0.101:3000/"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver, message)
            return True




