import numpy as np
from numpy import sin, cos, pi
from scipy.fftpack import fft, fftfreq, ifft
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
import simpleaudio as sa
import wave

class Denoiser_App:
    def __init__(self, input_sound_path, low_pass: int = 0, high_pass: int =10000):
        self.input_sound_path = input_sound_path
        self.x, self.sr = librosa.load(self.input_sound_path)
        self.low_pass = low_pass
        self.high_pass = high_pass

    def sound_card(self):
        print("\n------SOUND DATA CARD------\n")
        print(f'x data type is {type(self.x)}')
        print(f'sr (sampling rate) data type is {type(self.sr)}')
        print(f'x length: {len(self.x)} integers')
        print(f'sr (sampling rate) of the sound is : {self.sr} Hz')
        print(f'The sample sound clip is {len(self.x)/self.sr:.2f} seconds long')
        print("\n---------------------------\n")

    def display_input_sound(self, output_path="filtered_sound.wav"):
        sf.write(output_path, self.x, self.sr)
        wave_obj = wave.open(output_path, 'rb')
        play_obj = sa.WaveObject.from_wave_read(wave_obj).play()
        print("Playing input sound with simpleaudio...")

        play_obj.wait_done()


    def compute_spectrum(self):
        self.spectrum=fft(self.x)
        self.N = len(self.x)
        self.F=fftfreq(self.N,1/self.sr)
        self.Fpositive=np.where(self.F>=0)

    def filter_noise(self):
        high_threshold=self.high_pass
        low_threshold=self.low_pass
        bandpass_filter= (np.absolute(self.F) >= low_threshold) & (np.absolute(self.F) <= high_threshold)
        spectrum_filter = self.spectrum*bandpass_filter
        self.signal_filter=ifft(spectrum_filter)
        self.spectrum_output=fft(self.signal_filter)

    def display_output_sound(self, output_path="filtered_sound.wav"):
        sf.write(output_path, self.signal_filter.real, self.sr)
        wave_obj = wave.open(output_path, 'rb')
        play_obj = sa.WaveObject.from_wave_read(wave_obj).play()
        print("Playing filtered sound with simpleaudio...")

        play_obj.wait_done()

    def display_data(self):
        fig=plt.figure(figsize=(20,4))
        gs=fig.add_gridspec(2,2)
        
        t = np.array(range(0, len(self.x))) / self.sr
        ax1=fig.add_subplot(gs[:,0])
        ax2=fig.add_subplot(gs[0,1])
        ax3=fig.add_subplot(gs[1,1])


        ax1.plot(t,self.x,label='Input')
        ax1.plot(t,self.signal_filter.real,color='r',label='output')
        ax1.legend(fontsize=14)
        ax1.set_xlabel('Time(sec)',fontsize=14)
        ax1.set_ylabel('Signal',fontsize=14)

        ax2.plot(self.F[self.Fpositive],np.absolute(self.spectrum[self.Fpositive])/self.N,label='Input')
        ax2.grid()
        ax1.legend(fontsize=14)
        ax2.set_xlabel('Time(sec)',fontsize=14)
        ax2.set_ylabel('Spectrum',fontsize=14)


        ax3.plot(self.F[self.Fpositive],np.absolute(self.spectrum_output[self.Fpositive])/self.N,color='r',label='Output')
        ax3.grid()
        ax1.legend(fontsize=14)
        ax3.set_xlabel('Time(sec)',fontsize=14)
        ax3.set_ylabel('Spectrum',fontsize=14)

# sound_source = "Sample-Sound-Sambutan-Jokowi-Aksi-212.wav"
# run = Denoiser_App(sound_source, 1000, 3000)