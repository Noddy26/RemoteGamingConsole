from Methods import FileMethods
from Methods import ConfirmationEmail


class DeleteUser:

    def __init__(self, userDetails):
        self.userdetails = userDetails
        self.username = self._getusername()

    def run(self):
        ConfirmationEmail.delete(self.userdetails)
        FileMethods.removefile(self.username, self.userdetails)

    def _getusername(self):
        data = self.userdetails.split("-")
        user = data[0].split(":")
        return user[1]
