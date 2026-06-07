"""
Kitap Takip Uygulaması

Amaç: Okunan/okunacak kitapları ekleyen, listeleyen, durumunu (okundu/okunmadı)
güncelleyen ve silen basit bir konsol uygulaması. Kitaplar 'kitaplar.json'
dosyasında saklanır; program kapanıp açılınca kayıtlar korunur.

Nasıl çalıştırılır:
python3 kitap.py

İşlevler:
1. Kitapları Listele
2. Yeni Kitap Ekle (boş başlık/yazar kabul etmez)
3. Okundu/Okunmadı İşaretle
4. Kitap Sil
5. Çıkış (kayıtları dosyaya yazar)
"""

import json
import os

DOSYA_ADI = "kitaplar.json"

def kitaplari_yukle():
    if os.path.exists(DOSYA_ADI):
        try:
            with open(DOSYA_ADI, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def kitaplari_kaydet(kitaplar):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(kitaplar, f, ensure_ascii=False, indent=4)

def kitaplari_listele(kitaplar):
    if not kitaplar:
        print("\nHenüz kayıtlı kitap yok.")
        return
    
    print("\nKİTAP LİSTESİ")
    for i, kitap in enumerate(kitaplar, 1):
        durum = "okundu" if kitap["okundu"] else "okunmadı"
        print(f"{i}. {kitap['baslik']} - {kitap['yazar']} [{durum}]")

def kitap_ekle(kitaplar):
    baslik = input("Kitap başlığı: ").strip()
    if not baslik:
        print("Başlık boş olamaz!")
        return
    
    yazar = input("Yazar: ").strip()
    if not yazar:
        print("Yazar boş olamaz!")
        return
    
    yeni_kitap = {
        "baslik": baslik,
        "yazar": yazar,
        "okundu": False
    }
    kitaplar.append(yeni_kitap)
    kitaplari_kaydet(kitaplar)
    print(f"'{baslik}' eklendi.\nKitaplar başarıyla kaydedildi.")

def durum_degistir(kitaplar):
    if not kitaplar:
        print("\nHenüz kayıtlı kitap yok. Önce kitap eklemelisiniz.")
        return
        
    kitaplari_listele(kitaplar)
    try:
        secim = int(input("Durumunu değiştirmek istediğiniz kitabın numarası: "))
        if 1 <= secim <= len(kitaplar):
            kitap = kitaplar[secim - 1]
            kitap["okundu"] = not kitap["okundu"]
            kitaplari_kaydet(kitaplar)
            durum_str = "okundu" if kitap["okundu"] else "okunmadı"
            print(f"'{kitap['baslik']}' artık [{durum_str}] olarak işaretlendi.\nKitaplar başarıyla kaydedildi.")
        else:
            print("Geçersiz kitap numarası!")
    except ValueError:
        print("Lütfen bir sayı girin!")

def kitap_sil(kitaplar):
    if not kitaplar:
        print("\nSilinecek kitap yok.")
        return
        
    kitaplari_listele(kitaplar)
    try:
        secim = int(input("Silmek istediğiniz kitabın numarası: "))
        if 1 <= secim <= len(kitaplar):
            silinen = kitaplar.pop(secim - 1)
            kitaplari_kaydet(kitaplar)
            print(f"'{silinen['baslik']}' silindi.\nKitaplar başarıyla kaydedildi.")
        else:
            print("Geçersiz kitap numarası!")
    except ValueError:
        print("Lütfen bir sayı girin!")

def ana_menu():
    kitaplar = kitaplari_yukle()
    if not kitaplar:
        print("Kitap Takip Uygulamasına Hoş Geldiniz!\nKayıt dosyası bulunamadı. Yeni bir liste oluşturuldu.")
    else:
        print("Kitap Takip Uygulamasına Hoş Geldiniz!\nKitaplar başarıyla yüklendi.")

    while True:
        print("\nKİTAP TAKİP UYGULAMASI")
        print("1. Kitapları Listele")
        print("2. Yeni Kitap Ekle")
        print("3. Okundu/Okunmadı İşaretle")
        print("4. Kitap Sil")
        print("5. Çıkış")
        
        secim = input("Seçiminiz (1-5): ").strip()
        
        if secim == "1":
            kitaplari_listele(kitaplar)
        elif secim == "2":
            kitap_ekle(kitaplar)
        elif secim == "3":
            durum_degistir(kitaplar)
        elif secim == "4":
            kitap_sil(kitaplar)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arası bir değer girin.")

if __name__ == "__main__":
    ana_menu()