from templates.layout import layout 
from waves.longitudinal_wave import longitudinal_wave

def longitudinal_wave_output(amplitude_1, amplitude_2, frequency_1, frequency_2, wavelength_1, wavelength_2, speed_1, speed_2):
  return layout(f"""
                  <div class="flex flex-col items-center justify-center w-full md:w-1/2 min-h-screen md:min-h-fit border-2 border-white rounded-lg p-4">
                    <h1 class="w-full text-center text-3xl font-bold mt-5 mb-10">Simulator Gelombang Longitudinal</h1>
                    <div class="w-full flex flex-col justify-center items-center mb-6 bg-white text-slate-800">
                      {longitudinal_wave(amplitude_1, amplitude_2, frequency_1, frequency_2, wavelength_1, wavelength_2, speed_1, speed_2)}
                    </div>
                  </div>
                """)