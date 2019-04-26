import pandas as pd

# READ TXT-FILE
df = pd.read_csv('Econda_new.txt', sep=";", low_memory=False)

# DELATE NOT NECESARY COLUMNS
df = df.drop(['REQUEST_ID', 'FIRMA', 'SESSION_ID_1', 'VIEWTIME_IN_S', 'SEARCH_TREFFER', 'BESTELLSUMME', 'ABSATZ', 'COUPONWERT', 'NEUKUNDE', 'ANZAHL', 'ARTIKELNR', 'PROMOTIONNR', 'PPRICE', 'GROESSE', 'MARKTKENNZEICHEN'], axis=1)

# REPLACE NaN-Values WITH "-"
df['EVENT_TYPE'].fillna('-', inplace=True)
df['SEARCH_QUERY'].fillna('-', inplace=True)
df['KAUFPROZESS_STUFE'].fillna('-', inplace=True)

# SORT DATASET CHRONOLOGICAL
df = df.sort_values(by='DATUM_REQUEST')

# DETERMINE THE AMOUNT OF DIFFERENT VALUES OF VISITOR_ID AND SESSION_ID
# print(df['VISITOR_ID'].nunique())
# print(df['SESSION_ID'].nunique())

df = df[df['EVENT_TYPE'] == 'buy']
buy = df['SESSION_ID'].unique()
print(buy)

# SELECT DATA BY VISITOR_ID
# df = df[df['SESSION_ID'] == 96852013]
# print(df)