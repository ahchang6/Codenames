from flask import Flask, jsonify, request, abort
from game import Game
import logging


sessions = {}
running = True

app = Flask(__name__)


def get_words(room_id):
    return str(sessions[room_id].process_list)


@app.route('/get_info/<string:room_id>', methods=['GET'])
def get_info(room_id):
    if room_id in sessions:
        return get_words(room_id)


@app.route('/play_move/<string:room_id>/<int:x>/<int:y>', methods=['POST'])
def play_move(room_id):
    if room_id in sessions:
        return get_words(room_id)


@app.route('/create_room/', methods=['GET'])
def create_room():
    new_room = Game()
    while new_room.room in sessions:
        new_room = Game()
    sessions[new_room.room] = new_room
    return sessions[new_room.room].room


if __name__ == '__main__':
    app.run(debug=True)
