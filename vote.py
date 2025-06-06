from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

votes = {1: 0, 2: 0, 3: 0}

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    cid = data.get('candidateId')
    if cid in votes:
        votes[cid] += 1
        return "Thank you for voting!", 200
    return "Invalid candidate", 400

# Optional route to view results (only for admin, protect it)
@app.route('/results', methods=['GET'])
def results():
    return votes

if __name__ == '__main__':
    app.run()
