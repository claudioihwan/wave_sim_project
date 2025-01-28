from flask import Flask, render_template, request, send_from_directory
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

app = Flask(__name__)
STATIC_FOLDER = 'static'

def wave_func(x, t, speed, frequency, wavelength, amplitude):
    return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

def create_animation(frequency, wavelength, amplitude, speed, filename='animation.gif'):
    num_coils = 20
    x = np.linspace(0, 4 * np.pi, 1000)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-1, 1)
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        t = frame / 20.0
        y = np.sin(num_coils * x + wave_func(x, t, speed, frequency, wavelength, amplitude))
        x_disp = x + wave_func(x, t, speed, frequency, wavelength, amplitude)
        line.set_data(x_disp, y)
        return line,

    ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, interval=50, blit=True)

    if not os.path.exists(STATIC_FOLDER):
        os.makedirs(STATIC_FOLDER)

    ani.save(os.path.join(STATIC_FOLDER, filename), writer='imagemagick')
    plt.close(fig)

@app.route('/', methods=['GET', 'POST'])
def home():
    img = None
    if request.method == 'POST':
        frequency = float(request.form['frequency'])
        wavelength = float(request.form['wavelength'])
        amplitude = float(request.form['amplitude'])
        speed = float(request.form['speed'])
        create_animation(frequency, wavelength, amplitude, speed)
        img = 'animation.gif'
    return render_template('index.html', img=img)

@app.route('/static/<path:filename>')
def static_file(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
