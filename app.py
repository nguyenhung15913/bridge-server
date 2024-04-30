from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Fake data for rooms, later we will apply database concept

rooms = [
    {
        "name": "#R034",
        "latest_time": "4:27 PM",
        "latest_message": "you: Wassup dude",
        "status": "read",
        "message_counter": 0,
    },
    {
        "name": "#A102",
        "latest_time": "4:21 PM",
        "latest_message": "Phu: Wassup dude",
        "status": "unread",
        "message_counter": 4,
    },
    {
        "name": "#B207",
        "latest_time": "4:22 PM",
        "latest_message": "Vinit: Wassup dude",
        "status": "unread",
        "message_counter": 2,
    },
    {
        "name": "#D409",
        "latest_time": "4:15 PM",
        "latest_message": "John: Wassup dude",
        "status": "unread",
        "message_counter": 8,
    },
    {
        "name": "#C315",
        "latest_time": "3:27 PM",
        "latest_message": "you: Wassup dude",
        "status": "read",
        "message_counter": 0,
    }
]
    
    


# Create a route that handle request from client, this function is to send all rooms to the client
@app.route("/room")
def get_all_rooms():
    return jsonify(rooms), 200


# This function is to send a specific room detail ot the client "roomName" is a name that is sent from client request
@app.route("/room/<roomName>")
def get_room(roomName):
    result = {}
    for room in rooms:
        if room == roomName:
            result = room

    return jsonify(result), 200        
