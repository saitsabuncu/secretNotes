# Secret Notes

**Secret Notes**, kullanıcıların gizli notlarını güvenli bir şekilde şifreleyip kaydetmesine olanak tanıyan bir masaüstü uygulamasıdır. Python'un **Tkinter** modülü ile geliştirilmiş, şifreleme ve şifre çözme işlemleri için **Base64** yöntemi kullanılmıştır.

---

## 🛠️ Özellikler

- **Not Şifreleme**: Kullanıcı girdilerini bir anahtar ile şifreler ve dosya olarak kaydeder.
- **Şifre Çözme**: Şifrelenmiş dosyaları doğru anahtarla çözerek görüntüler.
- **Kullanıcı Dostu Arayüz**: Tkinter ile tasarlanmış basit ve işlevsel bir arayüz.
- **Güvenlik**: Şifreleme anahtarı olmadan şifre çözme mümkün değildir.

---

## 🔧 Nasıl Çalışır?

### 1. Not Kaydetme ve Şifreleme
- **Başlık Girin**: Dosya adını oluşturmak için bir başlık girin.
- **Gizli Notunuzu Yazın**: Şifrelemek istediğiniz metni yazın.
- **Anahtar Girin**: Şifreleme için bir anahtar oluşturun.
- **Save & Encrypt** butonuna tıklayın:
  - Notunuz şifrelenir ve `.txt` dosyası olarak kaydedilir.

### 2. Şifre Çözme
- **Dosya Adını Girin**: Şifrelenmiş dosyanızın adını girin.
- **Anahtar Girin**: Şifreyi çözmek için doğru anahtarı girin.
- **Decrypt** butonuna tıklayın:
  - Şifrelenmiş notunuzun çözülmüş hali ekranda görüntülenir.

---

## 🚀 Kurulum ve Çalıştırma

1. **Proje Dosyalarını İndirin**:
   ```bash
   git clone https://github.com/username/secret-notes.git
   cd secret-notes
   ```

2. **Gerekli Modülleri Yükleyin**:
   - Tkinter, Python ile varsayılan olarak gelir. Ek bir yükleme gerekmez.

3. **Uygulamayı Çalıştırın**:
   ```bash
   python main.py
   ```

---

## 📂 Proje Yapısı

```
Secret Notes/
│
├── main.py                 # Uygulamanın ana kodları
├── secretNotes.png         # Uygulama için kullanılan görsel
└── README.md               # Proje açıklamaları
```

---

## 📝 Kod Özetleri

### Şifreleme Fonksiyonu
```python
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
```

### Şifre Çözme Fonksiyonu
```python
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
```

---

## ⚙️ Kullanılan Teknolojiler

- **Python**
- **Tkinter**: Arayüz geliştirme
- **Base64**: Şifreleme işlemleri

---

## 📸 Ekran Görüntüsü

![Secret Notes Arayüzü](secretNotes.png)

---

## 📌 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

---

## 🤝 Katkıda Bulunma

Katkıda bulunmak istiyorsanız:

1. Depoyu forklayın.
2. Yeni bir dal oluşturun: `git checkout -b yeni-ozellik`.
3. Değişikliklerinizi yapın ve commitleyin: `git commit -m 'Yeni özellik ekle'`.
4. Dalınızı push edin: `git push origin yeni-ozellik`.
5. Bir Pull Request açın.

---

## ✨ İletişim

Herhangi bir soru veya öneriniz varsa lütfen [sait.sabuncu@hotmail.com](sait.sabuncu@hotmail.com) üzerinden iletişime geçin.
```

---

### **README.md İçeriği Hakkında**
- **Açıklayıcı Başlangıç**: Uygulamanın amacını net bir şekilde anlatır.
- **Kullanım Talimatları**: Uygulamayı nasıl çalıştıracağınızı açıklar.
- **Proje Yapısı**: Dosyaların ne işe yaradığını açıklar.
- **Kod Örnekleri**: Öne çıkan kod parçalarını içerir.
- **Katkı ve Lisans**: Projenize katkı yapmak isteyenler için rehber sunar.
