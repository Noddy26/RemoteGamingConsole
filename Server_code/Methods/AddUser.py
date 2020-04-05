from variables.Configuration import Configuration
import mysql.connector
from mysql.connector import Error
from Methods.FileMethods import FileMethods


class AddUser:

    def __init__(self, userDetails):
        self.userdetails = userDetails
        self.connection = None
        self.cursor = None

    def run(self):
        try:
            self.connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser,
                                                 password=Configuration.sqlpassword)
            self.userdetails = self._getUserQuery()
            self.cursor = self.connection.cursor()
            Query = self.userdetails
            print(self.cursor)
            self.cursor.execute(Query)
            self.connection.commit()
            FileMethods.removefile(self.userName)
            return True

        except Error as e:
            print("Error reading data from MySQL table", e)
            return False
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                if self.cursor is not None:
                    self.cursor.close()
                print("MySQL connection is closed")

    def _getUserQuery(self):
        data = self.userdetails.split("-")
        user = data[0].split(":")
        self.userName = user[1]
        with open(Configuration.adduserdir + self.userName + ".txt", "r") as f:
            sql = f.readline()
        return sql
