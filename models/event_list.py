from models.event import *
import datetime


event1 = Event(
    datetime.date(2020, 5, 17),
    "Wedding",
    100,
    "Ballroom",
    "Mr and Mrs Smith's wedding",
    False,
)
event2 = Event(
    datetime.date(2021, 7, 18),
    "Birthday Party",
    80,
    "Function hall",
    "Sally Summer's 21st bday",
    True,
)
event3 = Event(
    datetime.date(2022, 7, 12),
    "Business conference",
    200,
    "Conference Room",
    "Software Developer's convention",
    True,
)


events = [event1, event2, event3]


def save_event(new_event):
    events.append(new_event)
