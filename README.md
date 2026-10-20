# Bin2Dec – İkili (Binary) → Ondalık (Decimal) Dönüştürücü

Dijital bilgisayarların temelini oluşturan 2 tabanlı (ikili) sayı sistemini anlamak ve ondalık karşılıklarını hesaplamak amacıyla geliştirilmiş başlangıç seviyesi bir Python projesidir.

Proje hem **komut satırından (CLI)** hem de saf Python (`tkinter`) ile geliştirilmiş **masaüstü grafik arayüzünden (GUI)** çalıştırılabilir.

---

## 🚀 Özellikler

- **Girdi Doğrulama:** Sadece `0` ve `1` rakamlarının girilmesine izin verir; geçersiz karakterlerde kullanıcıya anında uyarı verir.
- **Kısıtlamalara Tam Uyum:**
  - Kullanıcı girdilerini tutmak için hiçbir dizi/liste (`list`, `array`) kullanılmamıştır.
  - Basamak değerini hesaplamak için doğrudan matematiksel üs alma ($2^n$) mantığı kullanılmıştır.
- **Kullanıcı Dostu Arayüz (Tkinter GUI):**
  - Butonla veya klavyeden `Enter` tuşuna basarak hızlı dönüştürme.
  - Hata durumunda kırmızı, başarılı sonuçta yeşil renkli görsel geri bildirim.
- **🌟 Bonus Özellik (Sınırsız Basamak):** Varsayılan olarak 8 basamak kısıtlaması bulunur. İstenirse arayüzdeki onay kutusu işaretlenerek istenilen uzunlukta ikili sayı dönüştürülebilir.

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için harici hiçbir kütüphane yüklemenize gerek yoktur. Python 3'ün bilgisayarınızda kurulu olması yeterlidir.

### 1. Repoyu Klonlayın
```bash
git clone https://github.com/burkillife27/Bin2Dec.git
cd Bin2Dec
```

### 2. Masaüstü Arayüzünü (GUI) Çalıştırma
```bash
python gui.py
```

### 3. Komut Satırı (CLI) Versiyonunu Çalıştırma
```bash
python main.py
```

---

## 📁 Proje Yapısı

```
Bin2Dec/
│
├── main.py        # Çekirdek dönüştürme fonksiyonu ve CLI çalıştırma bloğu
├── gui.py         # Tkinter ile geliştirilmiş masaüstü arayüzü
├── .gitignore     # Git tarafından yok sayılacak geçici dosyalar
└── README.md      # Proje dokümantasyonu
```

---

## 📝 Lisans
Bu proje açık kaynaklıdır ve eğitim/öğrenme amacıyla serbestçe kullanılabilir (MIT Lisansı).


<img width="334" height="189" alt="Uİ_1" src="https://github.com/user-attachments/assets/762230c7-747c-4333-b0d2-3de4adf02401" />

<img width="343" height="189" alt="UI_2" src="https://github.com/user-attachments/assets/f660203e-da69-42cc-a1de-dba8fbb7ee2c" />

<img width="344" height="191" alt="UI_3" src="https://github.com/user-attachments/assets/23933808-1640-4194-8106-43186d03f685" />



