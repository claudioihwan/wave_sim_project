import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameter untuk pegas
num_coils = 20     # Jumlah lilitan pegas
x = np.linspace(0, 4 * np.pi, 1000)  # Posisi x sepanjang pegas

# Fungsi gelombang longitudinal
def wave_func(x, t, speed, frequency, wavelength, amplitude):
    return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

# Fungsi untuk membuat animasi pegas
def create_animation(frequency, wavelength, amplitude, speed):
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
    return ani.to_jshtml()

