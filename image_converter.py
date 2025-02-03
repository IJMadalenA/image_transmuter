import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        self.label = tk.Label(root, text="Select images to convert")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Images", command=self.select_images)
        self.select_button.pack(pady=5)

        self.format_label = tk.Label(root, text="Select format to convert to:")
        self.format_label.pack(pady=5)

        self.format_var = tk.StringVar(value="JPEG")
        self.format_options = ["JPEG", "PNG", "BMP", "GIF"]
        self.format_menu = tk.OptionMenu(root, self.format_var, *self.format_options)
        self.format_menu.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert Images", command=self.convert_images)
        self.convert_button.pack(pady=20)

        self.image_paths = []

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if self.image_paths:
            self.label.config(text=f"Selected: {len(self.image_paths)} images")

    def convert_images(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected")
            return

        save_format = self.format_var.get()
        for image_path in self.image_paths:
            try:
                img = Image.open(image_path)
                save_path = filedialog.asksaveasfilename(defaultextension=f".{save_format.lower()}", filetypes=[(save_format, f"*.{save_format.lower()}")])
                if save_path:
                    img.save(save_path, format=save_format)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert image {image_path}: {e}")
                return

        messagebox.showinfo("Success", "All images converted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
