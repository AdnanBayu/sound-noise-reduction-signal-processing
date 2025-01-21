# Sound Noise Reduction Signal Processing
![Audio_Signal_Processing(Noise_Filter)](https://github.com/user-attachments/assets/852462b5-037e-48f0-a9f0-c78cb375a066) <br/>
![GitHub last commit](https://img.shields.io/github/last-commit/AdnanBayu/sound-noise-reduction-signal-processing) ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AdnanBayu/sound-noise-reduction-signal-processing) <br/>
Processing audio signal captured from INMP441 sensor to ESP32. This project created for Advanced Signal Processing college subject final project.

## Project activity
Several activity conducted on this project to analyzed signal and conduct filtering
- Capture dataset of cafe noise using laptop internal microphone
- Capture ambience noise using INMP441 mic module to ESP32
- Analyzed signal in frequency domain using FFT (Fast Fourier Transform)
- Filtered non continous signal using STFT and Low pass filter
- Filtered continous signal using butterworth filter coefficient

## Dependencies
for python program
```bash
numpy
scipy
librosa
matplotlib
soundfile
pandas
math
sounddevice
IPython
```

for arduino program
```bash
#include <driver/i2s.h>
```

## System block diagram
![Noise Reduction Mic drawio](https://github.com/user-attachments/assets/797271f0-5fc0-4daa-89e4-b3c7f174b5db)

## Directory explanation
- Butterworth-Offline-Sound : test butterworth filter coefficient to offline audio and save as WAV
- Butterworth-Complete/Design-Filter : design butterworth filter on audio signal, and applied it to realtime signal captured on ESP32 by INMP441
- Butterworth-Coefficient-on-ESP32 : apply butterworth filter coefficient to offline (non realtime) audio signal
- Filter-Coeff-Noise-Only : apply butterworth filter coefficient to noise only, to prove it could remove all the noise
- Filter-Coefficient-Generated-Sinusoid-Signals : apply butterworth filter coefficient to generated and controlled sinusoid signal
- Low Pass FFT and STFT Voice Processing : conduct regular low pass filter to signal after analyzed it using FFT and STFT
- Proof ESP32 Sucks for Sound : proving that ESP32 performs bad on capturing audio signal
- Read-INMP441-ESP32-ArduinoIDE : read audio from INMP441 to ESP32

## Non technical documentation
There are several pdf file for progress report (mid exam and final exam).
- [Paper] Sound Signal Noise Reduction Using STFT.pdf
- [Paper] Real-Time Noise Reduction on an ESP32-Based INMP441 Microphone System Using IIR Filtering.pdf
