import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, request, send_from_directory
import os
import logging


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

app = Flask(__name__)
STATIC_FOLDER = 'static'

# Parameter gelombang
frequency = 0.8  # Frekuensi gelombang
wavelength = 2     # Panjang gelombang
amplitude = 0.2    # Amplitudo, dikurangi untuk tampilan yang lebih baik
speed = 0.8        # Kecepatan gelombang

# Parameter untuk pegas
num_coils = 20     # Jumlah lilitan pegas
x = np.linspace(0, 4 * np.pi, 1000)  # Posisi x sepanjang pegas

# Fungsi gelombang longitudinal
def wave_func(x, t, speed, frequency, wavelength, amplitude):
    return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

# Fungsi untuk membuat animasi pegas
def create_animation():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-10, 10)
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        t = frame / 20.0
        # Perpindahan longitudinal sesuai dengan fungsi gelombang
        y = np.sin(num_coils * x + wave_func(x, t, speed, frequency, wavelength, amplitude))
        x_disp = x + wave_func(x, t, speed, frequency, wavelength, amplitude)
        line.set_data(x_disp, y)
        return line,

    ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, interval=50, blit=True)

    plt.show()

create_animation()

@app.route('/', methods=['GET', 'POST'])
def home():
    img = None
    if request.method == 'POST':
        try:
            frequency = float(request.form['frequency'])
            wavelength = float(request.form['wavelength'])
            amplitude = float(request.form['amplitude'])
            speed = float(request.form['speed'])
            create_animation(frequency, wavelength, amplitude, speed)
            img = 'animation.gif'
        except Exception as e:
            logging.error(f"Error in home route: {e}")
    return render_template('index.html', img=img)

@app.route('/static/<path:filename>')
def static_file(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
