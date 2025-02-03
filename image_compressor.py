import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
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

        self.preview_button = tk.Button(root, text="Preview Images", command=self.preview_images)
        self.preview_button.pack(pady=5)

        self.compress_button = tk.Button(root, text="Compress Images", command=self.compress_images)
        self.compress_button.pack(pady=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_images)
        self.reset_button.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.image_paths = []
        self.preview_window = None

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if self.image_paths:
            self.label.config(text=f"Selected: {len(self.image_paths)} images")

    def preview_images(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected")
            return

        if self.preview_window:
            self.preview_window.destroy()

        self.preview_window = tk.Toplevel(self.root)
        self.preview_window.title("Image Previews")

        for image_path in self.image_paths:
            img = Image.open(image_path)
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            label = tk.Label(self.preview_window, image=img_tk)
            label.image = img_tk
            label.pack()

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

    def reset_images(self):
        self.image_paths = []
        self.label.config(text="Select images to compress")
        if self.preview_window:
            self.preview_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()
