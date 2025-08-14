import math

# FUNZIONI 2D

def area_rettangolo(base, altezza):
    return round(base * altezza, 2)

def perimetro_rettangolo(base, altezza):
    return round(2 * (base + altezza),2)

def area_triangolo(base, altezza):
    return round((base * altezza) / 2, 2)

def perimetro_triangolo(lato1,lato2,lato3):
    return round(lato1 + lato2 + lato3,2)

def area_cerchio(raggio):
    return round(math.pi * raggio**2, 2)

def perimetro_cerchio(raggio):
    return round(2 * math.pi * raggio,2)

# FUNZIONI 3D

def volume_cubo(lato):
    return round(lato**3,2)

def superficie_cubo(lato):
    return round(6 * lato**2,2)

def volume_parallelepipedo(lato1, lato2, altezza):
    return round(lato1 * lato2 * altezza,2)

def superficie_parallelepipedo(lato1, lato2,altezza):
    return round(2 * (lato1 * lato2 + lato1 * altezza + lato2 * altezza),2)

def volume_sfera(raggio):
    return round((4 / 3) * math.pi * raggio**3, 2)

def superficie_sfera(raggio):
    return round(4 * math.pi * raggio**2, 2)

def volume_cilindro(raggio, altezza):
    return round(math.pi * raggio**2 * altezza, 2)

def superficie_cilindro(raggio,altezza):
    return round(2 * math.pi * raggio**2 + 2 * math.pi * raggio * altezza, 2)

# Menù principale

