import datetime
import SQLConnector

class Project():
    def __init__(self, id, name, description, creator):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.money = 0
        self.createdOn = datetime.datetime.now().strftime('%Y-%m-%d')


class ProjectConnector(SQLConnector):
    def __init__(self):
        super()
        


