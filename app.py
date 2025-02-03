from flask import Flask, request
from templates.home import home
from templates.transverse_wave_sim import transverse_wave_sim
from templates.transverse_wave_output import transverse_wave_output
from templates.longitudinal_wave_sim import longitudinal_wave_sim
from templates.longitudinal_wave_output import longitudinal_wave_output

app = Flask(__name__)

@app.route("/")
def index():
  return home()

@app.route("/transverse-wave-sim")
def transverse_wave():
  return transverse_wave_sim()

@app.route("/transverse-wave-output")
def transverse_output():
  wave_length_1 = request.args.get("wave_length_1")
  wave_length_2 = request.args.get("wave_length_2")
  frequency_1 = request.args.get("frequency_1")
  frequency_2 = request.args.get("frequency_2")
  amplitude_1 = request.args.get("amplitude_1")
  amplitude_2 = request.args.get("amplitude_2")
  return transverse_wave_output(wave_length_1, wave_length_2, frequency_1, frequency_2, amplitude_1, amplitude_2)

@app.route("/longitudinal-wave-sim")
def longitudinal_wave():
  return longitudinal_wave_sim()

@app.route("/longitudinal-wave-output")
def longitudinal_output():
  wavelength_1 = request.args.get("wavelength_1")
  wavelength_2 = request.args.get("wavelength_2")
  frequency_1 = request.args.get("frequency_1")
  frequency_2 = request.args.get("frequency_2")
  amplitude_1 = request.args.get("amplitude_1")
  amplitude_2 = request.args.get("amplitude_2")
  speed_1 = request.args.get("speed_1")
  speed_2 = request.args.get("speed_2")
  return longitudinal_wave_output(amplitude_1, amplitude_2, frequency_1, frequency_2, wavelength_1, wavelength_2, speed_1, speed_2)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)