while True:
    scelta = input("---CALCOLATORE GEOMETRICO---"
                   "\n 1- Figure piane (2D)"
                   "\n 2- Solidi (3D)"
                   "\n 3- Esci"
                   "\n Scegli: ").strip()
    # Inizio blocco figure piane
    if scelta == "1":
        while True:
            scelta_figura = input("---FIGURE PIANE---"
                                  "\n 1- Rettangolo"
                                  "\n 2- Triangolo"
                                  "\n 3- Cerchio"
                                  "\n 0- Torna al menù principale"
                                  "\n Scegli la figura: ").strip()
            if scelta_figura == "0":
                break

            elif scelta_figura == "1":
                while True:
                    area_o_perimetro = input("Cosa vuoi calcolare? "
                                             "\n a) Area"
                                             "\n b) Perimetro"
                                             "\n x) Torna indietro"
                                             "\n > ").strip().lower()
                    if area_o_perimetro == "a":
                        try:
                            b = float(input("Inserisci la base del rettangolo: "))
                            a = float(input("Inserisci l'altezza del rettangolo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if b<=0 or a <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("L'area del rettangolo è: ", area_rettangolo(b, a))

                    elif area_o_perimetro == "b":
                        try:
                            b = float(input("Inserisci la base del rettangolo: "))
                            a = float(input("Inserisci l'altezza del rettangolo "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if b<=0 or a <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("Il perimetro del rettangolo è: ", perimetro_rettangolo(b, a))

                    elif area_o_perimetro == "x":
                        break
                    else:
                        print("Scelta non valida. Selezionare voce presente nel menù")

            elif scelta_figura == "2":
                while True:
                    area_o_perimetro = input("Cosa vuoi calcolare? "
                                             "\n a) Area"
                                             "\n b) Perimetro"
                                             "\n x) Torna indietro"
                                             "\n > ").strip().lower()
                    if area_o_perimetro == "a":
                        try:
                            b = float(input("Inserisci la base del triangolo: "))
                            a = float(input("Inserisci l'altezza del triangolo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if b <= 0 or a <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("L'area del triangolo è: ", area_triangolo(b, a))

                    elif area_o_perimetro == "b":
                        try:
                            lato_1 = float(input("Inserisci lato 1 del triangolo: "))
                            lato_2 = float(input("Inserisci lato 2 del triangolo: "))
                            lato_3 = float(input("Inserire lato 3 del triangolo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if lato_1 <=0 or lato_2 <=0 or lato_3 <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("Il perimetro del triangolo è: ",perimetro_triangolo(lato_1, lato_2, lato_3))

                    elif area_o_perimetro == "x":
                        break
                    else:
                        print("Scelta non valida. Selezionare voce presente nel menù")

            elif scelta_figura == "3":
                while True:
                    area_o_perimetro = input("Cosa vuoi calcolare? "
                                             "\n a) Area"
                                             "\n b) Perimetro"
                                             "\n x) Torna indietro"
                                             "\n > ").strip().lower()
                    if area_o_perimetro == "a":
                        try:
                            r = float(input("Inserisci raggio del cerchio: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if r <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("L'area del cerchio è: ",area_cerchio(r))

                    elif area_o_perimetro == "b":
                        try:
                            r = float(input("Inserisci raggio del cerchio: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if r <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("La circonferenza del cerchio è: ",perimetro_cerchio(r))

                    elif area_o_perimetro == "x":
                        break
                    else:
                        print("Scelta non valida. Selezionare voce presente nel menù")
            else:
                print("Scelta non valida. Selezionare voce presente nel menù")



    # inizio blocco Solidi
    elif scelta == "2":
        while True:
            scelta_figura = input("---SOLIDI---"
                                  "\n 1- Cubo"
                                  "\n 2- Parallelepipedo"
                                  "\n 3- Sfera"
                                  "\n 4- Cilindro"
                                  "\n 0- Torna al menù principale"
                                  "\n Scegli la figura: ").strip()
            if scelta_figura == "1":
                while True:
                    volume_o_superficie = input("Cosa vuoi calcolare? "
                                             "\n a) Volume"
                                             "\n b) Superficie"
                                             "\n x) Torna indietro"
                                             "\n > ").strip().lower()
                    if volume_o_superficie == "a":
                        try:
                            l = float(input("Inserisci il lato del cubo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if l <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("Il volume del cubo è: ", volume_cubo(l))

                    elif volume_o_superficie == "b":
                        try:
                            l = float(input("Inserisci il lato del cubo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if l <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("La superficie del cubo è: ", superficie_cubo(l))

                    elif volume_o_superficie == "x":
                        break
                    else:
                        print("Scelta non valida. Selezionare voce presente nel menù")

            elif scelta_figura == "2":
                while True:
                    volume_o_superficie = input("Cosa vuoi calcolare? "
                                                "\n a) Volume"
                                                "\n b) Superficie"
                                                "\n x) Torna indietro"
                                                "\n > ").strip().lower()
                    if volume_o_superficie == "a":
                        try:
                            lato_1 = float(input("Inserisci lato 1 del parallelepipedo: "))
                            lato_2 = float(input("Inserisci lato 2 del parallelepipedo: "))
                            a = float(input("Inserisci altezza del parallelepipedo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if lato_1 <=0 or lato_2 <=0 or a <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("Il volume del parallelepipedo è: ",volume_parallelepipedo(lato_1, lato_2, a))

                    elif volume_o_superficie == "b":
                        try:
                            lato_1 = float(input("Inserisci lato 1 del parallelepipedo: "))
                            lato_2 = float(input("Inserisci lato 2 del parallelepipedo: "))
                            a = float(input("Inserisci altezza del parallelepipedo: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if lato_1 <=0 or lato_2 <=0 or a <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("La superficie del parallelepipedo è: ",superficie_parallelepipedo(lato_1, lato_2, a))

                    elif volume_o_superficie == "x":
                        break
                    else:
                        print("Scelta non valida. Selezionare voce presente nel menù")

            elif scelta_figura == "3":
                while True:
                    volume_o_superficie = input("Cosa vuoi calcolare? "
                                                "\n a) Volume"
                                                "\n b) Superficie"
                                                "\n x) Torna indietro"
                                                "\n > ").strip().lower()
                    if volume_o_superficie == "a":
                        try:
                            r =float(input("Inserire raggio della sfera: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if r <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("Il volume della sfera è: ",volume_sfera(r))

                    elif volume_o_superficie == "b":
                        try:
                            r = float(input("Inserire raggio della sfera: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if r <= 0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("La superficie della sfera è: ",superficie_sfera(r))

                    elif volume_o_superficie == "x":
                        break
                    else:
                        print("Scelta non valida. Selezionare voce presente nel menù")

            elif scelta_figura == "4":
                while True:
                    volume_o_superficie = input("Cosa vuoi calcolare? "
                                                "\n a) Volume"
                                                "\n b) Superficie"
                                                "\n x) Torna indietro"
                                                "\n > ").strip().lower()
                    if volume_o_superficie == "a":
                        try:
                            r = float(input("Inserire raggio del cilindro: "))
                            a = float(input("Inserire l'altezza del cilindro: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if r <=0 or a <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("Il volume del cilindro è: ",volume_cilindro(r, a))

                    if volume_o_superficie == "b":
                        try:
                            r = float(input("Inserire raggio del cilindro: "))
                            a = float(input("Inserire l'altezza del cilindro: "))
                        except ValueError:
                            print("Errore: Inserire solo numeri")
                            continue
                        if r <=0 or a <=0:
                            print("Errore: Inserire numeri positivi e diversi da zero")
                        else:
                            print("La superficie del cilindro è: ",superficie_cilindro(r, a))

                    if volume_o_superficie == "x":
                        break

            elif scelta_figura == "0":
                break
            else:
                print("Scelta non valida. Selezionare voce presente nel menù")

    elif scelta == "3":
        print("\nGrazie per aver utilizzato il calcolatore geometrico!")
        break
    else:
        print("Scelta non valida. Selezionare voce presente nel menù")

"""
Commento personale: Notando che il codice si ripete molto con la stessa struttura,
probabilmente avrei potuto creare una funzione per chiedere i numeri in input in modo da
evitare di riscrivere sempre lo stesso schema di try/except con relativi controlli if <= 0 
accorciando così il codice e rendendolo più compatto.
Non ho voluto azzardare per mancanza di fiducia in me stessa :D
"""















