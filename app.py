from flask import Flask,render_template,request,session,redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room, send
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "ROOM"
socketio = SocketIO(app)

rooms = {}

def generate_unique_code(Length): # New code when a room is created
    while True:
        code = ""
        for _ in range(Length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code


@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html", error="Please enter a name!", code=code, name=name)

        if join != False and not code:
            return render_template("home.html", error="Please enter a room code!", code=code, name=name)

        room = code
        if create != False: # If creating a room
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms: # If joining a room and room code does not exist
            return render_template("home.html", error="Room does not exist!", code=code, name=name)

        # Stores semi-permanent user data
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))


    return render_template("home.html")

@app.route("/room")
def room():
    room = session.get("room")

    # Check to make sure they originally visit the homepage and do not directly connect to room page
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home.html"))
    return render_template("room.html", code=room, messages=rooms[room]["messages"])

@socketio.on("connect") # Listening for a new connection
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name: # If theres no room or name do nothing
        return
    if room not in rooms: # leave the room if it does not exist
        leave_room(room)
        return

    join_room(room) # Otherwise we know the room exists so we can put the user inside it
    send({"name": name, "message": "has joined the chat room!"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}") 

@socketio.on("disconnect") # Listening for a disconnection
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    send({"name": name, "message": "has left the chat room!"}, to=room)
    print(f"{name} left room {room}")

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room] # Delete this room if everyone has left the room

@socketio.on("message") # Listening for a new message
def message(data):
    room = session.get("room")
    if room not in rooms:
        return

    content = {
        "name": session.get("name"), "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content) # Save history of messages in room while users are still present in room
    print(f"{session.get("name")} said: {data['data']}")

if __name__ == "__main__":
    socketio.run(app, debug=True, host="localhost", port=5000)


