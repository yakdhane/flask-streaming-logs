
import subprocess
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    process = subprocess.Popen(['tail', '-f', 'app.log'], stdout=subprocess.PIPE)
    def generate():
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                yield output.strip() + b'<br/>\n'
    return app.response_class(generate(), mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
