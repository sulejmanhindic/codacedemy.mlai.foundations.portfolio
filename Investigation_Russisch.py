import pandas as pd
import sys
import matplotlib.pyplot as plt 
import seaborn as sns

# Lese mit Pandas die Datei 'russia-investigation.csv' aus im try-Abschnitt
# Quelle: https://github.com/fivethirtyeight/data/tree/master/russia-investigation/russia-investigation.csv
russia_watergate = None
datei = 'russia-investigation.csv'

try:
    russia_watergate = pd.read_csv(datei)
except FileNotFoundError:
    print("Datei " + datei + " wurde nicht gefunden. Bitte vorhandene Datei eingeben.")
    sys.exit(1)

# Zeige die ersten 5 Datensätze an'
#russia_watergate.head() 
#russia_watergate.info()

#df = pd.DataFrame(russia_watergate)

# Zeige die Aufteilung auf, wie oft welcher Präsident investigiert wurde inkl. Ausgabe
print("Anzahl der Investigationen für jeden Präsidenten")
praesidenten_counts = russia_watergate.president.value_counts()
print(praesidenten_counts)
print()

# Zeige die Aufteilung auf, wie oft welcher Präsident investigiert wurde inkl. Ausgabe - normalisiert
print("Anzahl der Investigationen für jeden Präsidenten - Relation")
praesidenten_counts_props = russia_watergate.president.value_counts(normalize=True)
print(praesidenten_counts_props)
print()

# Erstelle ein Säulendiagram zu der Aufteilung
sns.countplot(x='president',data=russia_watergate)
plt.show()
plt.close()

# Erstelle ein Kreisdiagramm zu der Aufteilung
russia_watergate.president.value_counts().plot.pie()
plt.show()
plt.close()

