import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

print("ilk beş değer:\n", df.head())
print("Ortalama hesap:", df["total_bill"].mean())
print("Max tip:", df["tip"].max())
print("Cinsiyet dağılımı:\n", df["sex"].value_counts())

gun_ort = df.groupby("day")["total_bill"].mean()

print("\nGünlere göre ortalama hesap:\n", gun_ort)
print("En yüksek ortalama hesap olan gün:", gun_ort.idxmax())
print("En yüksek ortalama hesap:", gun_ort.max())

print("\nCinsiyete göre ortalama tip:\n", df.groupby("sex")["tip"].mean())
print("\nSigara içenlere göre ortalama tip:\n", df.groupby("smoker")["tip"].mean())

import matplotlib.pyplot as plt

gun_ort.plot(kind="bar")

plt.title("Günlük ortalama hesap")
plt.xlabel("Gün")
plt.ylabel("Hesap")

plt.show()
