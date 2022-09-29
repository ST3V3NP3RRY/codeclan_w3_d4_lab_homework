class Event:
    def __init__(self, date, name, guest_num, room, description, recurring):
        self.date = date
        self.name = name
        self.guest_num = guest_num
        self.room = room
        self.description = description
        self.recurring = recurring
