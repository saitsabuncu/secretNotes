from tkinter import *

FONT = ('Verdana',20,'normal')
my_window = Tk()
my_window.title('Secret Notes')
my_window.config(padx=30, pady=30)

#UI
my_foto = PhotoImage(file="secretNotes.png")
#photo_label = Label(image=my_foto)
#photo_label.pack()

canvas = Canvas(height=200, width=200)  # Görsel boyutuna göre ayarla
canvas.create_image(100, 100, image=my_foto)  # Koordinatları ortala
canvas.pack()

title_info_label = Label(text='Enter your title',font=FONT)
title_info_label.pack()
title_entry = Entry(width=30)
title_entry.pack()

input_info_label = Label(text='Enter your secret',font=FONT)
input_info_label.pack()
input_text = Text(width=50, height=25)
input_text.pack()

master_secret_label = Label(text='Enter master key',font=FONT)
master_secret_label.pack()
master_secret_input = Entry(width=30)
master_secret_input.pack()

save_button = Button(text='Save & Encrypt')
save_button.pack()
decrypt_button = Button(text='Decrypt')
decrypt_button.pack()



my_window.mainloop()