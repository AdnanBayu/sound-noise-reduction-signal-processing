    def sound_card(self):
        print("------SOUND DATA CARD------")
        print(f'x data type is {type(self.x)}')
        print(f'x length: {len(self.x)} integers')
        print(f'sr (sampling rate) data type is {type(self.sr)}')
        print(f'sr (sampling rate) of the sound is : {self.sr} Hz')
        print(f'The sample sound clip is {len(self.x)/self.sr:.2f} seconds long')

    def display_input_sound(self):
        ipd.Audio(self.x, rate=self.sr)

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

    def display_output_sound(self):
        ipd.Audio(self.signal_filter, rate=self.sr)

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