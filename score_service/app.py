from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for scores
scores = []

@app.route('/scores', methods=['POST'])
def submit_score():
    data = request.json
    score = data.get('score')
    player = data.get('player')
    
    if score is None or player is None:
        return jsonify({'error': 'Score and player are required'}), 400
    
    scores.append({'player': player, 'score': score})
    return jsonify({'message': 'Score submitted successfully'}), 201

@app.route('/scores', methods=['GET'])
def get_scores():
    return jsonify(scores), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)