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

> (Dodaj tutaj zrzuty ekranu aplikacji po uruchomieniu)

---

## Wykorzystane technologie

- [Python 3.12+](https://www.python.org/)
- [`pandas`](https://pandas.pydata.org/) – przetwarzanie danych
- [`matplotlib`](https://matplotlib.org/) – generowanie wykresów
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) – GUI
- `re` – wyrażenia regularne do ekstrakcji danych

---

## Struktura projektu
chorobyPsow/
│
├── data/
│ └── diseases.xlsx # Plik danych z informacjami o chorobach
│
├── src/
│ ├── main.py # Główne uruchomienie aplikacji
│ ├── ui_tinker.py # Interfejs graficzny
│ ├── chart.py # Generowanie wykresów
│ ├── risk_calculator.py # Obliczanie ryzyka chorób
│ └── data_cleaner.py # Wczytywanie i czyszczenie danych
│
└── README.md # Dokumentacja projektu

