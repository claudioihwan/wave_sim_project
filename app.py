from flask import Flask, render_template, request, send_from_directory
import numpy as np
import matplotlib.pyplot as plt
import os
import logging

app = Flask(__name__)
STATIC_FOLDER = 'static'

logging.basicConfig(level=logging.DEBUG)

def wave_func(x, t, speed, frequency, wavelength, amplitude):
    return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

def save_static_image(frequency, wavelength, amplitude, speed, filename='static_image.png'):
    try:
        logging.debug(f"Parameters received: frequency={frequency}, wavelength={wavelength}, amplitude={amplitude}, speed={speed}")
        num_coils = 20
        x = np.linspace(0, 4 * np.pi, 1000)

        fig, ax = plt.subplots()
        ax.set_xlim(0, 4 * np.pi)
        ax.set_ylim(-1, 1)

        t = 0
        y = np.sin(num_coils * x + wave_func(x, t, speed, frequency, wavelength, amplitude))
        x_disp = x + wave_func(x, t, speed, frequency, wavelength, amplitude)
        ax.plot(x_disp, y, lw=2)

        if not os.path.exists(STATIC_FOLDER):
            os.makedirs(STATIC_FOLDER)

        fig.savefig(os.path.join(STATIC_FOLDER, filename))
        plt.close(fig)

        return filename
    except Exception as e:
        logging.error(f"Error in save_static_image: {e}")
        raise

@app.route('/', methods=['GET', 'POST'])
def home():
    img = None
    if request.method == 'POST':
        try:
            frequency = float(request.form['frequency'])
            wavelength = float(request.form['wavelength'])
            amplitude = float(request.form['amplitude'])
            speed = float(request.form['speed'])
            img = save_static_image(frequency, wavelength, amplitude, speed)
        except Exception as e:
            logging.error(f"Error in home route: {e}")
    return render_template('index.html', img=img)

@app.route('/static/<path:filename>')
def static_file(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
