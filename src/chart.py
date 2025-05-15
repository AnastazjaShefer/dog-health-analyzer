import matplotlib
matplotlib.use("Agg")  # Ustawienie backendu, aby działało poprawnie w Tkinterze

import matplotlib.pyplot as plt
import numpy as np

def diseases_chart(diseases, probabilities):
    diseases = diseases.tolist() if isinstance(diseases, np.ndarray) else list(diseases)
    probabilities = probabilities.tolist() if isinstance(probabilities, np.ndarray) else list(probabilities)
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(diseases, probabilities, color="dodgerblue")

    # Dodanie większej liczby liczb na dole (oś X)
    ax.set_xticks(np.arange(0, max(probabilities) + 1, 0.2)) # co 0.2

    ax.grid(axis="x", linestyle="--", alpha=0.7, color="orange")  # "--" = linia przerywana, alpha = przezroczystość

    ax.set_xlabel("Prawdopodobieństwo (%)")
    ax.set_ylabel("Choroba")
    ax.set_title("Prawdopodobieństwo wystąpienia chorób")
    ax.set_xlim(0, 4)  # Upewnia się, że skala prawdopodobieństwa jest poprawna
    plt.tight_layout()  # Dopasowuje układ wykresu

    plt.show()
    return fig

if __name__ == "__main__":
    diseases = ["Choroba A", "Choroba B", "Choroba C"]
    probabilities = [30, 50, 20]

    fig = diseases_chart(diseases, probabilities)
    fig.show()  # Powinno otworzyć okno z wykresem