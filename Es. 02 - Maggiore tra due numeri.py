"""
Esercizio 1 - Somma di due numeri

Descrizione: Dati in input due numeri esegue la somma e restituisce in output il valore.
Autore: LEONARDO ESSAM DEI ROSSI (leonardo.deirossi@buonarroti.tn.it)

Parte di teoria: in questo esercizio viene introdotto il costrutto di selezione (detto comunemente "if"), questa istruzione permette di svolgere un'azione
                 solo nel caso si verifichi una determinata condizione (per esempio stampa "maggiore" se il numero dato è maggiore di 2).
"""

# Definizione delle variabili
numero1 = 0.0
numero2 = 0.0
maggiore = 0.0

# Fase di input
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

# Fase di elaborazione

"""
Alla riga 23 viene imposta la seguente condizione: se il numero che corrisponde a "numero1" è maggiore del numero che corrisponde a "numero2", allora il risultato
sarà che il primo numero è maggiore del secondo, in caso contrario sarà il viceversa.

Letteralmente la parola "if" significa "se" (se la condizione...) e la parola "else" significa "altrimenti".
"""
if (numero1 > numero2):
    maggiore = numero1
else:
    maggiore = numero2

# Fase di output
print("Il numero maggiore è:", maggiore)