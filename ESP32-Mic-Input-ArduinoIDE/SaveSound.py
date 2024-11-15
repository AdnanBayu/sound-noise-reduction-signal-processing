import serial
import wave

# Configure your serial port and baud rate
ser = serial.Serial("COM3", 115200)  # Replace with your ESP32 port
output_file = 'output.wav'

# Configure WAV file to handle 32-bit audio
with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(1)        # Mono
    wf.setsampwidth(4)        # 32-bit samples
    wf.setframerate(44100)    # 44.1 kHz sample rate

    try:
        while True:
            # Read 2048 bytes (512 samples of 32-bit) from serial
            data = ser.read(2048)
            if len(data) == 2048:
                wf.writeframes(data)
    except KeyboardInterrupt:
        print("Recording stopped.")
    finally:
        ser.close()
