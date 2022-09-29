from flask import render_template, request, redirect
from app import app
from models.event_list import events, save_event
from models.event import Event
import datetime


@app.route("/events")
def index():
    return render_template("index.html", title="Home", events=events)


@app.route("/events", methods=["POST"])
def add_event():
    form_date = request.form["date"]
    split_date = form_date.split("-")
    form_date = datetime.date(
        int(split_date[0]), int(split_date[1]), int(split_date[2])
    )
    name = request.form["name"]
    guest_num = request.form["guest_num"]
    location = request.form["location"]
    description = request.form["description"]
    new_event = Event(
        date=form_date,
        name=name,
        guest_num=guest_num,
        room=location,
        description=description,
        recurring=False,
    )
    save_event(new_event)
    return redirect("/events")


# @app.route("/events", methods=["POST"])
# def add_event():

#     form_date = request.form["date"]
#     split_date = form_date.split("-")
#     form_date = datetime.date(
#         int(split_date[0]), int(split_date[1]), int(split_date[2])
#     )
#     name = request.form["name"]
#     guest_num = request.form["guest_num"]
#     location = request.form["location"]
#     description = request.form["description"]

#     new_event = Event(
#         # datetime.date(int(form_date[0:4]), int(form_date[5]), int(form_date[-1])),
#         date=form_date,
#         name=name,
#         guest_num=guest_num,
#         location=location,
#         description=description,
#     )

#     save_event(new_event)
#     return redirect("/events")
