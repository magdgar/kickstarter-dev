from SQLConnector import SQLConnector

TABLE_NAME = "users"


class User:
    def __init__(self, name):
        self.name = name
        self.money = 0

    def to_json_obj(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'money': self.money,
            }
        return obj

    def to_database_query(self):
        name = "'" + self.name + "'"
        query = {"id": self.id, "name": name, "money": self.money}
        return query


class UserConnector(SQLConnector):
    def __init__(self):
        SQLConnector.__init__(self)
        self.table_name = TABLE_NAME

    def insert_into(self, project):
        return SQLConnector().insert_into(User.to_database_query())


