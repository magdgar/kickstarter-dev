import datetime

from SQLConnector import SQLConnector

TABLE_NAME = "transactions"


class Transaction:
    def __init__(self, project_id, user_id, money):
        self.project_id = project_id
        self.user_id = user_id
        self.money = money
        self.time = datetime.datetime.now().isoformat(' ')

    def to_json_obj(self):
        obj = {
            'id': self.id,
            'project-id': self.project_id,
            'user_id': self.user_id,
            'money': self.money,
            'time': self.time
            }
        return obj

    def to_database_query(self):
        project_id = "'" + self.project_id + "'"
        user_id = "'" + self.user_id + "'"
        money = "'" + self.money + "'"
        time = "'" + self.time + "'"
        query = {"project_id": project_id, "user_id": user_id, "money": money, "timestamp": time}
        return query


class TransactionConnector(SQLConnector):
    def __init__(self):
        SQLConnector.__init__(self)
        self.table_name = TABLE_NAME

    def insert_into(self, transaction):
        return SQLConnector.insert_into(self, transaction.to_database_query())
