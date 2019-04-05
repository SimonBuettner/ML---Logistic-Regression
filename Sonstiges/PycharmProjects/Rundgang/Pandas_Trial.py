import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

desired_width=320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns',15)

filename = 'Klickdaten_WittD_190114_20.txt'

# [0]: Einlesen der Datei; Seperator ist ";"
df = pd.read_csv(filename, sep = ";", low_memory=False)

print("[1]: Head: Gibt die ersten 5 Zeilen aus")
print(df.head())

print("[2]: Listet alle möglichen Ausprägungen von EVENT_TYPE auf")
print(df.EVENT_TYPE.unique())

print("[3]: Zählt auf, wie oft jede Ausprägung von EVENT_TYPE vorkommt")
print(df['EVENT_TYPE'].value_counts())

# [4]: Löscht unbrauchbare Spalten aus der Tabelle
df = df.drop(['REQUEST_ID', 'FIRMA', 'ARTIKELNR','GROESSE', 'SEARCH_QUERY', 'CONTENT_NAME', 'MARKTKENNZEICHEN', 'MARKTKENNZEICHEN'], axis=1)

print("[5]: Ausgabe der verbliebenen Spalten")
print(df.columns)

print("[6]: Gibt Informationen zu einzelnen Spalten aus (Datentyp)")
print(df.info())

print("[7] Group by: Gruppiert EVENT_TYPE nach buy und gibt ersten 5 Zeilen aus")
grouped = df.groupby('EVENT_TYPE')
print(grouped.get_group('buy').head(30))
