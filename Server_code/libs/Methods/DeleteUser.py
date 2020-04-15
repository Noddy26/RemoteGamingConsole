from libs.Methods.ConfirmationEmail import ConfirmationEmail
from libs.Methods.FileMethods import FileMethods


class DeleteUser:

    def __init__(self, userDetails):
        self.userdetails = userDetails
        self.username = self._getusername()

    def run(self):
        ConfirmationEmail(self.userdetails).delete()
        FileMethods.removefile(self.username)
        return True

    def _getusername(self):
        data = self.userdetails.split("-")
        user = data[0].split(":")
        return user[1]
