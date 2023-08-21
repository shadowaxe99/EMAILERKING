from flask import Flask, request
from src.agent import Agent

app = Flask(__name__)
agent = Agent()

@app.route('/process', methods=['POST'])
def process_request():
    request_data = request.get_json()
    response = agent.process_request(request_data)
    return response

if __name__ == '__main__':
    app.run(debug=True)