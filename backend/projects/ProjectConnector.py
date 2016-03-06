import datetime

from backend.SQLConnector import SQLConnector

TABLE_NAME = "projects"


class Project:
    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator
        self.money = 0
        self.createdOn = datetime.datetime.now().isoformat(' ')

    def to_json_obj(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creator': self.creator,
            'money': self.money,
            'date': self.createdOn
            }
        return obj

    def to_database_query(self):
        data = [self.name, self.description, self.createdOn]
        data = [repr(x) for x in data]
        data.append(self.creator)
        labels = ["name", "description", "createdOn", "creator"]
        return dict(zip(labels, data))


class ProjectConnector(SQLConnector):
    def __init__(self):
        SQLConnector.__init__(self)
        self.table_name = TABLE_NAME

    def insert_into(self, project):
        return SQLConnector.insert_into(self, project.to_database_query())


