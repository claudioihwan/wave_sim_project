from templates.layout import layout

def longitudinal_wave_sim():
  return layout(f"""
                  <div class="flex flex-col items-center justify-center w-full md:w-1/2 min-h-screen md:min-h-fit border-2 border-white rounded-lg p-4">
                    <h1 class="w-full text-center text-3xl font-bold mt-5 mb-10">Simulator Gelombang Longitudinal</h1>
                    <input type text placeholder="Masukkan Panjang Gelombang 1" id="wavelength_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Panjang Gelombang 2" id="wavelength_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">

                    <input type text placeholder="Masukkan Kelajuan Gelombang 1" id="speed_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Kelajuan Gelombang 2" id="speed_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">

                    <input type text placeholder="Masukkan Amplitudo Gelombang 1" id="amplitude_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Amplitudo Gelombang 2" id="amplitude_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">

                    <input type text placeholder="Masukkan Frekuensi Gelombang 1" id="frequency_1" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    <input type text placeholder="Masukkan Frekuensi Gelombang 2" id="frequency_2" class="w-full p-2 outline-none border-1 border-white rounded-lg mb-4 text-sm">
                    
                    <button type="submit" id="submit" class="w-full p-1 text-md text-slate-800 bg-white rounded-lg hover:font-bold cursor-pointer" onclick="handleClick()">Simulasi Gelombang Longitudinal</button>
                  </div>
                """, """
                const handleClick = () => {
                  const wavelength_1 = document.getElementById("wavelength_1").value;
                  const frequency_1 = document.getElementById("frequency_1").value;
                  const amplitude_1 = document.getElementById("amplitude_1").value;
                  const speed_1 = document.getElementById("speed_1").value;
                  const wavelength_2 = document.getElementById("wavelength_2").value;
                  const frequency_2 = document.getElementById("frequency_2").value;
                  const amplitude_2 = document.getElementById("amplitude_2").value;
                  const speed_2 = document.getElementById("speed_2").value;
                  const submit = document.getElementById("submit");
                  
                  if (!wavelength_1 || !frequency_1 || !amplitude_1 || !speed_1 || !wavelength_2 || !frequency_2 || !amplitude_2 || !speed_2) {
                    alert("Semua field harus diisi!");
                    return;
                  }
                  
                  submit.innerText = "Loading...";
                  submit.classList.remove("cursor-pointer");
                  submit.disabled = true;
                  
                  window.location.href = `/longitudinal-wave-output?wavelength_1=${wavelength_1}&frequency_1=${frequency_1}&amplitude_1=${amplitude_1}&speed_1=${speed_1}&wavelength_2=${wavelength_2}&frequency_2=${frequency_2}&amplitude_2=${amplitude_2}&speed_2=${speed_2}`;
                }
                """)