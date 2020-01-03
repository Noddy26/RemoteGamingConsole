import base64

import MySQLdb
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
        Query = """select * from %s where username = '%s';""" % (Configuration.sqlusertable, self.username)
        try:
            self.connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser,
                                                 password=Configuration.sqlpassword)
        except Error as e:
            print("Error reading data from MySQL table", e)
            if (self.connection is not None):
                if (self.connection.is_connected()):
                    self.connection.close()
                    cursor.close()
                    print("MySQL connection is closed")
                    # return False
            try:
                cursor = self.connection.cursor()
                cursor.execute(Query)
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                if (self.connection.is_connected()):
                    self.connection.close()
                return None
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

    def checkForUserPassword(self):
        global cursor
        try:
            self.connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser,
                                                 password=Configuration.sqlpassword)
        except Error as e:
            print("Error reading data from MySQL table", e)
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
                print("MySQL connection is closed")

        password = base64.b64encode(self.password.encode("utf-8"))
        checkpass = str(password).replace("'", "_")
        query = """select * from %s where username = '%s' AND password = '%s';""" \
                % (Configuration.sqlusertable, self.username, checkpass.strip())
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            if len(records) == 0:
                return False
            else:
                return True
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            if (self.connection.is_connected()):
                self.connection.close()

    def getAllUsers(self):
        global cursor, connection
        query = "SELECT * FROM " + Configuration.sqlusertable
        try:
            connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                      user=Configuration.sqluser, password=Configuration.sqlpassword)
        except Error as e:
            print("Error reading data from MySQL table", e)
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
                # return False
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print("Error")
            print(e)
            if (connection.is_connected()):
                connection.close()

    @staticmethod
    def deleteUser(Check):
        User = Check.replace("user", "")
        global cursor, connection
        query = "DELETE FROM %s WHERE id = '%s'" % (Configuration.sqlusertable, User)
        try:
            connection = mysql.connector.connect(host=Configuration.sqlhost, database=Configuration.sqldatabase,
                                                 user=Configuration.sqluser, password=Configuration.sqlpassword)
        except Error as e:
            print("Error reading data from MySQL table", e)
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
                # return False
        try:
            cursor = connection.cursor()
            print(query)
            cursor.execute(query)
            connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print("Error")
            print(e)
            if (connection.is_connected()):
                connection.close()
