"""
Esercizio 5 - Tutti tranne zero

Descrizione: Continua a chiedere e a sommare numeri finché non trovi uno zero.
Autore: LEONARDO ESSAM DEI ROSSI (leonardo.deirossi@buonarroti.tn.it)

Parte di teoria: in questo esercizio la differenza sta nella condizione che andiamo a imporre, prima si poneva un limite massimo da non superare
                 per completare il ciclo, in questo caso il limite è la necessità che il numero sia diverso da zero (potenzialmente finché l'utente non
                 inserisce zero il programma andrà avanti all'infinito).
"""

# Definizione delle variabili
somma = 0.0
numero = 0.0

# Fase di input / elaborazione
"""
In questo caso le fasi di input e di elaborazione sono unite, questo perché durante l'elaborazione sarà necessario chedere all'utente dei nuovi valori
da sommare ai precedenti.
"""

numero = float(input("Inserisci il numero da sommare: ")) # In questo caso viene richiesto un inserimento iniziale per permettere al ciclo di partire

while (numero != 0):
    somma = somma + numero
    numero = float(input("Inserisci il numero da sommare: ")) # In questo caso invece chiede un nuovo numero all'utente

# Fase di output
print("La somma di tutti i numeri è ", somma)
