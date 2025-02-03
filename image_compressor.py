import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image
import os

class ImageCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compressor")

        self.label = tk.Label(root, text="Select images to compress")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Images", command=self.select_images)
        self.select_button.pack(pady=5)

        self.quality_label = tk.Label(root, text="Compression Quality (1-100):")
        self.quality_label.pack(pady=5)

        self.quality_entry = tk.Entry(root)
        self.quality_entry.pack(pady=5)
        self.quality_entry.insert(0, "85")

        self.compress_button = tk.Button(root, text="Compress Images", command=self.compress_images)
        self.compress_button.pack(pady=20)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.image_paths = []

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if self.image_paths:
            self.label.config(text=f"Selected: {len(self.image_paths)} images")

    def compress_images(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected")
            return

        try:
            quality = int(self.quality_entry.get())
            if not (1 <= quality <= 100):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quality between 1 and 100")
            return

        output_dir = filedialog.askdirectory()
        if not output_dir:
            messagebox.showerror("Error", "No output directory selected")
            return

        self.progress["maximum"] = len(self.image_paths)
        self.progress["value"] = 0

        for i, image_path in enumerate(self.image_paths):
            try:
                img = Image.open(image_path)
                base_name = os.path.basename(image_path)
                save_path = os.path.join(output_dir, base_name)
                img.save(save_path, quality=quality)
                self.progress["value"] = i + 1
                self.root.update_idletasks()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to compress image {image_path}: {e}")
                return

        messagebox.showinfo("Success", "All images compressed successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()