# 📈 Finansal Öngörü: Çoklu Doğrusal Regresyon Modeli

Bu proje, ekonomik göstergeler (Dolar Kuru, Faiz, Enflasyon vb.) ile bir hisse senedi fiyatı arasındaki ilişkiyi analiz eden ve Makine Öğrenmesi (Machine Learning) tekniklerini kullanarak gelecek fiyat öngörüsü yapan bir uygulamadır.

## 🧠 Teorik Arka Plan (Ders Notlarımdan)

Bu model, Arthur Samuel'in tanımladığı gibi bilgisayara "açıkça programlanmadan öğrenme yeteneği kazandırma" prensibiyle çalışır.

* **Model Türü:** Denetimli Öğrenme (Supervised Learning) - Regresyon.
* **Hedef:** Sürekli bir değer (Hisse Fiyatı) tahmini yapmak.
* **Matematiksel Temel:** Model, Hipotez Fonksiyonu ($f_{w,b}(x) = wx + b$) üzerinden çalışır.
* **Optimizasyon:** Maliyet Fonksiyonu (MSE) kullanılarak hata payı hesaplanır ve Gradyan İnişi (Gradient Descent) algoritması ile ağırlıklar ($w$) ve sapma ($b$) değerleri optimize edilir.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.12**
* **Pandas:** Veri manipülasyonu ve CSV yönetimi.
* **Scikit-Learn:** `LinearRegression` modeli ve `r2_score` hesaplama.
* **Matplotlib:** Veri görselleştirme ve regresyon doğrusu çizimi.

## 📊 Veriseti Yapısı (Data Dictionary)

| Özellik (Feature) | Açıklama |
| :--- | :--- |
| Dolar_Kuru | Güncel USD/TRY kuru. |
| Faiz_Orani | Merkez Bankası politika faiz oranı. |
| Arge_Harcamasi | Şirketin teknolojik yatırımları. |
| BIST_100_Endeks | Borsa İstanbul genel endeks değeri. |
| Enflasyon_Orani | Yıllık tüketici enflasyonu (TÜFE). |
| **Hisse_Fiyati** | **Hedef Değişken (Bağımlı Değişken).** |

## 🚀 Nasıl Çalıştırılır?

1. Repoyu bilgisayarınıza indirin.
2. Gerekli kütüphaneleri yükleyin: `pip install pandas scikit-learn matplotlib`.
3. `StockPrice-MultiReg-ML` dosyasını çalıştırın.
 `dataset ile modeli aynı dosyaya alınız ve aldığınız dosyadaki datasetin yolunu koddaki gerekli yere yazınız örnek:df = pd.read_csv('stockprice_prediction.py/ekonomik_veriler.csv')`
5. Terminale güncel ekonomik verileri girin (veya Ar-Ge gibi bilmediğiniz verileri boş bırakarak ortalama değer atanmasını sağlayın).
6. Grafikteki **Kırmızı Yıldız** ile kendi tahmininizi görün!

## 📉 Model Performansı

Modelim, eğitim verileri üzerinde **0.996 R² Skoru** elde ederek değişkenler arasındaki pattern'leri (örüntüleri) çok yüksek bir doğrulukla kavramıştır.

---
**Hazırlayan:** Arda (@ardacodes)
https://ardaportakalkoku.com/
