from Configuration import Configuration
import mysql.connector
from mysql.connector import Error
from Methods.FileMethods import FileMethods


class AddUser:

    def __init__(self, userDetails):
        self.userdetails = userDetails
        self.connection = None

    def run(self):
        global cursor
        try:
            self.connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser,
                                                 password=Configuration.sqlpassword)
            self.userdetails = self._getUserQuery()
            Query = self.userdetails
            cursor = self.connection.cursor()
            cursor.execute(Query)
            FileMethods.removefile(self.userName)
            return True

        except Error as e:
            print("Error reading data from MySQL table", e)
            return False
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")

    def _getUserQuery(self):
        data = self.userdetails.split("-")
        user = data[0].split(":")
        self.userName = user[1]
        with open(Configuration.adduserdir + self.userName + ".txt", "r") as f:
            sql = f.readline()
        return sql
