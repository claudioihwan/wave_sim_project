import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, request, send_from_directory
import logging
from longitudinal_wave import create_animation

app = Flask(__name__)
STATIC_FOLDER = 'static'

logging.basicConfig(level=logging.DEBUG)



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/output')
def get_output():
    frequency = float(request.args.get('frequency'))
    wavelength = float(request.args.get('wavelength'))
    amplitude = float(request.args.get('amplitude'))
    speed = float(request.args.get('speed'))

    return f"<a href='/'>Back To Home</a><br> {create_animation(frequency, wavelength, amplitude, speed)}"

@app.route('/static/<path:filename>')
def static_file(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
