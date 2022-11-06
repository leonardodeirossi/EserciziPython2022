"""
Esercizio 3 - Maggiore tra tre numeri

Descrizione: Dati in input tre numeri determinare qual'è il maggiore.
Autore: LEONARDO ESSAM DEI ROSSI (leonardo.deirossi@buonarroti.tn.it)

Parte di teoria: come ulteriore passo in questo esercizio viene introdotta la parola "elif", questa parola fa parte del costrutto di selezione "if"
                 e permette di "tentare" una seconda condizione nel caso la prima non fosse soddisfatta (quindi entrerebbe nel ramo "else").
"""

# Definizione delle variabili
numero1 = 0.0
numero2 = 0.0
numero3 = 0.0
maggiore = 0.0

# Fase di input
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

# Fase di elaborazione

"""
Alle righe 30 e 32 viene introdotta la parola "elif", in questo esempio il programma verifica se il primo numero sia maggiore degli altri due, in caso contrario
prova a vedere se il secondo numero è maggiore degli altri due e infine prova a vedere se il terzo numero è maggiore degli altri due.
"""
if (numero1 > numero2) and (numero1 > numero3):
    maggiore = numero1
elif (numero2 > numero1) and (numero2 > numero3):
    maggiore = numero2
elif (numero3 > numero1) and (numero3 > numero2):
    maggiore = numero3

# Fase di output
print("Il numero maggiore è:", maggiore)
