from templates.layout import layout

def transverse_wave_sim():
  return layout(f"""
                  <div class="flex flex-col items-center justify-center w-full md:w-1/2 min-h-screen md:min-h-fit border-2 border-white rounded-lg p-4">
                    <h1 class="w-full text-center text-3xl font-bold mt-5 mb-10">Simulator Gelombang Transversal</h1>
                    <input type text placeholder="Masukkan Panjang Gelombang 1" id="wave_length_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Panjang Gelombang 2" id="wave_length_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Frekuensi Gelombang 1" id="frequency_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Frekuensi Gelombang 2" id="frequency_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Amplitudo Gelombang 1" id="amplitude_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Amplitudo Gelombang 2" id="amplitude_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <button type="submit" id="submit" class="w-full p-1 text-md text-slate-800 bg-white rounded-lg hover:font-bold cursor-pointer" onclick="handleClick()">Simulasi Gelombang Transversal</button>
                  </div>
                """, """
                const handleClick = () => {
                  const wave_length_1 = document.getElementById("wave_length_1").value;
                  const wave_length_2 = document.getElementById("wave_length_2").value;
                  const frequency_1 = document.getElementById("frequency_1").value;
                  const frequency_2 = document.getElementById("frequency_2").value;
                  const amplitude_1 = document.getElementById("amplitude_1").value;
                  const amplitude_2 = document.getElementById("amplitude_2").value;
                  
                  if (!wave_length_1 || !wave_length_2 || !frequency_1 || !frequency_2 || !amplitude_1 || !amplitude_2) {
                    alert("Semua field harus diisi!");
                    return;
                  }
                  
                  submit.innerText = "Loading...";
                  submit.classList.remove("cursor-pointer");
                  submit.disabled = true;
                  
                  window.location.href = `/transverse-wave-output?wave_length_1=${wave_length_1}&wave_length_2=${wave_length_2}&frequency_1=${frequency_1}&frequency_2=${frequency_2}&amplitude_1=${amplitude_1}&amplitude_2=${amplitude_2}`
                }
                """)