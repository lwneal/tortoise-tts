import os
import subprocess
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        voice = request.form.get('voice', '')
        preset = request.form.get('preset', '')

        cmd = [
            'python', 'tortoise/do_tts.py',
            '--text', text,
            '--voice', voice,
            '--preset', preset,
            '--candidates', '1',
        ]
        subprocess.run(cmd)

        return 'Generated audio files.'
    return render_template('index.html', os=os)


@app.route('/results/<path:filename>')
def get_result(filename):
    return send_from_directory('results', filename)


if __name__ == '__main__':
    app.run(port=7861, debug=True)
