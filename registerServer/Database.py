import base64

import mysql.connector
from mysql.connector import Error

from Configuration import Configuration
from Methods.StoreUserDataInFile import StoreDataInFile


class Database:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.connection = None

    def addUser(self):
        if StoreDataInFile(self.username, self.password, self.email).run() is True:
            return True
        return False


    def checkuserReg(self):
        global cursor, tuple
        try:
            self.connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser,
                                                 password=Configuration.sqlpassword)

            Query = """select * from %s where username = '%s';""" % (Configuration.sqlusertable, self.username)
            cursor = self.connection.cursor()
            cursor.execute(Query)
            records = cursor.fetchall()
            if len(records) == 0:
                return False
            for each in records:
                tuple = each
            if tuple[1] == self.username:
                if tuple[3] == self.email:
                    Configuration.emailUserCount = True
                    return True
                else:
                    return True
            return False

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")
                #return False

    def checkForUserPassword(self):
        global cursor
        try:
            self.connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser,
                                                 password=Configuration.sqlpassword)
            password = str(base64.b64encode(self.password.encode("utf-8")))
            checkpass = password.replace("'", "_")
            query = """select * from %s where username = '%s' AND password = '%s';""" % (Configuration.sqlusertable, self.username, checkpass)
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            if len(records) == 0:
                return False
            else:
                for each in records:
                    tuple = each
                    if tuple[1] == self.username and tuple[2] == self.password:
                        return True
                    return False

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")
                #return False
