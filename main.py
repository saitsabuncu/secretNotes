import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Resim işlemleri için

# XOR Şifreleme ve Çözme Fonksiyonları
import base64

def xor_sifrele(mesaj, anahtar):
    sifreli_mesaj = ''.join(chr(ord(c) ^ ord(anahtar[i % len(anahtar)])) for i, c in enumerate(mesaj))
    return base64.b64encode(sifreli_mesaj.encode()).decode()

def xor_coz(sifreli_mesaj, anahtar):
    try:
        mesaj = base64.b64decode(sifreli_mesaj).decode()
        cozulmus_mesaj = ''.join(chr(ord(c) ^ ord(anahtar[i % len(anahtar)])) for i, c in enumerate(mesaj))
        return cozulmus_mesaj
    except Exception as e:
        return f"Hata: {str(e)}"

# Kaydet ve Şifrele Fonksiyonu
def kaydet_ve_sifrele():
    baslik = baslik_girisi.get()
    mesaj = not_girisi.get("1.0", tk.END).strip()
    master_key = anahtar_girisi.get().strip()

    if not baslik or not mesaj or not master_key:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
        return

    sifreli_mesaj = xor_sifrele(mesaj, master_key)
    with open(f"{baslik}.txt", "w", encoding="utf-8") as dosya:
        dosya.write(sifreli_mesaj)

    messagebox.showinfo("Başarılı", f"Not '{baslik}' başarıyla şifrelendi ve kaydedildi!")

# Çözme Fonksiyonu
def coz():
    baslik = baslik_girisi.get()
    master_key = anahtar_girisi.get().strip()

    try:
        with open(f"{baslik}.txt", "r", encoding="utf-8") as dosya:
            sifreli_mesaj = dosya.read()

        cozulmus_mesaj = xor_coz(sifreli_mesaj, master_key)
        not_girisi.delete("1.0", tk.END)
        not_girisi.insert(tk.END, cozulmus_mesaj)
        messagebox.showinfo("Başarılı", f"Not '{baslik}' başarıyla çözüldü!")
    except FileNotFoundError:
        messagebox.showerror("Hata", f"Not '{baslik}' bulunamadı!")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

# Tkinter Arayüz
pencere = tk.Tk()
pencere.title("Şifreli Notlar")
pencere.geometry("400x600")

# Resim ekleme
resim_dosyasi = "secret notes.png"  # Resminizin tam dosya yolunu yazın
resim = Image.open(resim_dosyasi)
resim = resim.resize((100, 100), Image.LANCZOS)  # Yeni Pillow sürümleri için LANCZOS
resim_tk = ImageTk.PhotoImage(resim)

resim_etiketi = tk.Label(pencere, image=resim_tk)
resim_etiketi.pack(pady=10)


# Başlık girişi
ttk.Label(pencere, text="Enter your title").pack(pady=10)
baslik_girisi = ttk.Entry(pencere, width=40)
baslik_girisi.pack(pady=10)

# Not girişi
ttk.Label(pencere, text="Enter your secret").pack(pady=10)
not_girisi = tk.Text(pencere, wrap=tk.WORD, height=10, width=40)
not_girisi.pack(pady=10)

# Anahtar girişi
ttk.Label(pencere, text="Enter master key").pack(pady=10)
anahtar_girisi = ttk.Entry(pencere, show="*", width=40)
anahtar_girisi.pack(pady=10)

# Butonlar
ttk.Button(pencere, text="Save & Encrypt", command=kaydet_ve_sifrele).pack(pady=10)
ttk.Button(pencere, text="Decrypt", command=coz).pack(pady=10)

pencere.mainloop()
