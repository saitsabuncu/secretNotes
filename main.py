from tkinter import *
from tkinter import messagebox  # Kullanıcıya mesaj göstermek için
import base64

# Şifreleme fonksiyonu
def encode(key, clear):
    """
    Verilen bir anahtar (key) ve düz metni (clear), şifreli bir metne dönüştürür.

    Args:
        key (str): Şifreleme için kullanılan anahtar.
        clear (str): Şifrelenecek düz metin.

    Returns:
        str: Base64 formatında şifrelenmiş metin.
    """
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Şifre çözme fonksiyonu
def decode(key, enc):
    """
    Verilen bir anahtar (key) ve şifrelenmiş metni (enc), düz metne çözer.

    Args:
        key (str): Şifre çözme için kullanılan anahtar.
        enc (str): Şifrelenmiş metin (Base64 formatında).

    Returns:
        str: Çözülen düz metin.
    """
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

# Dosyayı kaydetme ve şifreleme fonksiyonu
def save_and_encrypt():
    """
    Kullanıcıdan alınan başlık, gizli not ve anahtar bilgilerini kullanarak notu şifreler
    ve bir dosyaya kaydeder.

    Dosya adı, kullanıcı tarafından girilen başlığa göre oluşturulur. Şifreleme işlemi
    için `encode` fonksiyonu kullanılır.

    Raises:
        messagebox.showerror: Gerekli alanlar boş bırakıldığında veya işlem sırasında hata oluştuğunda hata mesajı gösterir.
    """
    my_title = title_entry.get().strip()
    message = input_text.get("1.0", END).strip()
    master_key = master_secret_input.get().strip()

    # Alan kontrolü
    if not my_title or not message or not master_key:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
        return

    try:
        # Mesajı şifreleme
        encrypted_message = encode(master_key, message)

        # Dosya kaydetme
        file_name = f"{my_title.replace(' ', '_')}.txt"
        with open(file_name, "w") as file:
            file.write(encrypted_message)

        messagebox.showinfo("Başarılı", f"Gizli not başarıyla kaydedildi: {file_name}")
        # Giriş alanlarını temizle
        title_entry.delete(0, END)
        input_text.delete("1.0", END)
        master_secret_input.delete(0, END)

    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Şifre çözme fonksiyonu
def decrypt():
    """
    Kullanıcıdan alınan dosya adı ve anahtar bilgilerini kullanarak, şifrelenmiş bir dosyadaki
    içeriği çözer ve kullanıcıya gösterir.

    Dosya okuma işlemi sırasında dosya bulunamazsa veya şifre çözme işlemi başarısız olursa hata mesajı gösterir.

    Raises:
        messagebox.showerror: Gerekli alanlar boş bırakıldığında veya işlem sırasında hata oluştuğunda hata mesajı gösterir.
    """
    file_path = title_entry.get().strip()
    master_key = master_secret_input.get().strip()

    if not file_path or not master_key:
        messagebox.showerror("Hata", "Dosya adını ve anahtarınızı girin!")
        return

    try:
        # Dosyayı okuma
        with open(file_path, "r") as file:
            encrypted_message = file.read()

        # Şifre çözme
        decrypted_message = decode(master_key, encrypted_message)
        input_text.delete("1.0", END)
        input_text.insert("1.0", decrypted_message)
        messagebox.showinfo("Başarılı", "Şifre çözme işlemi tamamlandı!")

    except FileNotFoundError:
        messagebox.showerror("Hata", "Dosya bulunamadı!")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# UI Ayarları
FONT = ('Verdana', 15, 'normal')
my_window = Tk()
my_window.title('Secret Notes')

my_window.config(padx=30, pady=30)

my_foto = PhotoImage(file="secretNotes.png")

canvas = Canvas(height=200, width=200)  # Görsel boyutuna göre ayarla
canvas.create_image(100, 100, image=my_foto)  # Koordinatları ortala
canvas.pack()

title_info_label = Label(text='Enter your title or file name', font=FONT)
title_info_label.pack()
title_entry = Entry(width=30)
title_entry.pack()

input_info_label = Label(text='Enter your secret', font=FONT)
input_info_label.pack()
input_text = Text(width=50, height=20)
input_text.pack()

master_secret_label = Label(text='Enter master key', font=FONT)
master_secret_label.pack()
master_secret_input = Entry(width=30, show="*")
master_secret_input.pack()

# Kaydet ve Şifrele Butonu
save_button = Button(text='Save & Encrypt', command=save_and_encrypt, font=('Verdana', 14))
save_button.pack(pady=5)

# Şifre Çöz Butonu
decrypt_button = Button(text='Decrypt', command=decrypt, font=('Verdana', 14))
decrypt_button.pack(pady=5)

my_window.mainloop()