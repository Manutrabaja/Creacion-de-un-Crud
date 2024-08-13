import uuid


class ClientModule:

    def __init__(self, name, last_name, company, email, position, uid=None):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['name', 'last_name', 'company','email', 'position','uid']

