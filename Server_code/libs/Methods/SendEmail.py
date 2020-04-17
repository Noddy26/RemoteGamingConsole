import smtplib, ssl  # ssl is secure socket layer, designed to set up secure conection between client and server # smtp = Simple Mail Transfer Protocol
from libs.variables.Configuration import Configuration


class SendEmail:

    def __init__(self, email, user):
        print(email)
        self.user = user
        self.email = email
        self.port = 465
        self.context = None

    def run(self):
        try:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = Configuration.GamingEmailAddress
            password = Configuration.GamingEmailPassword
            receiver = Configuration.AdminemailAddress
            message = "\r\n".join([
                "From: " + Configuration.GamingEmailAddress,
                "\r\nTo: " + receiver,
                "\r\nSubject: Confirmation",
                "",
                "\r\nUser %s: %s  Wants to register for Gaming Server" % (self.user, self.email)
            ])

            self.context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=self.context) as server:
                print(sender_email)
                print(password)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver, message)
                return True
        except smtplib.SMTPAuthenticationError as e:
            print("Problem logging in to email")
            print(e)
            return True



