# 🧮 Betik Diller Ders Ödevi

## 🎯 Proje Amacı
Bu proje, verilen bir **people.csv** dosyasını okuyarak şu işlemleri yapar:

- Zorunlu sütunları kontrol eder (`name`, `age`, `city`)
- Eksik veya hatalı kayıtları temizler (`age` boş veya sayısal değilse çıkarılır)

Kalan verilerden:
- Geçerli kayıt sayısını hesaplar  
- Ortalama yaşı bulur  
- Şehirlere göre kişi sayılarını belirler  

Sonuçlar hem **JSON** hem de **TXT raporu** olarak kaydedilir.

---

## ⚙️ Çalıştırma
1. `people.csv` dosyasını proje klasörüne yerleştir.  
2. Terminalden çalıştır:
   ```bash
   python app.py

### 🖥️ Program Çalışma Ekranı
Aşağıda, programın terminalde çalıştırıldığında ürettiği örnek çıktı görülmektedir: 
<img width="392" height="113" alt="image" src="https://github.com/user-attachments/assets/b187182e-7002-4d26-b048-834a19a606a9" />
<img width="240" height="366" alt="image" src="https://github.com/user-attachments/assets/a2011be7-4b24-4246-8d4a-8ccacd67dc7d" />
