import mysql.connector
from tabulate import tabulate #Ho installato tabulate per visualizzare graficamente le tabelle

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "libreria"
)
#Funzione per non accettare campi vuoti
def safe_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Questo campo non può essere vuoto.")

# Funzione gestione errori: chiede un numero intero in modo sicuro
def safe_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f" Inserisci un numero >= {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Inserisci un numero <= {max_value}.")
                continue
            return value
        except ValueError:
            print(" Devi inserire un numero intero valido.")

# Funzione gestione errori: chiede un numero decimale (float) in modo sicuro
def safe_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Inserisci un valore >= {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Inserisci un valore <= {max_value}.")
                continue
            return value
        except ValueError:
            print(" Devi inserire un numero decimale valido (es. 12.50).")

#-----------------------------------------------------------------------------------------------------
#Funzione per visualizzare i libri nel DB
def list_books ():
    cursor = conn.cursor()
    query = "SELECT b.id, b.title, b.price, s.copies FROM books b JOIN stock s ON b.id = s.book_id; "
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["id", "title", "price", "copies"], tablefmt="grid"))
    else:
        print("Nessun libro presente nel database.")

#-------------------------------------------------------------------------------------------------
#Funzione per aggiunge un libro nel DB
def add_book():
    cursor=conn.cursor()
    title = input("Titolo: ")
    price = safe_float("Prezzo (€): ", min_value=0.01)
    copies = safe_int("Copie iniziali: ", min_value=0)

    # Inserisce il libro
    query = "INSERT INTO books (title,price) VALUES (%s, %s);"
    cursor.execute(query,(title,price))
    book_id = cursor.lastrowid

    #Inserisce le copie
    query = "INSERT INTO stock (book_id,copies) VALUES (%s,%s);"
    cursor.execute(query,(book_id,copies))

    conn.commit()
    print("Libro aggiunto con ID: ", book_id)
#--------------------------------------------------------------------------------------------------
#Funzione per aggiungere un cliente nel DB
def add_customers():
    cursor=conn.cursor()
    fname=safe_input("Nome: ")
    lname=safe_input("Cognome: ")
    email=input("Email: ")
    phone=input(f"Telefono: ")
    street=input("Indirizzo: ")
    city=input("Città: ")
    postal_code=input(f"Codice postale: ")
    country =input("Paese: ")

    #Inserisce cliente
    query="INSERT INTO customers (first_name,last_name,email,phone) VALUES (%s,%s,%s,%s);"
    cursor.execute(query,(fname,lname,email,phone))
    customer_id=cursor.lastrowid

    #inserisce indirizzo e città
    cursor.execute("INSERT INTO addresses (customer_id,street,city,postal_code,country) VALUES (%s,%s,%s,%s,%s);",(customer_id,street,city,postal_code,country))
    conn.commit()

    print("Cliente aggiunto con ID, ", customer_id)
#-------------------------------------------------------------------------------
#Funzione per cercare persone tramite nome,cognome o email
def search_customers():
    cursor=conn.cursor(dictionary=True)
    ricerca=safe_input("Inserisci nome, cognome, email da cercare: ")
    query="""
    SELECT c.id,c.first_name,c.last_name, c.email, c.phone, a.city, a.country
    FROM customers c
    LEFT JOIN addresses a ON c.id=a.customer_id
    WHERE c.first_name LIKE %s OR c.last_name LIKE %s OR c.email LIKE %s; """
    jolly= f"%{ricerca}%"
    cursor.execute(query,(jolly,jolly,jolly))
    risultati=cursor.fetchall()

    if risultati:
        print("\nClienti trovati:")
        print(tabulate(risultati,headers="keys",tablefmt="grid"))

        while True:
            try:
                customer_id = int(input("\nInserisci l'ID del cliente scelto (0 per annullare): "))
                if customer_id == 0:
                    print("Operazione annullata.")
                    return None
                # controllo che l'id esista tra i risultati
                if any(r["id"] == customer_id for r in risultati):
                    return customer_id
                else:
                    print("ID non presente nella lista mostrata. Riprova.")
            except ValueError:
                print("Inserisci un numero intero valido.")
    else:
        print("Nessun cliente trovato!")
        return None


#---------------------------------------------------------------------------------
#Funzione per ottenere lo storico acquisti di un cliente
def customer_history():
    cursor=conn.cursor(dictionary=True)
    customer_id=safe_int("Inserisci l'ID del cliente: ",min_value=1)
    query="""
    SELECT s.id AS id_vendita, s.sale_date, b.title, si.qty, si.price
    FROM sales s
    JOIN sale_items si ON s.id=si.sale_id
    JOIN books b ON si.book_id=b.id
    WHERE s.customer_id=%s
    ORDER BY s.sale_date DESC;"""

    cursor.execute(query,(customer_id,))
    risultati=cursor.fetchall()
    if risultati:
        print(tabulate(risultati,headers="keys",tablefmt="grid"))
    else:
        print("Nessuna vendita trovata per questo cliente.")
