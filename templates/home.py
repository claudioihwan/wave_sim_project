from templates.layout import layout

def home():
  return layout(f"""
  <div class="flex flex-col items-center justify-center w-full min-h-screen px-4">
    
    <div class="mb-8 flex justify-center">
      <img
        src="https://raw.githubusercontent.com/claudioihwan/wave_sim_project/refs/heads/main/images/logo_simulator-Photoroom.png"
        alt="Logo Simulator Interaktif Gelombang"
        class="h-24 md:h-30"
       > 
    </div>

    <!-- WRAPPER DUA KOTAK -->
    <div class="flex flex-col md:flex-row gap-8 w-full md:w-3/4">

      <!-- KOTAK GELOMBANG TRANSVERSAL -->
      <div class="flex flex-col items-center border-2 border-white rounded-lg p-6 w-full">
        <h2 class="text-2xl font-semibold mb-4 text-center">
          Gelombang Transversal
        </h2>

        <img 
          src="https://raw.githubusercontent.com/claudioihwan/wave_sim_project/refs/heads/main/images/transverse_wave.gif" 
          alt="Gelombang Transversal"
          class="mb-4"
          width="300"
        >

        <p class="text-justify mb-4">
          Gelombang transversal adalah gelombang yang arah rambatannya tegak lurus
          terhadap arah getarannya. Contohnya adalah gelombang cahaya dan gelombang
          pada tali. Gelombang ini memiliki puncak dan lembah serta dapat mengalami
          polarisasi.
        </p>

        <a 
          href="/transverse-wave-sim"
          class="mt-auto text-slate-800 bg-white font-bold px-4 py-2 rounded hover:bg-slate-200 transition"
        >
          Mulai Simulasi Transversal
        </a>
      </div>

      <!-- KOTAK GELOMBANG LONGITUDINAL -->
      <div class="flex flex-col items-center border-2 border-white rounded-lg p-6 w-full">
        <h2 class="text-2xl font-semibold mb-4 text-center">
          Gelombang Longitudinal
        </h2>

        <img 
          src="https://raw.githubusercontent.com/claudioihwan/wave_sim_project/refs/heads/main/images/longitudinal_wave.gif" 
          alt="Gelombang Longitudinal"
          class="mb-4"
          width="300"
        >

        <p class="text-justify mb-4">
          Gelombang longitudinal adalah gelombang yang arah rambatannya sejajar
          dengan arah getarannya. Contohnya adalah gelombang bunyi yang merambat
          melalui rapatan dan regangan partikel, serta tidak dapat mengalami
          polarisasi.
        </p>

        <a 
          href="/longitudinal-wave-sim"
          class="mt-auto text-slate-800 bg-white font-bold px-4 py-2 rounded hover:bg-slate-200 transition"
        >
          Mulai Simulasi Longitudinal
        </a>
      </div>

    </div>
  </div>
  """)








