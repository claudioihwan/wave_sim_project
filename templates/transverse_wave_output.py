from templates.layout import layout 
from waves.transverse_wave import transverse_wave

def transverse_wave_output(wave_length_1, wave_length_2, frequency_1, frequency_2, amplitude_1, amplitude_2):
  return layout(f"""
                  <div class="flex flex-col items-center justify-center w-full md:w-1/2 min-h-screen md:min-h-fit border-2 border-white rounded-lg p-4">
                    <h1 class="w-full text-center text-3xl font-bold mt-5 mb-10">Simulator Gelombang Transversal</h1>
                    <div class="w-full flex flex-col justify-center items-center mb-6 bg-white text-slate-800">
                      {transverse_wave(amplitude_1, amplitude_2, frequency_1, frequency_2, wave_length_1, wave_length_2)}
                    </div>
                  </div>
                """)