from templates.layout import layout

def home():
  return layout(f"""
                  <div class="flex flex-col items-center justify-center w-full md:w-1/2 min-h-screen md:min-h-fit border-2 border-white rounded-lg">
                    <h1 class="w-full text-center text-3xl font-bold mt-5 mb-6">Gelombang Transversal dan Longitudinal</h1>
                    <div class="w-full flex flex-col justify-center items-center mb-6">
                      <p class="w-full text-justify px-4">
                        Gelombang transversal adalah gelombang yang arah rambatannya tegak lurus terhadap arah getarannya. Contoh umum gelombang transversal adalah gelombang cahaya dan gelombang pada tali yang digoyangkan ke atas dan ke bawah. Puncak dan lembah adalah bagian utama dari gelombang transversal, di mana puncak merupakan titik tertinggi dan lembah merupakan titik terendah. Gelombang ini dapat merambat melalui medium padat, tetapi tidak bisa merambat dalam zat cair atau gas karena gaya pemulihnya tidak cukup kuat. Salah satu sifat penting gelombang transversal adalah polarisasi, yang membedakannya dari gelombang longitudinal.
                      </p>
                      <p class="w-full text-justify px-4">
                        <a href="/transverse-wave-sim" class="text-slate-800 bg-white font-bold">KLIK DISINI UNTUK MENUJU SIMULATOR GELOMBANG TRANSVERSAL</a>
                      </p>
                    </div>
                    <div class="w-full flex flex-col justify-center items-center mb-6">
                      <p class="w-full text-justify px-4">
                        Gelombang longitudinal adalah gelombang yang arah rambatannya sejajar dengan arah getarannya. Contoh umum gelombang longitudinal adalah gelombang suara yang merambat melalui udara dalam bentuk rapatan dan regangan partikel. Rapatan adalah daerah dengan partikel yang berkumpul rapat, sedangkan regangan adalah daerah dengan partikel yang menyebar renggang. Gelombang ini dapat merambat melalui zat padat, cair, dan gas karena bergantung pada elastisitas medium. Berbeda dengan gelombang transversal, gelombang longitudinal tidak dapat mengalami polarisasi.  
                      </p>
                      <p class="w-full text-justify px-4">
                        <a href="/longitudinal-wave-sim" class="text-slate-800 bg-white font-bold">KLIK DISINI UNTUK MENUJU SIMULATOR GELOMBANG LONGITUDINAL</a>
                      </p>
                    </div>
                  </div>
                """)