import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name):
        self.name = new_name

    def increment_rate(self):
        self.rate += 1

    def ban_user(self):
        self.is_banned = True

    def unban_user(self):
        self.is_banned = False

    def __repr__(self):
        info = f"User {self.name}: id: {self.id}, comments: {self.comments_count}, rate: {self.rate} "
        if self.is_banned:
            info += "is banned.\n"
        else:
            info += "isn't banned\n"
        return info
