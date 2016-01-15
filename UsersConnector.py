from SQLConnector import SQLConnector

TABLE_NAME = "users"


class User:
    def __init__(self, google_id, name):
        self.name = name
        self.money = 0
        self.google_id = google_id

    def to_json_obj(self):
        obj = {
            'name': self.name,
            'money': self.money,
            'google_id': self.google_id
            }
        return obj

    def to_database_query(self):
        name = "'" + self.name + "'"
        google_id = "'" + self.google_id + "'"
        query = {"name": name, "money": self.money, "google_id": google_id}
        return query


class UserConnector(SQLConnector):
    def __init__(self):
        SQLConnector.__init__(self)
        self.table_name = TABLE_NAME
        SQLConnector.table_name = TABLE_NAME


    def insert_into(self, user):
        return SQLConnector.insert_into(self, user.to_database_query())


