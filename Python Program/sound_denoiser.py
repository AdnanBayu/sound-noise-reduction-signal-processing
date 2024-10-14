import numpy as np
import tkinter as tk
from scipy.fftpack import fft, fftfreq, ifft
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
import simpleaudio as sa
import wave
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Denoiser_App:
    def __init__(self, input_sound_path, low_pass: int = 0, high_pass: int = 10000):
        self.input_sound_path = input_sound_path
        self.x, self.sr = librosa.load(self.input_sound_path)
        self.low_pass = low_pass
        self.high_pass = high_pass

    def sound_card(self):
        # Print sound data details
        data_info = (f'x data type: {type(self.x)}\n'
                     f'sr (sampling rate) data type: {type(self.sr)}\n'
                     f'x length: {len(self.x)} integers\n'
                     f'sr (sampling rate): {self.sr} Hz\n'
                     f'The sample sound clip is {len(self.x)/self.sr:.2f} seconds long')
        return data_info

    def filter_noise(self):
        # Compute the spectrum and filter the sound
        self.spectrum = fft(self.x)
        self.N = len(self.x)
        self.F = fftfreq(self.N, 1 / self.sr)
        self.Fpositive = np.where(self.F >= 0)
        bandpass_filter = (np.abs(self.F) >= self.low_pass) & (np.abs(self.F) <= self.high_pass)
        spectrum_filter = self.spectrum * bandpass_filter
        self.signal_filter = ifft(spectrum_filter)
        self.spectrum_output = fft(self.signal_filter)

    def display_data(self, root):
        # Display data visualization in a new Tkinter window
        fig = plt.figure(figsize=(10, 4))
        gs = fig.add_gridspec(2, 2)

        t = np.array(range(0, len(self.x))) / self.sr
        ax1 = fig.add_subplot(gs[:, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax3 = fig.add_subplot(gs[1, 1])

        ax1.plot(t, self.x)
        ax1.plot(t, self.signal_filter.real, color='r')

        ax1.set_xlabel('Time (sec)', fontsize=10)
        ax1.set_ylabel('Signal', fontsize=10)

        ax2.plot(self.F[self.Fpositive], np.absolute(self.spectrum[self.Fpositive]) / self.N)
        ax2.grid()

        ax2.set_xlabel('Frequency (Hz)', fontsize=10)
        ax2.set_ylabel('Spectrum', fontsize=10)

        ax3.plot(self.F[self.Fpositive], np.absolute(self.spectrum_output[self.Fpositive]) / self.N, color='r')
        ax3.grid()

        ax3.set_xlabel('Frequency (Hz)', fontsize=10)
        ax3.set_ylabel('Spectrum', fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()


    def display_output_sound(self, output_path="filtered_sound.wav"):
        # Save and play the filtered sound
        sf.write(output_path, self.signal_filter.real, self.sr)
        wave_obj = wave.open(output_path, 'rb')
        play_obj = sa.WaveObject.from_wave_read(wave_obj).play()
        play_obj.wait_done()

# sound_source = "Sample-Sound-Sambutan-Jokowi-Aksi-212.wav"
# run = Denoiser_App(sound_source, 1000, 3000)