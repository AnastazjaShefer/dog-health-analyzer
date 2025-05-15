# Aplikacja: Genetyczne Ryzyko Chorób u Psów

Aplikacja służy do analizy i wizualizacji prawdopodobieństwa wystąpienia chorób genetycznych u psów na podstawie rasy i typu choroby.


## Funkcje aplikacji

-  Wczytywanie danych o chorobach z pliku Excel.
-  Interaktywny wybór rasy psa i typu choroby.
-  Obliczanie ryzyka wystąpienia chorób.
-  Prezentacja wyników w formie tekstowej i graficznej (wykres słupkowy).
-  Nowoczesny interfejs graficzny (GUI) stworzony z użyciem `customtkinter`.

---

## Zrzuty ekranu
#### Po uruchomieniu aplikacji:

![Zrzut ekranu 2025-05-15 220456](https://github.com/user-attachments/assets/cfbbecc3-cf87-4298-8726-4a565d50f957)

#### Po naciśnięciu przycisku "oblicz":

![Zrzut ekranu 2025-05-15 220542](https://github.com/user-attachments/assets/6c375e99-8ae0-40da-9f09-525291228e18)

##### Wybór rasy i typu choroby z listy:

![Zrzut ekranu 2025-05-15 220656](https://github.com/user-attachments/assets/5cab2500-646c-46e8-bdb5-813e16c68dd9)

---

## Wykorzystane technologie

- [Python 3.12+](https://www.python.org/)
- [`pandas`](https://pandas.pydata.org/) – przetwarzanie danych
- [`matplotlib`](https://matplotlib.org/) – generowanie wykresów
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) – GUI
- `re` – wyrażenia regularne do ekstrakcji danych

---

## Źródło danych

Dane wykorzystywane w aplikacji pochodzą z ogólnodostępnej bazy badań naukowych. Zostały opracowane na podstawie wyników dotyczących genetycznej predyspozycji poszczególnych ras psów do wybranych chorób (Tabela 4).

Źródło: NCBI - National Library of Medicine, https://pmc.ncbi.nlm.nih.gov/articles/PMC8577088/ 

---

## Struktura projektu

```
data/
└── diseases.xlsx             # Plik Excel z danymi o chorobach psów

src/
├── main.py                  # Główna aplikacja – uruchamia interfejs
├── ui_tinker.py             # Interfejs graficzny (customtkinter)
├── chart.py                 # Generowanie wykresów chorób (matplotlib)
├── risk_calculator.py       # Obliczanie ryzyka chorób genetycznych
└── data_cleaner.py          # Czyszczenie i przekształcanie danych z Excela

README.md                    # Opis i dokumentacja projektu
```

---

## Instalacja wymaganych bibliotek (polecenie):

   ```bash
   pip install pandas matplotlib customtkinter openpyxl
