import math

#Creo tutte le funzioni che mi serviranno per la calcolatrice semplice

def addizione(x,y):
    return x+y

def sottrazione(x,y):
    return x-y

def moltiplicazione(x,y):
    return x * y

def divisione(x,y):
    return x/y

def percentuale(x,y):
    return (x * y)/100
# Creo anche un dizionario di funzioni disponibili all'utente che gli servirà nella voce g) del
#menù della calcolatrice scientifica

funzioni_disponibili = {
    # logaritmi
    "log": math.log,         # log naturale o con base
    "log10": math.log10,     # log base 10
    # radici e potenze
    "sqrt": math.sqrt,
    "pow": math.pow,
    # trigonometria
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e          #esponenziali
}

#Primo step: devo chiedere all'utente di poter scegliere tra calcolatrice semplice o scientifica

while True:
    scelta = input("Scegli tra: \n 1. Calcolatrice semplice \n 2. Calcolatrice scientifica \n> ")
# Calcolatrice semplice
    if scelta == "1":
        print("La scelta selezionata è: Calcolatrice semplice")
        print("Quale operazione ti interessa eseguire?")
#Creo il menù di operazioni per la calcolatrice semplice con la possibiltà di uscire e tornare
#al menù principale (Grazie al while True/break).
        while True:
            scelta_operazione = input("Scegli tra: "
                                      "\n a) addizione;"
                                      "\n b) sottrazione;"
                                      "\n c) moltiplicazione;"
                                      "\n d) divisione;"
                                      "\n e) percentuale;"
                                      "\n x) Torna al menù principale."
                                      "\n > ")
            if scelta_operazione == "x":
                break
            try: #Gestione dell'errore nell'eventualità che l'utente inserisca lettere anzichè numeri
                if scelta_operazione == "a":
                    primo = float(input("Inserisci il primo numero: "))
                    secondo = float(input("Inserisci il secondo numero: "))
                    print("La somma tra i due numeri inseriti è: ", addizione(primo, secondo))
                elif scelta_operazione == "b":
                    primo = float(input("Inserisci il primo numero: "))
                    secondo = float(input("Inserisci il secondo numero: "))
                    print("La sottrazione tra i due numeri inseriti è: ", sottrazione(primo, secondo))
                elif scelta_operazione == "c":
                    primo = float(input("Inserisci il primo numero: "))
                    secondo = float(input("Inserisci il secondo numero: "))
                    print("La moltiplicazione tra i due numeri inseriti è: ", moltiplicazione(primo, secondo))
                elif scelta_operazione == "d":
                    primo = float(input("Inserisci il primo numero: "))
                    secondo = float(input("Inserisci il secondo numero: "))
                    if secondo == 0:
                        print("Errore: Divisione per zero")
                    else:
                        print("La divisione tra i due numeri inseriti è: ", divisione(primo, secondo))
                elif scelta_operazione == "e":
                    primo = float(input("Inserisci il numero di cui vuoi calcolare la percentuale: "))
                    secondo = float(input("Inserisci il valore della percentuale: "))
                    print(f"Il {secondo} % di {primo} è: ", percentuale(primo, secondo))
                elif scelta_operazione not in ["a", "b", "c", "d", "e", "x"]:
                    print("La scelta selezionata non è valida. Scegliere opzione presente nel menù ")
            except ValueError:
                print("Errore: Inserire solo numeri ")

# Calcolatrice scientifica
    if scelta == "2":
        print("La scelta selezionata è: Calcolatrice scientifica")
        print("Quale operazione ti interessa eseguire?")
        while True:
            scelta_operazione=input("Scegli tra: "
                                    "\n a) potenza;"
                                    "\n b) radice quadrata;"
                                    "\n c) seno;"
                                    "\n d) coseno;"
                                    "\n e) tangente;"
                                    "\n f) logaritmo;"
                                    "\n g) funzione da scrivere;"
                                    "\n x) Torna al menù principale."
                                    "\n > ")
            if scelta_operazione == "x":
                break
            try:
                if scelta_operazione == "a":
                    numero = float(input("Inserisci il numero da elevare a potenza: "))
                    potenza = float(input("Inserisci la potenza a cui elevare il numero: "))
                    risultato_potenza = math.pow(numero, potenza)
                    print("Il risultato è: ", round(risultato_potenza, 4))
                elif scelta_operazione == "b":
                    numero = float(input("Inserisci il numero: "))
                    if numero < 0:
                        print("Errore: Il numero deve essere positivo")
                    else:
                        risultato_radice = math.sqrt(numero)
                        print("Il risultato è: ", round(risultato_radice, 4))
                elif scelta_operazione == "c":
                    numero = float(input("Inserisci un numero: "))
                    risultato_seno = math.sin(numero)
                    print("Il risultato è: ", round(risultato_seno, 4))
                elif scelta_operazione == "d":
                    numero = float(input("Inserisci un numero: "))
                    risultato_coseno = math.cos(numero)
                    print("Il risultato è: ", round(risultato_coseno, 4))
                elif scelta_operazione == "e":
                    numero = float(input("Inserisci un numero: "))
                    risultato_tangente = math.tan(numero)
                    print("Il risultato è: ", round(risultato_tangente, 4))
                elif scelta_operazione == "f":
                    numero = float(input("Inserisci un numero: "))
                    if numero < 0:
                        print("Errore: il numero deve essere positivo.")
                    else:
                        risultato_logaritmo = math.log(numero)
                        print("Il risultato è: ", round(risultato_logaritmo, 4))
                elif scelta_operazione == "g":
                    espressione = input("Inserisci un'espressione: ")
                    try:
                        risultato = eval(espressione, {"__builtins__": None}, funzioni_disponibili)
                        print("Risultato:", round(risultato, 4))
                    except Exception as e:
                        print(f"Errore nell'espressione: ", e)

                elif scelta_operazione not in ["a", "b", "c", "d", "e", "f", "g", "x"]:
                    print("La scelta selezionata non è valida. Scegliere opzione presente nel menù ")
            except ValueError:
                print("Errore: Inserire solo numeri ")

# Fine Programma!



