#-----------------------------------------------------------------------------------------------
#Funzione per modificare un libro (titolo o prezzo)
def update_book():
    cursor=conn.cursor()
    book_id=safe_int("Inserisci l'Id del libro da modificare: ",min_value=1)
    title=input("Inserisci nuovo titolo (lascia vuoto se non vuoi modificare): ")
    price=safe_float("Inserisci nuovo prezzo (lascia vuoto se non vuoi modificare): ",min_value=0.01)

    if title and price:
        query="UPDATE books SET title=%s, price=%s WHERE id=%s;"
        parametri=(title,price,book_id)
    elif title:
        query="UPDATE books SET title=%s WHERE id_%s;"
        parametri=(title,book_id)
    elif price:
        query="UPDATE books SET price=%s WHERE id=%s;"
        parametri=(price,book_id)
    else:
        print("Nessun campo da aggiornare")
        return
    cursor.execute(query,parametri)
    conn.commit()
    print("Libro aggiornato con successo!")
#---------------------------------------------------------------------------------------------
#Funzione per eliminare libro e relativo stock
def delete_book():
    cursor=conn.cursor()
    book_id=safe_int("Inserisci l'ID da eliminare: ",min_value=1)
    conferma=input(f"Sei sicuro di voler eliminare il libro con ID: {book_id}? (s/n): ")
    if conferma.lower() !="s":
        print("Operazione annullata!")
        return
    cursor.execute("DELETE FROM stock WHERE book_id=%s",(book_id,))
    cursor.execute("DELETE FROM books WHERE id=%s",(book_id,))
    conn.commit()
    print("Libro eliminato con successo!")
#----------------------------------------------------------------------------------
#Funzione per cercare un libro e relativo numero di copie
def search_book():
    cursor=conn.cursor(dictionary=True)
    ricerca=safe_int("Inserisci titolo (anche parziale) del libro da cercare: ",min_value=1)
    jolly=f"%{ricerca}%"
    query=("""SELECT b.id,b.title,b.price,s.copies 
           FROM books b
           JOIN stock s ON b.id=s.book_id
           WHERE b.title LIKE %s;""")
    cursor.execute(query,(jolly,))
    risultato=cursor.fetchall()

    if risultato:
        print("\n Risultati della ricerca:")
        print(tabulate(risultato,headers="keys",tablefmt="grid"))

        for r in risultato:
            if r['copies']>0:
                print(f"{r['title']} è disponibile ({r['copies']} copie.")
            else:
                print(f"{r['title']} non è disponibile al momento.")
    else:
        print("Nessun libro trovato con questo titolo!")
#------------------------------------------------------------------------------------
#Funzione per estrarre le vendite nelle ultime 24h
def sales_last_day():
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT b.title,
    SUM(si.qty) AS total_sold,
    DATE(s.sale_date) AS sale_date
    FROM sale_items si
    JOIN sales s ON si.sales_id=s.id
    JOIN books b ON si.book_id=b.id
    WHERE s.sale_date >= NOW() - INTERVAL 1 DAY
    GROUP BY b.id, DATE(s.sale_date)
    ORDER BY s.sale_date DESC;
    """
    cursor.execute(query)
    risultato=cursor.fetchall()

    if risultato:
        print(f"\n Vendite nelle ultime 24 ore:")
        print(tabulate(risultato, headers="keys", tablefmt="grid"))
    else:
        print(" Nessuna vendita nelle ultime 24 ore.")
#----------------------------------------------------------------------------------------
#Funzione ricerca vendita negli ultimi tot giorni
def sales_last_days():
    cursor=conn.cursor(dictionary=True)
    days=safe_int("Inserisci il numero di giorni da analizzare: ",min_value=1)
    query = f"""
       SELECT b.title,
       SUM(si.qty) AS total_sold,
       DATE(s.sale_date) AS sale_date
       FROM sale_items si
       JOIN sales s ON si.sales_id=s.id
       JOIN books b ON si.book_id=b.id
       WHERE s.sale_date >= NOW() - INTERVAL {days} DAY
       GROUP BY b.id, DATE(s.sale_date)
       ORDER BY s.sale_date DESC; """
    cursor.execute(query)
    risultato=cursor.fetchall()

    if risultato:
        print(f"\n Vendite negli ultimi {days} giorni:")
        print(tabulate(risultato, headers="keys", tablefmt="grid"))
    else:
        print("Nessuna vendita nel periodo selezionato.")
#-----------------------------------------------------------------------------
#Funzione per estrarre i 10 libri più venduti
def top_10_book():
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT b.title,
    SUM(si.qty) AS total_sold
    FROM sale_items si
    JOIN books b ON si.book_id=b.id
    GROUP BY b.id
    ORDER BY total_sold DESC
    LIMIT 10;
    """
    cursor.execute(query)
    risultato=cursor.fetchall()
    if risultato:
        print("\nTop 10 libri più venduti:")
        print(tabulate(risultato, headers="keys", tablefmt="grid"))
    else:
        print("Nessuna vendita registrata.")

