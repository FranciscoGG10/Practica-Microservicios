from flask import Flask, jsonify, request

app = Flask(__name__)

games = []

@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(games), 200

@app.route('/games', methods=['POST'])
def create_game():
    game_data = request.json
    games.append(game_data)
    return jsonify(game_data), 201

@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    if 0 <= game_id < len(games):
        return jsonify(games[game_id]), 200
    return jsonify({'error': 'Game not found'}), 404

@app.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    if 0 <= game_id < len(games):
        game_data = request.json
        games[game_id] = game_data
        return jsonify(game_data), 200
    return jsonify({'error': 'Game not found'}), 404

@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    if 0 <= game_id < len(games):
        games.pop(game_id)
        return jsonify({'message': 'Game deleted'}), 204
    return jsonify({'error': 'Game not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)