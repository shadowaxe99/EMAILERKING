from flask import Flask, render_template, request
from src.main import Main
import threading

app = Flask(__name__)
main = Main()
thread = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global thread
    if thread is None:
        thread = threading.Thread(target=main.run)
        thread.start()
    return 'OK'

@app.route('/stop', methods=['POST'])
def stop():
    global thread
    if thread is not None:
        thread.join()
        thread = None
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)