#Funzione per effettuare vendita da cliente già inserito
def make_purchase():
    cursor=conn.cursor(dictionary=True)
    print("Cerca un cliente esistente ")
    customer_id=search_customers()
    if not customer_id:
        return

    #Faccio mostrare i libri disponibili
    print("\n Libri disponibili: ")
    cursor.execute("SELECT b.id, b.title, s.copies,b.price FROM books b JOIN stock s ON b.id=s.book_id")
    books = cursor.fetchall()
    print(tabulate(books,headers="keys",tablefmt="grid"))

    #Faccio selezionare il libro che vuole comprare e la quantità
    book_id = safe_int("Inserisci l'ID del libro da acquistare: ", min_value=1)
    qty = safe_int("Quante copie vuoi acquistare? ", min_value=1)

    #Faccio un controllo sulle copie disponibili
    cursor.execute("SELECT copies,price FROM stock s JOIN books b ON s.book_id = b.id WHERE book_id=%s",(book_id,))
    risultati=cursor.fetchone()

    if not risultati:
        print("Libro non trovato")
    if risultati["copies"] < qty:
        print(f"Solo {risultati['copies']} disponibili.")
        return

    #Inserisco la vendita nella tabella
    cursor.execute("INSERT INTO sales (customer_id) VALUES (%s)",(customer_id,))
    sale_id = cursor.lastrowid #prendo l'ID della vendita appena creata

    #Inserisco i dettagli della vendita
    cursor.execute("INSERT INTO sale_items (sales_id,book_id,qty,price) VALUES (%s,%s,%s,%s)",(sale_id,book_id,qty,risultati['price'],))
    # Aggiorno lo stock
    new_stock = risultati["copies"] - qty
    cursor.execute("UPDATE stock SET copies = %s WHERE book_id = %s", (new_stock, book_id))

    conn.commit()
    print(f"\n Acquisto completato! Vendita n° {sale_id}.")
    print(f"Stock aggiornato: {new_stock} copie rimaste.")

#------------------------------------------------------------------------------
def make_purchase_for_customer(customer_id):
    cursor = conn.cursor(dictionary=True)

    # Mostra i libri disponibili
    print("\nLibri disponibili:")
    cursor.execute("SELECT b.id, b.title, s.copies, b.price FROM books b JOIN stock s ON b.id = s.book_id")
    books = cursor.fetchall()
    print(tabulate(books, headers="keys", tablefmt="grid"))

    # Scelta libro e quantità
    book_id = safe_int("Inserisci l'ID del libro da acquistare: ", min_value=1)
    qty = safe_int("Quante copie vuoi acquistare? ", min_value=1)

    # Controllo disponibilità
    cursor.execute("SELECT copies, price FROM stock s JOIN books b ON s.book_id = b.id WHERE book_id = %s", (book_id,))
    risultati = cursor.fetchone()

    if not risultati:
        print(" Libro non trovato.")
        return
    if risultati["copies"] < qty:
        print(f" Solo {risultati['copies']} copie disponibili.")
        return

    # Inserisce la vendita
    cursor.execute("INSERT INTO sales (customer_id) VALUES (%s)", (customer_id,))
    sale_id = cursor.lastrowid

    # Inserisce dettaglio vendita
    cursor.execute(
        "INSERT INTO sale_items (sales_id, book_id, qty, price) VALUES (%s, %s, %s, %s)",
        (sale_id, book_id, qty, risultati["price"])
    )

    # Aggiorna stock
    new_stock = risultati["copies"] - qty
    cursor.execute("UPDATE stock SET copies = %s WHERE book_id = %s", (new_stock, book_id))
    conn.commit()

    print(f"\n Acquisto completato! Vendita n° {sale_id}.")
    print(f"Stock aggiornato: {new_stock} copie rimaste.")


