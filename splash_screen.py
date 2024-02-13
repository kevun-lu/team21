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

# Since the window is now fullscreen, you might want to resize the image based on the screen's resolution.
# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize the photo to fit the screen while maintaining aspect ratio
aspect_ratio = min(screen_width / img.width, screen_height / img.height)
new_width = int(img.width * aspect_ratio)
new_height = int(img.height * aspect_ratio)

# Use Image.Resampling.LANCZOS for high-quality downsampling
img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Convert the resized image to a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(img_resized)

# Create a label to display the image, centered
label = tk.Label(root, image=photo)
label.pack(expand=True)

# Wait for 3000 milliseconds (3 seconds) and then close the window
root.after(3000, close_window)

root.mainloop()
