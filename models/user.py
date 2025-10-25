
class User:
    def __init__(self, username, password, role='user', birth=None):
        self.username = username
        self.password = password
        self.role = role
        self.birth = birth
        self.joined_tours = []
