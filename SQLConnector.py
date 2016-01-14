import MySQLdb


class SQLConnector:
    def __init__(self):
        self.db = MySQLdb.connect(host="173.194.246.10", user="magdalena", passwd="root", db="kickstarter")
        self.cursor = self.db.cursor()

    def select_all_from(self, table_name):
        self.cursor.execute("SELECT * FROM %s" % (table_name))
        return self.cursor.fetchall()

    def select_from(self, table_name, columns):
        self.cursor.execute("SELECT %s FROM %s" % ((', '.join(columns)), table_name))
        return self.cursor.fetchall()

    def select_all_where(self, table_name, condition):
        self.cursor.execute("SELECT * FROM %s WHERE %s" % (table_name, condition))
        return self.cursor.fetchall()

    def select_where(self, table_name, columns, condition):
        self.cursor.execute("SELECT %s FROM %s WHERE %s" % ((', '.join(columns)), table_name, condition))
        return self.cursor.fetchall()

    def insert_into(self, table_name, keys_and_values):
        keys = (', '.join(keys_and_values.keys()))
        values = (', '.join(map(str, keys_and_values.values())))
        try:
            self.cursor.execute(("INSERT INTO %s(%s) VALUES (%s)" % (table_name, keys, values)))
            self.db.commit()
            return True
        except MySQLdb.Error:
            self.db.rollback()
            return False
