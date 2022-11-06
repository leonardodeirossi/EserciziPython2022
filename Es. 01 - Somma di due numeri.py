"""
Esercizio 1 - Somma di due numeri

Descrizione: Dati in input due numeri esegue la somma e restituisce in output il valore.
Autore: LEONARDO ESSAM DEI ROSSI (leonardo.deirossi@buonarroti.tn.it)

Parte di teoria: nelle righe (x, y) sono presenti le due istruzioni di input, nello specifico per "numero1" e "numero2"; davanti alla parola chiave "input"
                 viene specificato il tipo di dato "float", questo tipo di dato permette di memorizzare valori con parte decimale (per esempio 3.14).
"""

# Definizione delle variabili
numero1 = 0.0
numero2 = 0.0
somma = 0.0

# Fase di input
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

# Fase di elaborazione
somma = numero1 + numero2

# Fase di output
print("La somma dei numeri è: ", somma)