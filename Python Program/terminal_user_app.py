from sound_denoiser import Denoiser_App

print("\n------SIGNAL PROCESSING SOUND NOISE REDUCTION------\n")
print("Follow the Steps")

print("1. Input Sound, Low Pass Freq, High Pass Freq")
sound_source = input("input string path to your wav file....")
high_freq = input("input integer high pass frequency threshold....")
low_freq = input("input integer low pass frequency threshold....")
run = Denoiser_App(sound_source, low_freq, high_freq)

print("2. Input Sound Data Card")
run.sound_card()

print("3. Display Input Sound")
# run.display_input_sound()

print("4. Compute Input Sound Spectrum")
run.compute_spectrum()

print("5. Filter Sound Noise")
run.filter_noise()

print("6. Display Filtered Sound")
# run.display_output_sound

print("7. Compute Filtered Sound Spectrum")
run.display_data()