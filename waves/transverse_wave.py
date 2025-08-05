import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def transverse_wave(amplitude_1, amplitude_2, frequency_1, frequency_2, wavelength_1, wavelength_2, grid_max=10):
  fig, ax = plt.subplots()
  x = np.linspace(0, grid_max, 1000)
  t = 0

  lambda_1 = float(wavelength_1)
  lambda_2 = float(wavelength_2)
  k_1 = 2 * np.pi / lambda_1
  k_2 = 2 * np.pi / lambda_2
  W_1 = 2 * np.pi * float(frequency_1)
  W_2 = 2 * np.pi * float(frequency_2)
  A_1 = float(amplitude_1)
  A_2 = float(amplitude_2)
  
  y_1 = A_1 * np.sin(k_1 * x - W_1 * t) + 1
  y_2 = A_2 * np.sin(k_2 * x - W_2 * t) - 1
  line_y_1, = ax.plot(x, y_1, 'b-', linewidth=2, label=f'y1')
  line_y_2, = ax.plot(x, y_2, 'r-', linewidth=2, label=f'y2')
  
  ax.set_xlabel('t')
  ax.set_ylabel('y')
  ax.set_title('Animasi Gelombang Transversal')
  ax.set_xticks(np.arange(0,grid_max+1,1))
  ax.set_xlim(0,10)
  ax.set_yticks(np.arange(-5,5,1))
  ax.set_ylim(-5,5)
  ax.set_aspect('equal', adjustable='box')
  fig.set_constrained_layout(True)
  
  
  ax.legend()
  plt.grid(True, color='k', linestyle='-', linewidth=0.5)
  


  # Fungsi update animasi
  def update(frame):
      time = frame / 30
      line_y_1.set_ydata(A_1 * np.sin(k_1 * x - W_1 * (t + frame / 5.0)) + 1) # Mempercepat pergerakan
      line_y_2.set_ydata(A_2 * np.sin(k_2 * x - W_2 * time) - 1)# Mempercepat pergerakan
      return line_y_1, line_y_2

  # Membuat animasi
  ani = animation.FuncAnimation(fig, update, frames=100, interval=25, blit=True)  # html = Mengurangi interval
  html = ani.to_jshtml()
  plt.show()

  return html












