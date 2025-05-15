def calculate_risk(breed, diseases_type, diseases_data):

    # Filtrujemy dane dla wybranej rasy i typu choroby
    breed_data = diseases_data[(diseases_data["rasa"] == breed) & 
                               (diseases_data["typ_choroby"] == diseases_type)]

    # Sprawdzamy, czy mamy dane
    if breed_data.empty:
        return f"Brak danych dla rasy '{breed}' i typu choroby '{diseases_type}'."

    # Sortowanie po chorobie
    breed_data = breed_data.sort_values(by=['choroba'])

    # Tworzenie wyniku
    results = "\n".join(f"{row['choroba']}: {row['ryzyko_zachorowania']}%" for _, row in breed_data.iterrows())

    return results
