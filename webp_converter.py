
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_to_webp(input_folder, output_folder, quality):
    try:
        # Iterate through every file in the 'input' folder and its subfolders
        for folderpath, _, filenames in os.walk(input_folder):
            # Create corresponding subfolder structure in 'output' folder
            relative_path = os.path.relpath(folderpath, input_folder)
            output_subfolder = os.path.join(output_folder, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)

            for filename in filenames:
                input_image_path = os.path.join(folderpath, filename)
                output_image_path = os.path.join(output_subfolder, f'{os.path.splitext(filename)[0]}.webp')

                # Open the image file
                with Image.open(input_image_path) as img:
                    # Convert the image to WebP format
                    img.save(output_image_path, 'WEBP', quality=quality)

                print(f"Conversion successful. Image saved at {output_image_path}")
    except Exception as e:
        print(f"Error: {e}")
        
def choose_input_path():
    folder_path = filedialog.askdirectory()
    input_path_entry.delete(0, tk.END)
    input_path_entry.insert(0, folder_path)

def choose_output_path():
    folder_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, folder_path)

def create_folders_and_update_paths():
    # Create 'input' and 'output' folders in the same directory as the script
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_folder = os.path.join(script_directory, 'input')
    output_folder = os.path.join(script_directory, 'output')
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    input_path_entry.delete(0, tk.END)
    input_path_entry.insert(0, input_folder)

    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_folder)

def convert_button_clicked():
    input_folder = input_path_entry.get()
    output_folder = output_path_entry.get()
    quality_value = quality_var.get()
    
    if input_folder and output_folder:
        convert_to_webp(input_folder, output_folder, quality_value)
    else:
        result_label.config(text="Please provide both input and output paths.")

# Create the main window
root = tk.Tk()
root.title("WEBP Converter")

# Input Path
input_label = tk.Label(root, text="Input Path:")
input_label.grid(row=0, column=0, padx=10, pady=5)
input_path_entry = tk.Entry(root, width=40)
input_path_entry.grid(row=0, column=1, padx=10, pady=5)
input_button = tk.Button(root, text="Browse", command=choose_input_path)
input_button.grid(row=0, column=2, padx=10, pady=5)

# Output Path
output_label = tk.Label(root, text="Output Path:")
output_label.grid(row=1, column=0, padx=10, pady=5)
output_path_entry = tk.Entry(root, width=40)
output_path_entry.grid(row=1, column=1, padx=10, pady=5)
output_button = tk.Button(root, text="Browse", command=choose_output_path)
output_button.grid(row=1, column=2, padx=10, pady=5)

# Quality
quality_label = tk.Label(root, text="Quality (1-100):")
quality_label.grid(row=2, column=0, padx=10, pady=5)
quality_var = tk.IntVar(value=80)
quality_entry = tk.Entry(root, textvariable=quality_var, width=5)
quality_entry.grid(row=2, column=1, padx=10, pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_button_clicked)
convert_button.grid(row=3, column=1, pady=10)

# Create Folders and Update Paths Button
create_folders_button = tk.Button(root, text="Create Folders and Update Paths", command=create_folders_and_update_paths)
create_folders_button.grid(row=4, column=1, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1, pady=5)

# Start the main loop
root.mainloop()
