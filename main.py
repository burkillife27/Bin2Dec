#ikili_sayi = input("En fazla 8 haneli bir ikili sayı (binary) giriniz:")


def ikiliyi_ondaliga_cevir(ikili_sayi, sinirsiz=False):
    ondalik_deger = 0
    us = 0

    if len(ikili_sayi) > 8 and sinirsiz == False:
        return "HATA! Girdiğiniz sayı 8 karakterden fazla."

    else:
        for karakter in ikili_sayi:
            if karakter != "0" and karakter != "1":
                return "HATA! Sadece 0 ve 1 rakamlarından oluşan bir sayı giriniz."
        else:
            for karakter in ikili_sayi[::-1]:
                if karakter == "1":
                    ondalik_deger += 2 ** us

                us += 1
            return f"Giridiğiniz sayı: {ikili_sayi} -> Ondalık karşılığ: {ondalik_deger}"

if __name__ == "__main__":
    cevap = ikiliyi_ondaliga_cevir(input("En fazla 8 haneli bir ikili sayı (binary) giriniz:"))
    print(cevap)
