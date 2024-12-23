from tkinter import *
from tkinter import messagebox  # Kullanıcıya mesaj göstermek için
import os  # Dosya işlemleri için

FONT = ('Verdana',20,'normal')
my_window = Tk()
my_window.title('Secret Notes')
my_window.config(padx=30, pady=30)

#UI
my_foto = PhotoImage(file="secretNotes.png")

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


# Dosyayı kaydetme fonksiyonu
def save_and_encrypt():
    title = title_entry.get().strip()
    secret = input_text.get("1.0", END).strip()
    master_key = master_secret_input.get().strip()

    if not title or not secret or not master_key:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
        return

    # Dosya ismi oluşturma
    file_name = f"{title.replace(' ', '_')}.txt"
    file_path = os.path.join(os.getcwd(), file_name)

    try:
        # Dosyayı kaydet
        with open(file_path, "w") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Secret: {secret}\n")
            file.write(f"Master Key: {master_key}\n")

        messagebox.showinfo("Başarılı", f"Notlar başarıyla kaydedildi: {file_name}")
        # Alanları temizle
        title_entry.delete(0, END)
        input_text.delete("1.0", END)
        master_secret_input.delete(0, END)

    except Exception as e:
        messagebox.showerror("Hata", f"Dosya kaydedilirken bir hata oluştu: {e}")


# Şifre Çözme Fonksiyonu (örnek)
def decrypt():
    messagebox.showinfo("Bilgi", "Şifre çözme işlemi henüz entegre edilmedi!")

# Kaydet ve Şifrele Butonu
save_button = Button(text='Save & Encrypt',command=save_and_encrypt(),font=('Verdana',14))
save_button.pack(pady=5)

# Şifre Çöz Butonu
decrypt_button = Button(text='Decrypt',command=decrypt(),font=('Verdana',14))
decrypt_button.pack(pady=5)

my_window.mainloop()