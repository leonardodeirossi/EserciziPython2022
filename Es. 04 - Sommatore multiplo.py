"""
Esercizio 4 - Sommatore multiplo

Descrizione: Dati in input un numero e il numero di ripetizioni moltiplicare il primo per 2 tante volte quanto il secondo.
Autore: LEONARDO ESSAM DEI ROSSI (leonardo.deirossi@buonarroti.tn.it)

Parte di teoria: lo scopo di questo esercizio è di prendere in input un numero e moltiplicarlo per 2 un numero N di volte, per questo scopo
                 utilizzeremo il construtto di iterazione "while", che ci permette di ripetere un'operazione finché è soddisfatta una condizione.
"""

# Definizione delle variabili
numero = 0.0
numeroRipetizioni = 0
numeroIterazioni = 0

# Fase di input
numero = float(input("Inserisci il numero da moltiplicare: "))
numeroRipetizioni = int(input("Inserisci il numero di volte: "))

# Fase di elaborazione

""" 
alla riga 25 viene posta come condizione che il numero di iterazioni (quante volte ho fatto quella cosa) sia minore del numero di iterazioni che mi ha chiesto l'utente.
"""
while (numeroIterazioni < numeroRipetizioni):
    numero = numero * 2
    numeroIterazioni = numeroIterazioni + 1

# Fase di output
print("Il nuovo numero è ", numero)
