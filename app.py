from flask import Flask, render_template, request, jsonify
from src.response_generator import ResponseGenerator
from src.utils import Utils

app = Flask(__name__)
response_generator = ResponseGenerator()
utils = Utils()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-response', methods=['POST'])
def generate_response():
    email = request.form.get('email')
    if utils.validate_email(email):
        response = response_generator.generate_response(email)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid email address'})

if __name__ == '__main__':
    app.run(debug=True)