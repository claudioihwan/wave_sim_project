import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def longitudinal_wave(amplitude_1 = 0.2, amplitude_2 = 0.2, frequency_1 = 0.8, frequency_2 = 0.8, wavelength_1 = 2, wavelength_2 = 2, speed_1 = 0.8, speed_2 = 0.8):
  # Parameter gelombang
  frequency_1 = float(frequency_1) # Frekuensi gelombang
  frequency_2 = float(frequency_2) # Frekuensi gelombang
  wavelength_1 = float(wavelength_1)     # Panjang gelombang
  wavelength_2 = float(wavelength_2)     # Panjang gelombang
  amplitude_1 = float(amplitude_1)    # Amplitudo, dikurangi untuk tampilan yang lebih baik
  amplitude_2 = float(amplitude_2)    # Amplitudo, dikurangi untuk tampilan yang lebih baik
  speed_1 = float(speed_1)        # Kecepatan gelombang
  speed_2 = float(speed_2)        # Kecepatan gelombang

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
      ax.set_xlabel('t')
      ax.set_ylabel('y')
      ax.set_title('Animasi Gelombang Longitudinal')
      line_1, = ax.plot([], [], 'b-', lw=2, label=f'y1')
      line_2, = ax.plot([], [], 'r-', lw=2, label=f'y2')
      ax.legend()
      ax.set_aspect('equal', adjustable='box')
      fig.set_constrained_layout(True)
      plt.grid(True, color='k', linestyle='-', linewidth=0.5)

     

      def update(frame):
          t = frame / 20.0
          # Perpindahan longitudinal sesuai dengan fungsi gelombang
          y_1 = np.sin(num_coils * x + wave_func(x, t, speed_1, frequency_1, wavelength_1, amplitude_1)) + 4
          x_disp_1 = x + wave_func(x, t, speed_1, frequency_1, wavelength_1, amplitude_1)
          line_1.set_data(x_disp_1, y_1)

          y_2 = np.sin(num_coils * x + wave_func(x, t, speed_2, frequency_2, wavelength_2, amplitude_2)) - 4
          x_disp_2 = x + wave_func(x, t, speed_2, frequency_2, wavelength_2, amplitude_2)
          line_2.set_data(x_disp_2, y_2)

          return line_1, line_2

      ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
      return ani.to_jshtml()
  
  return create_animation()

