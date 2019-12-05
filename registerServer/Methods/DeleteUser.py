import os

from Methods.ConfirmationEmail import ConfirmationEmail
from Methods.FileMethods import FileMethods
from Configuration import Configuration


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
