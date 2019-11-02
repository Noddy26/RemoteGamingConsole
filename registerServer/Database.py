import mysql.connector
from mysql.connector import Error

from registerServer import Configuration
from registerServer.Methods.StoreUserDataInFile import StoreDataInFile


class Database:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def addUser(self):
        if StoreDataInFile(self.username, self.password, self.email).run() is True:
            return True
        return False


    def checkuserReg(self):
        global connection, cursor, tuple
        try:
            connection = mysql.connector.connect(host='localhost', database='users',
                                                 user='root',
                                                 password='12shroot')

            Query = """select * from registeredusers where username = '%s'""" % (self.username)
            cursor = connection.cursor()
            cursor.execute(Query)
            records = cursor.fetchall()
            if len(records) == 0:
                return False
            for each in records:
                tuple = each
            if tuple[1] == self.username:
                if tuple[3] == self.email:
                    Configuration.Configuration.emailUserCount = True
                    return True
                else:
                    return True
            return False

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
                return False

    def checkForUserPassword(self):
        global connection, cursor
        try:
            connection = mysql.connector.connect(host='localhost', database='users',
                                                 user='root',
                                                 password='12shroot')

            query = """select * from registeredusers where username = '%s' AND password = '%s'""" % (self.username, self.password)
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            if len(records) == 0:
                return False
            else:
                for each in records:
                    tuple = each
                    a, b, c, d = tuple
                    if b == self.username and c == self.password:
                        return True
                    return False

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
                return False
