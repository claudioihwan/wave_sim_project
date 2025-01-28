from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import io
import base64
from PIL import Image

app = Flask(__name__)

frequency = 0.8  # Frekuensi gelombang
wavelength = 2     # Panjang gelombang
amplitude = 0.2    # Amplitudo, dikurangi untuk tampilan yang lebih baik
speed = 0.8        # Kecepatan gelombang
num_coils = 20     # Jumlah lilitan pegas
x = np.linspace(0, 4 * np.pi, 1000)  # Posisi x sepanjang pegas

def wave_func(x, t, speed, frequency, wavelength, amplitude):
    return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

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
        y = np.sin(num_coils * x + wave_func(x, t, speed, frequency, wavelength, amplitude))
        x_disp = x + wave_func(x, t, speed, frequency, wavelength, amplitude)
        line.set_data(x_disp, y)
        return line,

    ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, interval=50, blit=True)

    # Simpan frame animasi sebagai gambar
    frames = []
    for i in range(200):
        update(i)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        img = Image.open(buf)
        frames.append(img)

    # Simpan sebagai GIF menggunakan Pillow
    buf = io.BytesIO()
    frames[0].save(buf, format='GIF', save_all=True, append_images=frames[1:], loop=0, duration=50)
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)  # Menutup plt untuk menghemat memori
    return img

@app.route('/')
def home():
    img = create_animation()
    return render_template('index.html', img=img)

if __name__ == '__main__':
    app.run(debug=True)

