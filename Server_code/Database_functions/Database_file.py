import sqlite3


class DatabaseLite():

    def __init__(self, file_path):
        self.connection = sqlite3.connect(file_path)
        self.cursor = self.connection.cursor()

    def create(self, table_name, *attributes):
        args_str = ", ".join(attributes)
        command = "CREATE TABLE IF NOT EXISTS '%s' (%s);" % (table_name, args_str)
        return self.executes(command)

    def executes(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def insert(self, table_name, *values):
        val = str(values).replace("(", "").replace(")", "").replace(" ", "")
        command = "INSERT INTO %s('key', 'value', 'bool') VALUES(%s)" % (table_name, val)
        return self.executes(command)

    def drop(self, table_name):
        command = "DROP TABLE IF EXISTS '%s'" % (table_name)
        return self.executes(command)

    def select(self, attribute, table_name):
        command = "SELECT %s FROM '%s'" % (attribute, table_name)
        return self.executes(command)

    def close(self):
        self.connection.commit()
        self.connection.close()
