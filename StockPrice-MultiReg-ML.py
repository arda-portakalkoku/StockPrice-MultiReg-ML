# Finansal modelleme için gerekli kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


#modeli seçme linear regression çünkü labellerimiz sürekli bir değer (Dolar Kuru) ve bağımsız değişkenlerimiz (Faiz Oranı, Arge Harcaması) var. Bu nedenle, doğrusal regresyon modeli uygun olacaktır.
model = LinearRegression()

# read_excel yerine read_csv kullanıyoruz. dosyayı ml.py klasörüne attık ve xlsx formatında kaydettik.
df = pd.read_csv('ekonomik_veriler.csv')

#modelin eğitimi
y=df['Hisse_Fiyati'].values # bağımlı değişken
X = df[['Dolar_Kuru', 'Faiz_Orani', 'Arge_Harcamasi', 'BIST_100_Endeks', 'Enflasyon_Orani']].values  # bağımsız değişkenler
model.fit(X, y)

ortalama_arge = df['Arge_Harcamasi'].mean()#arge harcaması için ortalama değeri hesaplıyoruz. kullanıcı dğeri bilmiyorsa otomatik atanacak

#kullancıdan güncel veriler model eğitildikten sonra alınır. Kullanıcıdan alınan veriler model tarafından tahmin edilen hisse fiyatını hesaplamak için kullanılır.
while True:
    try:
        dolar=float(input("Güncel dolar kurunu giriniz: "))
        faiz=float(input("Güncel faiz oranını giriniz: "))
        arge_girisi = input("Güncel Arge Harcamasını giriniz (bilmiyorsanız enter'a basınız): ")
        if arge_girisi == '':
            arge = ortalama_arge  # Zaten float olduğu için tekrar çevirme
            print("Arge Harcaması değeri belirtilmedi. Ortalama değer kullanılacak.")
        else: 
            arge = float(arge_girisi)  # Kullanıcının girdiği değeri float'a çeviriyoruz.
        bist=float(input("Güncel BIST 100 Endeksini giriniz: "))
        enflasyon=float(input("Güncel Enflasyon oranını giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

#tahmin edilen hisse fiyatını hesaplamak için kullanıcıdan alınan verilerle modelin predict metodunu kullanarak tahmin yapıyoruz. Tahmin edilen hisse fiyatı ekrana yazdırılır.
yeni_veri=[[dolar,faiz,arge,bist,enflasyon]]
tahminedilen_fiyat=model.predict(yeni_veri)
print("\n----Tahmin Değeri----")
print(f"Öngörülen hisse fiyatı:[{tahminedilen_fiyat[0]:.2f}]")

#model istatistiği
print("\n----Model İstatistikleri----")
b0 = model.intercept_  # y ekseni kesişimi (sabit terim)
print("b0 eksenlerin kesişimi:", b0)
b1, b2, b3, b4, b5 = model.coef_  ##eğim
print("b1 (Dolar Kuru katsayısı):", b1)
b0 = model.predict([[0, 0, 0, 0, 0]])  # sabit terim
print("b0 (sabit terim):", b0)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)#modelin doğruluk oranı(1'e yakınlaştıkça modelin doğruluğu artar)
print("R² Skoru:", r2)

#verileri göselleştirme
plt.scatter(df['Dolar_Kuru'], df['Hisse_Fiyati'], color='blue', label='Dolar Kuru')
plt.grid()
plt.xlabel('Dolar Kuru')
plt.ylabel('Hisse Fiyati')
plt.title('Dolar Kuru vs Hisse Fiyati')

# Regresyon doğrusunu çiz
plt.plot(df['Dolar_Kuru'], y_pred, color='red', linewidth=2, label='Regresyon Doğrusu')
plt.legend()
# Her bir veri noktası için hata çizgisini çizdirelim
for i in range(len(df)):
    # x koordinatı: Dolar Kuru
    # y başlangıç: Gerçek Hisse Fiyatı, y bitiş: Tahmin Edilen Fiyat
    plt.plot([df['Dolar_Kuru'].iloc[i], df['Dolar_Kuru'].iloc[i]], 
             [df['Hisse_Fiyati'].iloc[i], y_pred[i]], 
             color='gray', linestyle='-', linewidth=1, alpha=0.5)
# Kullanıcının girdiği dolar kuru ve tahmin edilen hisse fiyatını grafikte gösterelim
plt.scatter(dolar,tahminedilen_fiyat[0], color='#27F5E0', label='Tahmin Edilen fiyat')
plt.legend()

plt.show()

