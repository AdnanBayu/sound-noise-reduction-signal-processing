import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from sound_denoiser import Denoiser_App

class DenoiserAppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sound Denoiser")
        
        # File selection
        self.file_label = tk.Label(root, text="Select a sound file:")
        self.file_label.pack(pady=5)
        
        self.file_path = tk.Entry(root, width=50)
        self.file_path.pack(pady=5)
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)
        
        # Low-pass filter input
        self.low_pass_label = tk.Label(root, text="Low-pass filter (Hz):")
        self.low_pass_label.pack(pady=5)
        
        self.low_pass_input = tk.Entry(root)
        self.low_pass_input.pack(pady=5)
        self.low_pass_input.insert(0, "1000")  # Default value
        
        # High-pass filter input
        self.high_pass_label = tk.Label(root, text="High-pass filter (Hz):")
        self.high_pass_label.pack(pady=5)
        
        self.high_pass_input = tk.Entry(root)
        self.high_pass_input.pack(pady=5)
        self.high_pass_input.insert(0, "3000")  # Default value
        
        # Process button
        self.process_button = tk.Button(root, text="Denoise", command=self.denoise_sound)
        self.process_button.pack(pady=10)

    def browse_file(self):
        # Open file dialog to select sound file
        file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if file:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, file)

    def denoise_sound(self):
        # Get input values
        sound_file = self.file_path.get()
        try:
            low_pass = int(self.low_pass_input.get())
            high_pass = int(self.high_pass_input.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for low-pass and high-pass filter.")
            return
        
        if not sound_file:
            messagebox.showerror("No File Selected", "Please select a sound file.")
            return
        
        try:
            # Run the denoising process
            denoiser = Denoiser_App(sound_file, low_pass, high_pass)
            denoiser.filter_noise()
            self.show_data_visualization(denoiser)
            denoiser.display_output_sound()
            messagebox.showinfo("Success", "Denoising completed and sound played!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_data_visualization(self, denoiser):
        # Create a new window for data visualization
        data_window = Toplevel(self.root)
        data_window.title("Sound Data Visualization")
        
        # Display sound card information
        data_info = denoiser.sound_card()
        info_label = tk.Label(data_window, text=data_info, justify="left")
        info_label.pack(pady=10)
        
        # Display the data visualization
        denoiser.display_data(data_window)

# Main loop
root = tk.Tk()
app = DenoiserAppUI(root)
root.mainloop()
