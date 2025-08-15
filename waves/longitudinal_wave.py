import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def longitudinal_wave(amplitude_1 = 1, amplitude_2 = 1, frequency_1 = 0.8, frequency_2 = 0.8, wavelength_1 = 2, wavelength_2 = 2, speed_1 = 0.8, speed_2 = 0.8, grid_max=10):
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
  #num_coils = 20     # Jumlah lilitan pegas
  num_coils_1 = (2 * np.pi / wavelength_1)  # rad/satuan untuk pegas 1
  num_coils_2 = (2 * np.pi / wavelength_2)  # rad/satuan untuk pegas 2
  x = np.linspace(0, 10, 1000)  # Posisi x sepanjang pegas

  # Fungsi gelombang longitudinal
  def wave_func(x, t, speed, frequency, wavelength, amplitude):
      return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

  # Fungsi untuk membuat animasi pegas
  def create_animation():
      fig, ax = plt.subplots()
  
      ax.set_xlim(0, 10)
      ax.set_ylim(-5, 5)
      ax.set_xlabel('t')
      ax.set_ylabel('y')
      ax.set_xticks(np.arange(0,grid_max+1,1))
      ax.set_yticks(np.arange(-5,5,1))
      ax.set_title('Animasi Gelombang Longitudinal')
      line_1, = ax.plot([], [], 'b-', lw=2, label=f'y1')
      line_2, = ax.plot([], [], 'r-', lw=2, label=f'y2')
      ax.legend()
      ax.set_aspect('equal', adjustable='box')
      fig.tight_layout()
      plt.grid(True, color='k', linestyle='-', linewidth=0.5)

     

      def update(frame):
          t = frame / 20.0
          
          # Bilangan gelombang (rad/satuan) langsung dari λ
          k1 = 2 * np.pi / wavelength_1
          k2 = 2 * np.pi / wavelength_2
          
          # Posisi x dasar (pegas lurus)
          x_base = x
          
          # Pergeseran longitudinal (maju-mundur sepanjang x)
          u1 = amplitude_1 * np.sin(k1 * x_base - 2 * np.pi * frequency_1 * t)
          u2 = amplitude_2 * np.sin(k2 * x_base - 2 * np.pi * frequency_2 * t)
          
          # Bentuk pegas: sinus kecil untuk memberi efek lilitan
          y_shape_1 = 0.2 * np.sin(20 * np.pi * x_base / wavelength_1) + 4
          y_shape_2 = 0.2 * np.sin(20 * np.pi * x_base / wavelength_2) - 4
          
          # Geser titik pegas di arah x sesuai gelombang longitudinal
          x_disp_1 = x_base + u1
          x_disp_2 = x_base + u2
          
          # Update data
          line_1.set_data(x_disp_1, y_shape_1)
          line_2.set_data(x_disp_2, y_shape_2)
          
          return line_1, line_2



      ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
      return ani.to_jshtml()
  
  return create_animation()















