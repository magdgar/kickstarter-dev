import MySQLdb


class SQLConnector:
    def __init__(self):
        self.db = MySQLdb.connect(host="173.194.246.10", user="magdalena", passwd="root", db="kickstarter")
        self.cursor = self.db.cursor()
        self.table_name = ""

    def select_all(self):
        self.cursor.execute("SELECT * FROM %s" % self.table_name)
        return self.cursor.fetchall()

    def select_from(self, columns):
        self.cursor.execute("SELECT %s FROM %s" % ((', '.join(columns)), self.table_name))
        return self.cursor.fetchall()

    def select_all_where(self, condition):
        self.cursor.execute("SELECT * FROM %s WHERE %s" % (self.table_name , condition))
        return self.cursor.fetchall()

    def select_where(self, columns, condition):
        self.cursor.execute("SELECT %s FROM %s WHERE %s" % ((', '.join(columns)), self.table_name, condition))
        return self.cursor.fetchall()

    def insert_into(self, keys_and_values):
        keys = (', '.join(keys_and_values.keys()))
        values = (', '.join(map(str, keys_and_values.values())))
        try:
            self.cursor.execute(("INSERT INTO %s(%s) VALUES (%s)" % (self.table_name, keys, values)))
            self.db.commit()
            return True
        except MySQLdb.Error:
            self.db.rollback()
            return False
