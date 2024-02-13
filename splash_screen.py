import tkinter as tk
from PIL import Image, ImageTk

def close_window():
    root.destroy()

root = tk.Tk()

# Make the window fullscreen
root.attributes("-fullscreen", True)

# Load your image (ensure the path is correct)
image_path = 'logo.jpg'  # Replace 'logo.jpg' with the actual path to your image
img = Image.open(image_path)

# Get screen width and height for fullscreen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize the photo to match the screen dimensions exactly
# This may distort the image or crop it if maintaining the original aspect ratio is not required
img_resized = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

# Convert the resized image to a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(img_resized)

# Create a label to display the image, filling the entire screen
label = tk.Label(root, image=photo)
label.pack(expand=True, fill=tk.BOTH)

# Wait for 3000 milliseconds (3 seconds) and then close the window
root.after(3000, close_window)

root.mainloop()
