import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def transverse_wave(amplitude_1, amplitude_2, frequency_1, frequency_2, wavelength_1, wavelength_2):
  fig, ax = plt.subplots()
  x = np.linspace(0, 4 * np.pi, 1000)
  t = np.linspace(0, 10, 1000)

  lambda_1 = float(wavelength_1)
  lambda_2 = float(wavelength_2)
  k_1 = 2 * np.pi / lambda_1
  k_2 = 2 * np.pi / lambda_2
  W_1 = 2 * np.pi * float(frequency_1)
  W_2 = 2 * np.pi * float(frequency_2)
  A_1 = float(amplitude_1)
  A_2 = float(amplitude_2)
  
  y_1 = A_1 * A_1 * np.sin(k_1 * x - W_1 * t) + 4
  y_2 = A_2 * A_1 * np.sin(k_2 * x - W_2 * t) - 4
  y_2 = y_2+2
  line_y_1, = ax.plot(x, y_1, 'b-', linewidth=2, label=f'y1')
  line_y_2, = ax.plot(x, y_2, 'r-', linewidth=2, label=f'y2')
  #ax.set_xlim(0, 4 * np.pi)
  ax.set_xlabel('t')
  ax.set_ylabel('y')
  ax.set_title('Animasi Gelombang Transversal')
  ax.set_xticks(np.arange(0,12,2))
  ax.set_xlim(0,12)
  ax.set_yticks(np.arange(-12,12,2))
  #custom_labels = [-'12','-11','-10','-9','-8','-7','-6','-5','-4','-3','2','1','0','1', '2', '3', '4','5','6','7','8','9','10','11','12']
  #ax.set_yticklabels(custom_labels)
  ax.set_ylim(-12,12)
  ax.set_aspect('equal', adjustable='box')
  ax.legend()
  #plt.tight_layout()
  plt.grid(True, color='k', linestyle='-', linewidth=0.5)
  plt.show()


  # Fungsi update animasi
  def update(frame):
      line_y_1.set_ydata(A_1 * np.sin(k_1 * x - W_1 * (t + frame / 5.0)) + 4) # Mempercepat pergerakan
      line_y_2.set_ydata(A_2 * np.sin(k_2 * x - W_2 * (t + frame / 5.0)) - 4)# Mempercepat pergerakan
      return line_y_1, line_y_2

  # Membuat animasi
  ani = animation.FuncAnimation(fig, update, frames=100, interval=25, blit=True)  # html = Mengurangi interval
  html = ani.to_jshtml()

  return html
