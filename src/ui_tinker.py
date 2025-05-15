from customtkinter import *
from risk_calculator import calculate_risk
from data_cleaner import cleaned_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from chart import diseases_chart

canvas = None
# Wczytanie danych o chorobach
diseases_data = cleaned_data()
diseases_names = list(set(diseases_data["rasa"]))
diseases_types = list(set(diseases_data["typ_choroby"]))
def start_ui():
    """Tworzy interfejs użytkownika do obliczania ryzyka chorób genetycznych u psów."""

    def calculate():
        global prob, canvas
        breed = breed_opt.get()
        diseases_type = type_opt.get()

        probability = calculate_risk(breed, diseases_type, diseases_data)
        # print("Surowe dane z calculate_risk:", probability)

        result_mess.configure(state="normal")
        # Aby wyczyścić zawartość
        result_mess.delete("1.0", "end")
        result_mess.insert("1.0", f"Prawdopodobieństwo wybranych chorób: \n\n{probability}")
        result_mess.configure(state="disabled")

        # Pobranie nazw chorób i wartości procentowych
        disease_labels = []
        prob = []

        for line in probability.split("\n"):
            if ":" in line and "%" in line:
                disease, value = line.split(":")
                disease = disease.strip()
                value = value.strip().replace("%", "")

                try:
                    prob.append(float(value))
                    disease_labels.append(disease)
                except ValueError:
                    continue

        print("Poprawnie przetworzone prob:", prob)
        print("Etykiety chorób:", disease_labels)

        if not prob:
            print("Brak danych do wykresu!")
            return

        # Usuwamy stary wykres
        if canvas:
            canvas.get_tk_widget().destroy()

        chart(disease_labels, prob)

    def chart(disease_labels, prob):
        global canvas
        # print("Dane do wykresu:", prob)

        figure = diseases_chart(disease_labels, prob)  # Teraz przekazujemy etykiety i wartości

        canvas = FigureCanvasTkAgg(figure, master=app)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.95, rely=0.3, anchor="ne")

        canvas.draw()

    # Tworzenie głównego okna aplikacji
    app = CTk()
    set_appearance_mode("dark")
    app.title("Genetyczne Ryzyko Chorób u Psów")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f'{screen_width}x{screen_height}+0+0')

    styles = {
        "label_text": {"font" : ("Arial", 18)},
        "input": {"width": 200, "height": 40, "font" : ("Arial", 18)},
        "btn_1": {"width": 150, "height": 40},
        "result": {"font" : ("Aptos", 20), "fg_color": "transparent", "width": 450, "height": screen_height/1.6, "wrap": "word"}
    }

    # Wybór rasy psa
    CTkLabel(app, text="Rasa psa:", **styles["label_text"]).place(relx=0.41, rely=0.1, anchor="center")
    # breed_var = StringVar()
    # CTkEntry(app, textvariable=breed_var, **styles["input"]).pack()

    breed_opt = CTkComboBox(app, values=diseases_names, **styles["input"])
    breed_opt.place(relx=0.5, rely=0.1, anchor="center")
    breed_opt.set(diseases_names[0])

    #wybor typu choroby
    CTkLabel(app, text="Typ choroby:", **styles["label_text"]).place(relx=0.41, rely=0.15, anchor="center")
    type_opt = CTkComboBox(app, values=diseases_types, **styles["input"])
    type_opt.place(relx=0.5, rely=0.15, anchor="center")
    type_opt.set(diseases_types[0])

    # Przycisk obliczający prawdopodobieństwo
    oblicz = CTkButton(app, text="Oblicz", command=calculate, **styles["btn_1"], **styles["label_text"])
    oblicz.place(relx=0.5, rely=0.22, anchor="center")

    # pozioma linia
    hr = CTkFrame(app, height=2, fg_color="gray")
    hr.place(relx=0.5, rely=0.28, anchor="center", relwidth=0.95)

    # Pole do wyświetlenia wyniku
    result = StringVar()
    result_mess = CTkTextbox(app, **styles["result"], state = "normal")
    # result_mess.pack(pady=(40, 0), anchor = "w", padx=(30,0))
    result_mess.place(relx=0.02, rely=0.3, anchor="nw")
    # CTkEntry(app, textvariable=result, **styles["input"]).pack()


    # Uruchomienie interfejsu
    app.mainloop()
