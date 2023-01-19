import sqlite3
from tkinter import *
from tkinter import messagebox
from resources.companies import producenci
from resources.phonak import phonak_chargers, phonak_roger, phonak_acc
from resources.oticon import oticon_chargers, oticon_acc
from resources.signia import signia_chargers, signia_acc
from resources.sonic import sonic_chargers, sonic_acc
from resources.philips import philips_chargers, philips_acc
from resources.interton import interton_acc

root2 = Tk()
root2.title('Magazyn Slaska KA-MED')
root2.geometry("400x400")

def add():
    conn = sqlite3.connect('akcesoria_do_aparatu.db')
    c = conn.cursor()
    '''
    c.execute("""CREATE TABLE Akcesoria_do_aparatu (
            producent text,
            akcesorium text,
            model text,
            nr  text
            )""")
    
    conn.commit()
    '''
    c.execute("""SELECT nr FROM Akcesoria_do_aparatu WHERE nr=?""", (sn.get(),))

    result = c.fetchone()
    if result:
        messagebox.showinfo("Informacja", "Akcesorium o takim numerze seryjnym znajduje się w bazie")
        conn.close()
    else:
        match c_producent.get():
            case "Phonak":
                match c_haacc.get():
                    case "Ładowarka":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': c_haacc.get(),
                                    'mod': c_pho_char.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
                    case "Roger":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': c_haacc.get(),
                                    'mod': c_pho_roger.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
                    case "Pozostałe":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': "-",
                                    'mod': c_pho_acc.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
            case "Oticon":
                match c_haacc.get():
                    case "Ładowarka":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': c_haacc.get(),
                                    'mod': c_oti_char.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
                    case "Pozostałe":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': "-",
                                    'mod': c_oti_acc.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
            case "Signia":
                match c_haacc.get():
                    case "Ładowarka":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': c_haacc.get(),
                                    'mod': c_sig_char.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
                    case "Pozostałe":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': "-",
                                    'mod': c_sig_acc.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
            case "Sonic":
                match c_haacc.get():
                    case "Ładowarka":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': c_haacc.get(),
                                    'mod': c_son_char.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
                    case "Pozostałe":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': "-",
                                    'mod': c_son_acc.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
            case "Philips":
                match c_haacc.get():
                    case "Ładowarka":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': c_haacc.get(),
                                    'mod': c_phi_char.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
                    case "Pozostałe":
                        c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': "-",
                                    'mod': c_phi_acc.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                        conn.close()
            case "Interton":
                c.execute("INSERT INTO Baza VALUES(:prod, :akc, :mod, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'akc': "-",
                                    'mod': c_int_acc.get(),
                                    'sn': sn.get()
                                })
                try:
                    conn.commit()
                    sn.delete(0, END)
                    messagebox.showinfo("Dodawanie do bazy danych", "Apkcesorium zostało dodane do bazy")
                except:
                    messagebox.showinfo("Błąd", "Nieudane dodanie akcesorium do bazy")
                conn.close()

def delete():
    conn = sqlite3.connect('akcesoria_do_aparatu.db')
    c = conn.cursor()
    c.execute("""SELECT nr FROM Akcesoria_do_aparatu WHERE nr=?""", (sn.get(),))

    result = c.fetchone()
    if result:
        c.execute("DELETE from Akcesoria_do_aparatu WHERE nr = " + sn.get())    
        conn.commit()
        sn.delete(0, END)
        messagebox.showinfo("Usuwanie z bazy danych", "Akcesorium zostało usunięte z bazy")
    else:
        messagebox.showinfo("UWAGA!", "Akcesorium o takim nr seryjnym nie ma w bazie danych.")
    conn.close()

def check():
    conn = sqlite3.connect('akcesoria_do_aparatu.db')
    c = conn.cursor()
    c.execute("""SELECT nr FROM akcesoria_do_aparatu WHERE nr=?""", (sn.get(),))

    result = c.fetchone()
    if result:
        messagebox.showinfo("Informacja", "Akcesorium znajduje się w bazie")
    else:
        messagebox.showinfo("Informacja", "Akcesorium nie ma w bazie")
    
    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('akcesoria_do_aparatu.db')
    c = conn.cursor()

    c.execute("SELECT * FROM akcesoria_do_aparatu.db")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root2, text=print_records)
    query_label.grid(row=7, column=0, columnspan=2)
    conn.commit()

    conn.close()

def new():
    for child in root2.winfo_children():
        child.destroy()


def SN(xc):
    global sn
    sn = Entry(root2)
    wpr_sn = Label(root2, text="Wprowadz numer seryjny")
    wpr_sn.grid(row=3, column=0)
    sn.grid(row=3, column=1)

    dodaj_acc = Button(root2, text="Dodaj do bazy", command=add)
    dodaj_acc.grid(row=4, column=0)

    usun = Button(root2, text="Usuń z bazy", command=delete)
    usun.grid(row=4, column=1)

    spr_czy_jest = Button(root2, text="Sprawdz czy produkt jest w bazie", command=check)
    spr_czy_jest.grid(row=5, column=0, columnspan=2)

    zawartosc = Button(root2, text="Pokaz co jest w bazie", command=query)
    zawartosc.grid(row=6, column=0,)

    nowy_aparat = Button(root2, text="Dodaj inny sprzęt", command=new)
    nowy_aparat.grid(row=6, column=1)

