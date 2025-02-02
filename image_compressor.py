import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compressor")

        self.label = tk.Label(root, text="Select an image to compress")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=5)

        self.quality_label = tk.Label(root, text="Compression Quality (1-100):")
        self.quality_label.pack(pady=5)

        self.quality_entry = tk.Entry(root)
        self.quality_entry.pack(pady=5)
        self.quality_entry.insert(0, "85")

        self.compress_button = tk.Button(root, text="Compress Image", command=self.compress_image)
        self.compress_button.pack(pady=20)

        self.image_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if self.image_path:
            self.label.config(text=f"Selected: {self.image_path}")

    def compress_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected")
            return

        try:
            quality = int(self.quality_entry.get())
            if not (1 <= quality <= 100):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quality between 1 and 100")
            return

        try:
            img = Image.open(self.image_path)
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp"), ("GIF", "*.gif")])
            if save_path:
                img.save(save_path, quality=quality)
                messagebox.showinfo("Success", f"Image saved to {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to compress image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()
