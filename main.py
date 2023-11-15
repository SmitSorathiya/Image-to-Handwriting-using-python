import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pytesseract
import random

class ImageToHandwritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Handwriting Converter")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Set background color

        # Create a frame for the top section
        self.top_frame = tk.Frame(root, bg="#2c3e50")  # Set frame background color
        self.top_frame.pack(fill="both", padx=10, pady=10)

        # Create a label for displaying the image
        self.image_label = tk.Label(self.top_frame, bg="white", padx=10, pady=10)
        self.image_label.grid(row=0, column=0, columnspan=2)

        # Create a button to open an image file
        self.open_button = ttk.Button(self.top_frame, text="Open Image", command=self.open_image)
        self.open_button.grid(row=1, column=0, padx=10, pady=5)

        # Create a button to convert the image to handwriting style
        self.convert_button = ttk.Button(self.top_frame, text="Convert to Handwriting", command=self.convert_to_handwriting)
        self.convert_button.grid(row=1, column=1, padx=10, pady=5)

        # Create a frame for the text widget
        self.bottom_frame = tk.Frame(root, bg="#2c3e50")
        self.bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create a text widget to display the converted text
        self.text_widget = tk.Text(self.bottom_frame, wrap=tk.WORD, font=("Courier", 12))
        self.text_widget.pack(fill="both", expand=True)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if hasattr(self, 'image'):
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.tk_image)
            self.image_label.image = self.tk_image

    def convert_to_handwriting(self):
        if hasattr(self, 'image'):
            # Specify the Tesseract executable path
            pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'

            # Extract text from the image using Tesseract OCR
            text = pytesseract.image_to_string(self.image)

            # Simulate handwriting-like text on a white background
            handwriting_image = self.simulate_handwriting(text)

            # Display the handwriting-like text
            self.display_handwriting_image(handwriting_image)

    def simulate_handwriting(self, text):
        # Create an image with white background
        image = Image.new("RGB", (800, 600), "white")
        draw = ImageDraw.Draw(image)

        # Load a handwriting-style font (you'll need to have a TTF font file)
        handwriting_font = ImageFont.truetype(r"C:\Users\admin\Desktop\handwriting_3\Handwriting.ttf", 20)

        # Split text into lines
        lines = text.split("\n")

        # Position variables
        x, y = 10, 10

        for line in lines:
            # Simulate handwriting variation in x, y position
            x += random.randint(5, 10)
            y += random.randint(5, 10)

            # Draw the text on the image using the handwriting font
            draw.text((x, y), line, fill="black", font=handwriting_font)

            # Adjust the y-position for the next line
            y += 30

        return image

    def display_handwriting_image(self, handwriting_image):
        # Convert the PIL Image to a PhotoImage
        handwriting_photo = ImageTk.PhotoImage(handwriting_image)

        # Display the handwriting-like text image
        self.image_label.config(image=handwriting_photo)
        self.image_label.image = handwriting_photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToHandwritingApp(root)
    root.mainloop()
