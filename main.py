import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw


def file_open():
    if entry.get() != "":
        entry.delete(1, tk.END)
    file_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpg;*.jpeg"), ("PNG Files", "*.png")])
    entry.insert(tk.END, file_path)


def watermark(file_path, text):
    # Load the image
    image = Image.open(file_path)
    # Make it compatible with Tkinter
    image_tk = ImageTk.PhotoImage(image)
    draw = ImageDraw.Draw(image)
    w, h = image.size
    x, y = int(w/2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype("arial.ttf", int(font_size / 6))
    draw.text((x, y), text, font=font, fill=(225, 225, 225, 100))
    return image


def show():
    file_path = entry.get()
    text2 = text.get()
    new_window = tk.Toplevel()
    new_window.title("Image viewer")
    image = watermark(file_path, text2)
    w, h = image.size
    new_window.geometry(f'{w}x{h}')
    photo = ImageTk.PhotoImage(image)

    # Create a label widget to display the image
    label = tk.Label(new_window, image=photo)
    label.image = photo  # Keep a reference to the photo to avoid garbage collection
    label.pack()


window = tk.Tk()
window.title("Watermark")
window.geometry("300x150")
upload_label = tk.Label(window, text="Choose file:")
upload_label.pack()
entry = tk.Entry()
entry.pack()
upload_btn = tk.Button(window, text="Browse", command=file_open)
upload_btn.pack()
text_label = tk.Label(window, text="Add you watermark text:")
text_label.pack()
text = tk.Entry()
text.pack()
upload_btn = tk.Button(window, text="Add Watermark", command=show)
upload_btn.pack()
window.mainloop()
