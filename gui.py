import tkinter as tk
from main import ikiliyi_ondaliga_cevir

pencere = tk.Tk()
pencere.title("Bin2Dec - Binary to Decimal")
pencere.geometry("350x200")

def butona_tiklandiginda():
    sayi = giris_kutusu.get()
    sonuc = ikiliyi_ondaliga_cevir(sayi)
    sonuc_etiketi.config(text=sonuc)

etiket = tk.Label(pencere, text="Bir ikili sayı giriniz:")
giris_kutusu = tk.Entry(pencere)
buton = tk.Button(pencere, text="Dönüştür", command=butona_tiklandiginda)
sonuc_etiketi = tk.Label(pencere, text="Sonuç")

etiket.pack(pady=5)
giris_kutusu.pack(pady=5)
buton.pack(pady=10)
sonuc_etiketi.pack(pady=10)

pencere.mainloop()