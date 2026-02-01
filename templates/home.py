from templates.layout import layout

def home():
  return layout(f"""
  <div class="flex flex-col items-center justify-center w-full min-h-screen px-4">
    
    <h1 class="text-3xl font-bold mb-8 text-center">
      Gelombang Transversal dan Longitudinal
    </h1>

    <!-- WRAPPER DUA KOTAK -->
    <div class="flex flex-col md:flex-row gap-8 w-full md:w-3/4">

      <!-- KOTAK GELOMBANG TRANSVERSAL -->
      <div class="flex flex-col items-center border-2 border-white rounded-lg p-6 w-full">
        <h2 class="text-2xl font-semibold mb-4 text-center">
          Gelombang Transversal
        </h2>

        <img 
          src="https://github.com/claudioihwan/wave_sim_project/blob/main/images/longitudinal_wave.gif" 
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
          src="https://www.flippingphysics.com/uploads/2/1/1/0/21103672/0319-animated-gif-1_6.gif" 
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


