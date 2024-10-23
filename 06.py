
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# veri oluşturur
data = {
    'boy_cm': [170, 165, 180, 175, 160, 168, 172, 158, 182, 177],
    'kilo_kg': [70, 55, 85, 65, 50, 58, 72, 53, 90, 68],
    'cinsiyet': ['k', 'k', 'e', 'k', 'k', 'e', 'e', 'k', 'e', 'e']
}

# pandas data frame oluşturur
df = pd.DataFrame(data)
print(df)
# seaborn grafik stili
sns.set_style("whitegrid")
# seaborn ile scatter plot oluşturur
sns.scatterplot(data=df,
                x="kilo_kg",
                y="boy_cm",
                hue="cinsiyet",
                size_order=(2700,6300),
                palette={"e":"blue","k":"pink"})
plt.xlabel("kilo (kg)")
plt.ylabel("boy (cm)")
plt.title("3 boyutlu görselleştirme")
plt.show()