#------------------------------------------------------------------------------------
#Funzione per acquistare da un cliente non registrato
def add_customer_and_purchase():
    cursor = conn.cursor()
    print("\n--- Inserimento nuovo cliente ---")

    # Dati anagrafici del cliente
    fname = safe_input("Nome: ")
    lname = safe_input("Cognome: ")
    email = input("Email: ")
    phone = input("Telefono: ")
    street = input("Indirizzo: ")
    city = input("Città: ")
    postal_code = input("Codice postale: ")
    country = input("Paese: ")

    try:
        # Inserisce il cliente
        cursor.execute(
            "INSERT INTO customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)",
            (fname, lname, email, phone)
        )
        customer_id = cursor.lastrowid

        # Inserisce l'indirizzo
        cursor.execute(
            "INSERT INTO addresses (customer_id, street, city, postal_code, country) VALUES (%s, %s, %s, %s, %s)",
            (customer_id, street, city, postal_code, country)
        )

        conn.commit()
        print(f"\n Cliente aggiunto con ID {customer_id}!")

        # Subito dopo l’inserimento, parte l’acquisto
        make_purchase_for_customer(customer_id)

    except mysql.connector.Error as e:
        print(f"Errore durante l'inserimento del cliente: {e}")
        conn.rollback()




#----------------------------------------------------------------------------------------------------------

#Menù per le diverse funzionalità
#Menù Principale:
def main_menu():
    while True:
        print("\n--------GESTIONE LIBRERIA---------")
        print("1) Gestione Clienti")
        print("2) Gestione Libri")
        print("3) Vendite e Statistiche")
        print("4) Processo di acquisto")
        print("0) Esci")

        scelta=safe_int("Scegli un'opzione: ",min_value=0,max_value=4)

        if scelta == 1:
            menu_clienti()
        elif scelta == 2:
            menu_libri()
        elif scelta == 3:
            menu_statistiche()
        elif scelta == 4:
            menu_acquisto()
        elif scelta == 0:
            print("\n Uscita dal programma. Arrivederci!")
            break


#Menù per la Gestione Clienti
def menu_clienti():
    while True:
        print("\n--------GESTIONE CLIENTI--------")
        print("1) Cerca un Cliente")
        print("2) Aggiungi un Cliente")
        print("0) Torna al menù principale")


        scelta=safe_int("\n Scegli un'opzione: ",min_value=0,max_value=2)


        if scelta == 1:
            search_customers()
        elif scelta == 2:
            add_customers()
        elif scelta == 0:
            break

#Menù Gestione Libri
def menu_libri():
    while True:
        print("\n---------GESTIONE LIBRI--------")
        print("1) Visualizza lista libri")
        print("2) Aggiungi libro")
        print("3) Modifica libro")
        print("4) Elimina libro")
        print("0) Torna al menù principale")

        scelta =safe_int("\n Scegli un'opzione: ",min_value=0,max_value=4)

        if scelta == 1:
            list_books()
        elif scelta == 2:
            add_book()
        elif scelta == 3:
            update_book()
        elif scelta == 4:
            delete_book()
        elif scelta == 0:
            break

#Menu Statistiche
def menu_statistiche():
    while True:
        print("\n --------GESTIONE STATISTICHE--------")
        print("1) Storico vendite ultime 24h")
        print("2) Storico vendite ultimi N giorni")
        print("3) Top 10 libri più venduti")
        print("0) Torna al menù principale")


        scelta = safe_int("\n Scegli un'opzione: ",min_value=0,max_value=3)

        if scelta == 1:
            sales_last_day()
        elif scelta == 2:
            sales_last_days()
        elif scelta == 3:
            top_10_book()
        elif scelta == 0:
            break

#Menù per acquistare
def menu_acquisto():
    while True:
        print("\n -------GESTIONE ACQUISTI-------")
        print("1) Cliente già registrato ")
        print("2) Nuovo cliente + acquisto")
        print("0) Torna al menù principale")


        scelta = safe_int("Scegli un'opzione: ",min_value=0,max_value=2)

        if scelta == 1:
            make_purchase()
        elif scelta == 2:
            add_customer_and_purchase()
        elif scelta == 0:
            break

    conn.close()

if __name__ == "__main__":
    main_menu()

""" Commento personale: Ho provato a gestire gli errori tramite funzioni definite all'inizio del codice in modo da evitare la ripetitività 
di try/except. Per l'acquisto da parte di un cliente già registrato e uno non ancora inserito, probabilmente avrei potuto scrivere meno funzioni..
magari mettendo insieme "make_purchase" e "make_purchase_for_customer" ma non sono riuscita a trovare una soluzione soddisfacente.
Nella realizzazione di tabelle in MariaDB ho utilizzato chiavi esterne (Foreign Key) per collegare le varie tabelle logicamente, nelle varie query 
dunque ho utilizzato JOIN e non JOIN INNER o JOIN OUTER. Spero sia lo stesso."""















    

















