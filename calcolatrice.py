def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError
    return num / den

# Aggiungi le funzioni moltiplicazione e sottrazione
def sottrazione():
    pass

def moltiplicazione():
    pass

# Aggiungi una funzione magicNumbers per restituire una lista di tutti e soli i numeri interi dispari e multipli di 5 tra start e stop
def magicNumbers():
    # bonus: fallo su una unica riga con la list comprehension
    pass