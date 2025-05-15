import pandas as pd
import re

def cleaned_data():
    df = pd.read_excel("D:\\chorobyPsowPyV3.0\\data\\diseases.xlsx")
    print("Kolumny w DataFrame po wczytaniu pliku:", df.columns.tolist())

    # Usuń wiersze zawierające 'Sub-total'
    df = df[~df['Type'].astype(str).str.contains('Sub-total', na=False)]

    # Wypełnienie brakujących wartości w kolumnie 'Type'
    df['Type'].fillna(method='ffill', inplace=True)

    # Przekształcenie do formatu długiego (melt)
    df_long = df.melt(id_vars=['Type', 'Disease'], var_name='rasa', value_name='ryzyko')

    # 1. Usuń nawiasy i przekonwertuj na float
    df_long['ryzyko'] = df_long['ryzyko'].astype(str).apply(
        lambda x: re.search(r'\(([\d,.]+)\)', x).group(1) if re.search(r'\(([\d,.]+)\)', x) else None
    )

    # 2. Konwersja na liczby
    df_long['ryzyko'] = df_long['ryzyko'].str.replace(',', '.').astype(float)

    # 3. Zmień nazwy kolumn
    df_long.rename(columns={'Type': 'typ_choroby', 'Disease': 'choroba', 'ryzyko': 'ryzyko_zachorowania'}, inplace=True)


    return df_long

if __name__ == "__main__":
    print(cleaned_data())