choise_acc = Label(root2, text="Wybierz akcesorium")
choise_model = Label(root2, text="Wybierz model")

def wybor_prod(xc):
    match xc:
        case "Phonak":
            def which_haacc(xc):
                match xc:
                    case "Ładowarka":
                        global c_pho_char
                        c_pho_char = StringVar()
                        pho_char = OptionMenu(root2, c_pho_char, command=SN, *phonak_chargers)
                        pho_char.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
                    case "Roger":
                        global c_pho_roger
                        c_pho_roger = StringVar()
                        pho_roger = OptionMenu(root2, c_pho_roger, command=SN, *phonak_roger)
                        pho_roger.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
                    case "Pozostałe":
                        global c_pho_acc
                        c_pho_acc = StringVar()
                        pho_acc = OptionMenu(root2, c_pho_acc, command=SN, *phonak_acc)
                        pho_acc.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
            global c_haacc
            c_haacc = StringVar()
            haacc = OptionMenu(root2, c_haacc, command=which_haacc, *['Ładowarka', 'Roger', 'Pozostałe'])
            choise_acc.grid(row=1, column=0)
            haacc.grid(row=1, column=1)
        case "Oticon":
            def which_haacc(xc):
                match xc:
                    case "Ładowarka":
                        global c_oti_char
                        c_oti_char = StringVar()
                        oti_char = OptionMenu(root2, c_oti_char, command=SN, *oticon_chargers)
                        oti_char.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
                    case "Pozostałe":
                        global c_oti_acc
                        c_oti_acc = StringVar()
                        oti_acc = OptionMenu(root2, c_oti_acc, command=SN, *oticon_acc)
                        oti_acc.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
            c_haacc = StringVar()
            haacc = OptionMenu(root2, c_haacc, command=which_haacc, *['Ładowarka', 'Pozostałe'])
            choise_acc.grid(row=1, column=0)
            haacc.grid(row=1, column=1)
        case "Signia":
            def which_haacc(xc):
                match xc:
                    case "Ładowarka":
                        global c_sig_char
                        c_sig_char = StringVar()
                        sig_char = OptionMenu(root2, c_sig_char, command=SN, *signia_chargers)
                        sig_char.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
                    case "Pozostałe":
                        global c_sig_acc
                        c_sig_acc = StringVar()
                        sig_acc = OptionMenu(root2, c_sig_acc, command=SN, *signia_acc)
                        sig_acc.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
            c_haacc = StringVar()
            haacc = OptionMenu(root2, c_haacc, command=which_haacc, *['Ładowarka', 'Pozostałe'])
            choise_acc.grid(row=1, column=0)
            haacc.grid(row=1, column=1)
        case "Sonic":
            def which_haacc(xc):
                match xc:
                    case "Ładowarka":
                        global c_son_char
                        c_son_char = StringVar()
                        son_char = OptionMenu(root2, c_son_char, command=SN, *sonic_chargers)
                        son_char.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
                    case "Pozostałe":
                        global c_son_acc
                        c_son_acc = StringVar()
                        son_acc = OptionMenu(root2, c_son_acc, command=SN, *sonic_acc)
                        son_acc.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
            c_haacc = StringVar()
            haacc = OptionMenu(root2, c_haacc, command=which_haacc, *['Ładowarka', 'Pozostałe'])
            choise_acc.grid(row=1, column=0)
            haacc.grid(row=1, column=1)
        case "Philips":
            def which_haacc(xc):
                match xc:
                    case "Ładowarka":
                        global c_phi_char
                        c_phi_char = StringVar()
                        phi_char = OptionMenu(root2, c_phi_char, command=SN, *philips_chargers)
                        phi_char.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
                    case "Pozostałe":
                        global c_phi_acc
                        c_phi_acc = StringVar()
                        phi_acc = OptionMenu(root2, c_phi_acc, command=SN, *philips_acc)
                        phi_acc.grid(row=2, column=1)
                        choise_model.grid(row=2, column=0)
            c_haacc = StringVar()
            haacc = OptionMenu(root2, c_haacc, command=which_haacc, *['Ładowarka', 'Pozostałe'])
            choise_acc.grid(row=1, column=0)
            haacc.grid(row=1, column=1)
        case "Interton":
            global c_int_acc
            c_int_acc = StringVar()
            int_acc = OptionMenu(root2, c_int_acc, command=SN, *interton_acc)
            int_acc.grid(row=1, column=1)
            choise_model.grid(row=1, column=0)
c_producent = StringVar()
producent = OptionMenu(root2, c_producent, command=wybor_prod, *producenci)
producent.grid(row=0, column=1)
wyb_prod = Label(root2, text="Wybierz producenta")
wyb_prod.grid(row=0, column=0)



root2.mainloop()