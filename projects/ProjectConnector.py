import datetime
from SQLConnector import SQLConnector


class Project():
    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator
        self.money = 0
        self.createdOn = datetime.datetime.now().strftime('%Y-%m-%d')

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
        name = "'" + self.name + "'"
        desc = "'" + self.description + "'"
        date = "'" + self.createdOn + "'"
        query = {"name": name, "description": desc, "creator": self.creator, "createdOn": date, "money": self.money}
        return query



class ProjectConnector(SQLConnector):
    def __init__(self):
        SQLConnector().__init__()

    def select_all_from(self):
        return SQLConnector().select_all_from("projects")

    def select_from(self, columns):
        return SQLConnector().select_from("projects", columns)

    def select_all_where(self, condition):
        return SQLConnector().select_all_where("projects", condition)

    def select_where(self, columns, condition):
        return SQLConnector().select_where("projects", columns, condition)

    def insert_into(self, project):
        return SQLConnector().insert_into("projects", project.to_database_query())
