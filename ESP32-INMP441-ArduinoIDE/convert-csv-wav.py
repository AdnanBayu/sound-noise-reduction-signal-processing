import csv
import wave
import numpy as np
import struct

CSV_FILE = r"C:\Users\ASUS\Documents\GitHub\sound-noise-reduction-signal-processing\ESP32-Mic-Input-ArduinoIDE\sound_samples.csv"
WAV_FILE = r"C:\Users\ASUS\Documents\GitHub\sound-noise-reduction-signal-processing\ESP32-Mic-Input-ArduinoIDE\sound_sample.wav"

def csv_to_wav():
    # Read the audio samples from the CSV file
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        # Skip header row
        next(reader)
        
        # Collect audio samples as integers
        samples = []
        for row in reader:
            if row:
                samples.append(int(row[0]))  # Convert to int if needed

    # Convert to numpy array (16-bit integer format)
    samples = np.array(samples, dtype=np.int16)

    # Open a new wave file for writing
    with wave.open(WAV_FILE, 'w') as wav_file:
        # Set parameters: 1 channel, 2 bytes per sample (16-bit), sample rate (adjust as needed)
        sample_rate = 10000  # This should match the sampling rate you used for recording
        wav_file.setparams((1, 2, sample_rate, len(samples), 'NONE', 'not compressed'))

        # Convert samples to binary format
        for sample in samples:
            wav_file.writeframes(struct.pack('h', sample))  # 'h' for 16-bit integer

    print(f"WAV file saved to {WAV_FILE}")

# Convert CSV to WAV
csv_to_wav()
