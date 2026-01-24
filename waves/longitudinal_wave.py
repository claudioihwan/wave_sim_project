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
  x0 = np.linspace(0, 10, 80)  # Posisi x sepanjang pegas
  colors = ["tab:blue" if i % 2 == 0 else "tab:red" for i in range(len(x))]



  # Fungsi gelombang longitudinal
  def wave_func(x, t, speed, frequency, wavelength, amplitude):
      return amplitude * np.sin(2 * np.pi * frequency * (x / wavelength - speed * t))

  # Fungsi untuk membuat animasi pegas
  def create_animation():
      fig, ax = plt.subplots()
  
      ax.set_xlim(0, 10)
      ax.set_ylim(-5, 5)
      ax.set_xlabel('Posisi X')
      ax.set_ylabel('Posisi Y')
      ax.set_xticks(np.arange(0,grid_max+1,1))
      ax.set_yticks(np.arange(-5,5,1))
      ax.set_title('Animasi Gelombang Longitudinal')
      #points_1 = ax.scatter([], [], s=30, c='b')
      #points_2 = ax.scatter([], [], s=30, c='r')
      points_1 = ax.scatter(x, np.zeros_like(x) + 4, c=colors, s=30)
      points_2 = ax.scatter(x, np.zeros_like(x) - 4, c=colors, s=30)

      #line_1, = ax.plot([], [], 'b-', lw=1, label=f'y1')
      #line_2, = ax.plot([], [], 'r-', lw=1, label=f'y2')
      ax.legend()
      #ax.set_aspect('equal', adjustable='box')
      fig.tight_layout()
      plt.grid(True, color='k', linestyle='-', linewidth=0.5)

     

      def update(frame):
          t = frame * 0.02   # lebih lambat & stabil
      
          k1 = 2 * np.pi / wavelength_1
          k2 = 2 * np.pi / wavelength_2
      
          omega1 = 2 * np.pi * frequency_1
          omega2 = 2 * np.pi * frequency_2
      
          # simpangan longitudinal (KECIL!)
          dx1 = 0.3 * amplitude_1 * np.sin(k1 * x0 - omega1 * t)
          dx2 = 0.3 * amplitude_2 * np.sin(k2 * x0 - omega2 * t)
      
          # posisi aktual = posisi setimbang + simpangan
          x1 = x0 + dx1
          x2 = x0 + dx2
      
          # Y tetap → ini kunci anti "bukit-lembah"
          y1 = np.zeros_like(x1) + 4
          y2 = np.zeros_like(x2) - 4
      
          points_1.set_offsets(np.c_[x1, y1])
          points_2.set_offsets(np.c_[x2, y2])

          return points_1, points_2





      ani = animation.FuncAnimation(fig, update, frames=120, interval=50, blit=True)
      return ani.to_jshtml()
  
  return create_animation()
















































