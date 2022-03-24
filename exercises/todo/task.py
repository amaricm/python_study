class Task(object):
    def __init__(self, id, name, description):
        self.name = name
        self.id = id
        self.description = description

    def pretty_print(self):
        return str(self.id) + "       " + self.name + "       " + self.description