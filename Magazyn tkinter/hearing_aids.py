import sqlite3
from tkinter import *
from tkinter import messagebox
from resources.phonak import *
from resources.oticon import *
from resources.signia import *
from resources.sonic import *
from resources.philips import *
from resources.interton import *
from resources.companies import producenci

root = Tk()
root.title('Magazyn Slaska KA-MED')
root.geometry("400x400")

#sprawdzenie nazwy kolumn w bazie
#def xxx():
#    connection = sqlite3.connect('baza_slaska.db')
#    cursor = connection.execute('select * from Baza')
#    names = list(map(lambda x: x[0], cursor.description))
#    connection.close()
#    print(names)

def add():
    conn = sqlite3.connect('baza_slaska.db')
    c = conn.cursor()
    '''
    c.execute("""CREATE TABLE Baza (
            producent text,
            model text,
            rodzaj text,
            poziom tech text,
            nr seryjny text
            )""")
    
    conn.commit()
    '''
    c.execute("""SELECT nr FROM Baza WHERE nr=?""", (sn.get(),))

    result = c.fetchone()
    if result:
        messagebox.showinfo("Informacja", "Aparat o takim numerze seryjnym znajduje się w bazie")
        conn.close()
    else:
        match c_producent.get():
            case "Phonak":
                match c_model_pho.get():
                    case "Audeo":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_audeo.get(),
                                    'techlvl': c_pho_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()

                    case "Bolero":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_bolero.get(),
                                    'techlvl': c_pho_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()

                    case "Naida":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_naida.get(),
                                    'techlvl': c_pho_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                        
                    case "Virto":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_virto.get(),
                                    'techlvl': c_pho_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Sky":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_bolero.get(),
                                    'techlvl': c_pho_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Vitus":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_vitus.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Vitus+":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_pho.get(),
                                    'rod': c_vituspl.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
            case "Oticon":
                match c_model_oti.get():
                    case "More":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_oti.get(),
                                    'rod': c_more.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Play PX":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_oti.get(),
                                    'rod': c_playpx.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Zicron":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_oti.get(),
                                    'rod': c_zicron.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Xceed":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_oti.get(),
                                    'rod': c_xceed.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Xceed Play":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_oti.get(),
                                    'rod': c_xceedplay.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
            case "Signia":
                match c_model_sig.get():
                    case "Pure":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_sig.get(),
                                    'rod': c_pure.get(),
                                    'techlvl': c_sig_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Motion":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_sig.get(),
                                    'rod': c_motion.get(),
                                    'techlvl': c_sig_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Styletto":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_sig.get(),
                                    'rod': c_styletto.get(),
                                    'techlvl': c_sig_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Silk":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_sig.get(),
                                    'rod': c_silk.get(),
                                    'techlvl': c_sig_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close() 
                    case "Active":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_sig.get(),
                                    'rod': c_active.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()  
                    case "Intuis 3":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_sig.get(),
                                    'rod': c_intuis3.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
            case "Sonic":
                match c_model_son.get():
                    case "Radiant":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_son.get(),
                                    'rod': c_radiant.get(),
                                    'techlvl': c_son_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Enchant SE":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_son.get(),
                                    'rod': c_enchantse.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "Trek":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_son.get(),
                                    'rod': c_trek.get(),
                                    'techlvl': "-",
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
            case "Philips":
                match c_model_phi.get():
                    case "HearLink XX30":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_phi.get(),
                                    'rod': c_hlxx30.get(),
                                    'techlvl': c_phi_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "HearLink XX10":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_phi.get(),
                                    'rod': c_hlxx10.get(),
                                    'techlvl': c_phi_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
                    case "HearLink XX00":
                        c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_phi.get(),
                                    'rod': c_hlxx00.get(),
                                    'techlvl': c_phi_klasy.get(),
                                    'sn': sn.get()
                                })
                        try:
                            conn.commit()
                            sn.delete(0, END)
                            messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                        except:
                            messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                        conn.close()
            case "Interton":
                match c_model_int.get():
                    case "Move":
                        match c_int_klasy.get():
                            case "6":
                                c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_int.get(),
                                    'rod': c_int_6.get(),
                                    'techlvl': c_int_klasy.get(),
                                    'sn': sn.get()
                                })
                                try:
                                    conn.commit()
                                    sn.delete(0, END)
                                    messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                                except:
                                    messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                                conn.close()
                            case "4":
                                c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_int.get(),
                                    'rod': c_int_4.get(),
                                    'techlvl': c_int_klasy.get(),
                                    'sn': sn.get()
                                })
                                try:
                                    conn.commit()
                                    sn.delete(0, END)
                                    messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                                except:
                                    messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                                conn.close()
                            case "3":
                                c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_int.get(),
                                    'rod': c_int_3.get(),
                                    'techlvl': c_int_klasy.get(),
                                    'sn': sn.get()
                                })
                                try:
                                    conn.commit()
                                    sn.delete(0, END)
                                    messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                                except:
                                    messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                                conn.close()
                            case "2":
                                c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_int.get(),
                                    'rod': c_int_2.get(),
                                    'techlvl': c_int_klasy.get(),
                                    'sn': sn.get()
                                })
                                try:
                                    conn.commit()
                                    sn.delete(0, END)
                                    messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                                except:
                                    messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                                conn.close()
                            case "1":
                                c.execute("INSERT INTO Baza VALUES(:prod, :mod, :rod, :techlvl, :sn)",
                                {
                                    'prod': c_producent.get(),
                                    'mod': c_model_int.get(),
                                    'rod': c_int_1.get(),
                                    'techlvl': c_int_klasy.get(),
                                    'sn': sn.get()
                                })
                                try:
                                    conn.commit()
                                    sn.delete(0, END)
                                    messagebox.showinfo("Dodawanie do bazy danych", "Aparat został dodany do bazy")
                                except:
                                    messagebox.showinfo("Błąd", "Nieudane dodanie aparatu do bazy")
                                conn.close()
def query():
    conn = sqlite3.connect('baza_slaska.db')
    c = conn.cursor()

    c.execute("SELECT * FROM Baza")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    conn.commit()

    conn.close()

def delete():
    conn = sqlite3.connect('baza_slaska.db')
    c = conn.cursor()
    c.execute("""SELECT nr FROM Baza WHERE nr=?""", (sn.get(),))

    result = c.fetchone()
    if result:
        c.execute("DELETE from Baza WHERE nr = " + sn.get())    
        conn.commit()
        sn.delete(0, END)
        messagebox.showinfo("Usuwanie z bazy danych", "Aparat został usuniety z bazy")
    else:
        messagebox.showinfo("UWAGA!", "Aparatu o takim nr seryjnym nie ma w bazie danych.")
    conn.close()

def new():
    for child in root.winfo_children():
        child.destroy()

def check():
    conn = sqlite3.connect('baza_slaska.db')
    c = conn.cursor()
    c.execute("""SELECT nr FROM Baza WHERE nr=?""", (sn.get(),))

    result = c.fetchone()
    if result:
        messagebox.showinfo("Informacja", "Aparat znajduje się w bazie")
    else:
        messagebox.showinfo("Informacja", "Aparatu nie ma w bazie")
    
    conn.commit()
    conn.close()
    
wyb_rodzaj = Label(root, text="Wybierz rodzaj aparatu")
wyb_poziom = Label(root, text="Wybierz poziom technologiczny")
wpr_sn = Label(root, text="Wprowadz numer seryjny")

def SN(xc):
    global sn
    sn = Entry(root)
    wpr_sn.grid(row=4, column=0)
    sn.grid(row=4, column=1)

    dodaj_ha = Button(root, text="Dodaj do bazy", command=add)
    dodaj_ha.grid(row=5, column=0)

    usun = Button(root, text="Usuń z bazy", command=delete)
    usun.grid(row=5, column=1)

    spr_czy_jest = Button(root, text="Sprawdz czy aparat jest w bazie", command=check)
    spr_czy_jest.grid(row=6, column=0, columnspan=2)

    zawartosc = Button(root, text="Pokaz co jest w bazie", command=query)
    zawartosc.grid(row=7, column=0,)

    nowy_aparat = Button(root, text="Dodaj inny aparat", command=new)
    nowy_aparat.grid(row=7, column=1)

def wybor_prod(xc):
    match xc:
        case "Phonak":
            def wybor_pho_model(xc):
                match xc:
                    case "Audeo":
                        global pho_audeo
                        global c_audeo
                        c_audeo = StringVar()
                        pho_audeo = OptionMenu(root, c_audeo, *phonak_audeo)
                        wyb_poziom.grid(row=2, column=0)
                        pho_audeo.grid(row=2, column=1)

                        global c_pho_klasy
                        c_pho_klasy = StringVar()
                        pho_klasy = OptionMenu(root, c_pho_klasy, command=SN, *phonak_klasy)
                        pho_klasy.grid(row=3, column=1)
                    case "Bolero":
                        global c_bolero
                        c_bolero = StringVar()
                        pho_bolero = OptionMenu(root, c_bolero, *phonak_bolero)
                        wyb_poziom.grid(row=2, column=0)
                        pho_bolero.grid(row=2, column=1)

                        c_pho_klasy = StringVar()
                        pho_klasy = OptionMenu(root, c_pho_klasy, command=SN, *phonak_klasy)
                        pho_klasy.grid(row=3, column=1)
                    case "Naida":
                        global c_naida
                        c_naida = StringVar()
                        pho_naida = OptionMenu(root, c_naida, *phonak_naida)
                        wyb_poziom.grid(row=2, column=0)
                        pho_naida.grid(row=2, column=1)

                        c_pho_klasy = StringVar()
                        pho_klasy = OptionMenu(root, c_pho_klasy, command=SN, *phonak_klasy)
                        pho_klasy.grid(row=3, column=1)
                    case "Virto":
                        global c_virto
                        c_virto = StringVar()
                        pho_virto = OptionMenu(root, c_virto, *phonak_virto)
                        wyb_poziom.grid(row=2, column=0)
                        pho_virto.grid(row=2, column=1)

                        c_pho_klasy = StringVar()
                        pho_klasy = OptionMenu(root, c_pho_klasy, command=SN, *phonak_klasy)
                        pho_klasy.grid(row=3, column=1)
                    case "Sky":
                        global c_sky
                        c_sky = StringVar()
                        pho_sky = OptionMenu(root, c_sky, *phonak_sky)
                        wyb_poziom.grid(row=2, column=0)
                        pho_sky.grid(row=2, column=1)

                        c_pho_klasy = StringVar()
                        pho_klasy = OptionMenu(root, c_pho_klasy, command=SN, *phonak_klasy)
                        pho_klasy.grid(row=3, column=1)
                    case "Vitus+":
                        global c_vituspl
                        c_vituspl = StringVar()
                        pho_vituspl = OptionMenu(root, c_vituspl, command=SN, *phonak_vituspl)
                        wyb_poziom.grid(row=2, column=0)
                        pho_vituspl.grid(row=2, column=1)
                    case "Vitus":
                        global c_vitus
                        c_vitus = StringVar()
                        pho_vitus = OptionMenu(root, c_vitus, command=SN, *phonak_vitus)
                        wyb_poziom.grid(row=2, column=0)
                        pho_vitus.grid(row=2, column=1)

            global c_model_pho
            c_model_pho = StringVar()
            pho_model = OptionMenu(root, c_model_pho, command=wybor_pho_model, *phonak_model)
            wyb_rodzaj.grid(row=1, column=0)
            pho_model.grid(row=1, column=1)
        case "Oticon":
            def wybor_oti_model(xc):
                match xc:
                    case "More":
                        global c_more
                        c_more = StringVar()
                        oti_more = OptionMenu(root, c_more, command=SN, *oticon_more)
                        wyb_poziom.grid(row=2, column=0)
                        oti_more.grid(row=2, column=1)
                    case "Play PX":
                        global c_playpx
                        c_playpx = StringVar()
                        oti_playpx = OptionMenu(root, c_playpx, command=SN, *oticon_playpx)
                        wyb_poziom.grid(row=2, column=0)
                        oti_playpx.grid(row=2, column=1)
                    case "Zicron":
                        global c_zicron
                        c_zicron = StringVar()
                        oti_zicron = OptionMenu(root, c_zicron, command=SN, *oticon_zicron)
                        wyb_poziom.grid(row=2, column=0)
                        oti_zicron.grid(row=2, column=1)
                    case "Xceed":
                        global c_xceed
                        c_xceed = StringVar()
                        oti_xceed = OptionMenu(root, c_xceed, command=SN, *oticon_xceed)
                        wyb_poziom.grid(row=2, column=0)
                        oti_xceed.grid(row=2, column=1)
                    case "Xceed Play":
                        global c_xceedplay
                        c_xceedplay = StringVar()
                        oti_xceedplay = OptionMenu(root, c_xceedplay, command=SN, *oticon_xceedplay)
                        wyb_poziom.grid(row=2, column=0)
                        oti_xceedplay.grid(row=2, column=1)
            global c_model_oti
            c_model_oti = StringVar()
            oti_model = OptionMenu(root, c_model_oti, command=wybor_oti_model, *oticon_model)
            wyb_rodzaj.grid(row=1, column=0)
            oti_model.grid(row=1, column=1)
        case "Signia":
            def wybor_sig_model(xc):
                match xc:
                    case "Pure":
                        global c_pure
                        c_pure = StringVar()
                        sig_pure = OptionMenu(root, c_pure, *signia_pure)
                        wyb_poziom.grid(row=2, column=0)
                        sig_pure.grid(row=2, column=1)

                        global c_sig_klasy
                        c_sig_klasy = StringVar()
                        sig_klasy = OptionMenu(root, c_sig_klasy, command=SN, *signia_klasy)
                        sig_klasy.grid(row=3, column=1)
                    case "Motion":
                        global c_motion
                        c_motion = StringVar()
                        sig_motion = OptionMenu(root, c_motion, *signia_motion)
                        wyb_poziom.grid(row=2, column=0)
                        sig_motion.grid(row=2, column=1)

                        c_sig_klasy = StringVar()
                        sig_klasy = OptionMenu(root, c_sig_klasy, command=SN, *signia_klasy)
                        sig_klasy.grid(row=3, column=1)
                    case "Styletto":
                        global c_styletto
                        c_styletto = StringVar()
                        sig_styletto = OptionMenu(root, c_styletto, *signia_styletto)
                        wyb_poziom.grid(row=2, column=0)
                        sig_styletto.grid(row=2, column=1)

                        c_sig_klasy = StringVar()
                        sig_klasy = OptionMenu(root, c_sig_klasy, command=SN, *signia_klasy)
                        sig_klasy.grid(row=3, column=1)
                    case "Silk":
                        global c_silk
                        c_silk = StringVar()
                        sig_silk = OptionMenu(root, c_silk, *signia_silk)
                        wyb_poziom.grid(row=2, column=0)
                        sig_silk.grid(row=2, column=1)

                        c_sig_klasy = StringVar()
                        sig_klasy = OptionMenu(root, c_sig_klasy, command=SN, *signia_klasy)
                        sig_klasy.grid(row=3, column=1)
                    case "Active":
                        global c_active
                        c_active = StringVar()
                        sig_active = OptionMenu(root, c_active, command=SN, *signia_active)
                        wyb_poziom.grid(row=2, column=0)
                        sig_active.grid(row=2, column=1)
                    case "Intuis 3":
                        global c_intuis3
                        c_intuis3 = StringVar()
                        sig_intuis3 = OptionMenu(root, c_intuis3, command=SN, *signia_intuis3)
                        wyb_poziom.grid(row=2, column=0)
                        sig_intuis3.grid(row=2, column=1)

            global c_model_sig
            c_model_sig = StringVar()
            sig_model = OptionMenu(root, c_model_sig, command=wybor_sig_model, *signia_model)
            wyb_rodzaj.grid(row=1, column=0)
            sig_model.grid(row=1, column=1)
        case "Sonic":
            def wybor_son_model(xc):
                match xc:
                    case "Radiant":
                        global c_radiant
                        c_radiant = StringVar()
                        son_radiant = OptionMenu(root, c_radiant, *sonic_radiant)
                        wyb_poziom.grid(row=2, column=0)
                        son_radiant.grid(row=2, column=1)

                        global c_son_klasy
                        c_son_klasy = StringVar()
                        son_klasy = OptionMenu(root, c_son_klasy, command=SN, *sonic_klasy)
                        son_klasy.grid(row=3, column=1)
                    case "Enchant SE":
                        global c_enchantse
                        c_enchantse = StringVar()
                        son_enchantse = OptionMenu(root, c_enchantse, command=SN, *sonic_enchantse)
                        wyb_poziom.grid(row=2, column=0)
                        son_enchantse.grid(row=2, column=1)
                    case "Trek":
                        global c_trek
                        c_trek = StringVar()
                        son_trek = OptionMenu(root, c_trek, command=SN, *sonic_trek)
                        wyb_poziom.grid(row=2, column=0)
                        son_trek.grid(row=2, column=1)
            global c_model_son
            c_model_son = StringVar()
            son_model = OptionMenu(root, c_model_son, command=wybor_son_model, *sonic_model)
            wyb_rodzaj.grid(row=1, column=0)
            son_model.grid(row=1, column=1)
        case "Philips":
            def wybor_phi_model(xc):
                match xc:
                    case "HearLink XX30":
                        global c_hlxx30
                        c_hlxx30 = StringVar()
                        phi_hlxx30 = OptionMenu(root, c_hlxx30, *philips_hlxx30)
                        wyb_poziom.grid(row=2, column=0)
                        phi_hlxx30.grid(row=2, column=1)

                        global c_phi_klasy
                        c_phi_klasy = StringVar()
                        phi_klasy = OptionMenu(root, c_phi_klasy, command=SN, *philips_klasy)
                        phi_klasy.grid(row=3, column=1)
                    case "HearLink XX10":
                        global c_hlxx10
                        c_hlxx10 = StringVar()
                        phi_hlxx10 = OptionMenu(root, c_hlxx10, *philips_hlxx10)
                        wyb_poziom.grid(row=2, column=0)
                        phi_hlxx10.grid(row=2, column=1)

                        c_phi_klasy = StringVar()
                        phi_klasy = OptionMenu(root, c_phi_klasy, command=SN, *philips_klasy)
                        phi_klasy.grid(row=3, column=1)
                    case "HearLink XX00":
                        global c_hlxx00
                        c_hlxx00 = StringVar()
                        phi_hlxx00 = OptionMenu(root, c_hlxx00, *philips_hlxx00)
                        wyb_poziom.grid(row=2, column=0)
                        phi_hlxx00.grid(row=2, column=1)

                        c_phi_klasy = StringVar()
                        phi_klasy = OptionMenu(root, c_phi_klasy, command=SN, *philips_klasy_xx00)
                        phi_klasy.grid(row=3, column=1)
            global c_model_phi
            c_model_phi = StringVar()
            phi_model = OptionMenu(root, c_model_phi, command=wybor_phi_model, *philips_model)
            wyb_rodzaj.grid(row=1, column=0)
            phi_model.grid(row=1, column=1)
        case "Interton":
            def wybor_int_model(xc):
                match xc:
                    case "Move":
                        def wybor_klasy(klasa):
                            match klasa:
                                case "6":
                                    global c_int_6
                                    c_int_6 = StringVar()
                                    int_6 = OptionMenu(root, c_int_6, command=SN, *interton_6)
                                    int_6.grid(row=3, column=1)
                                case "4":
                                    global c_int_4
                                    c_int_4 = StringVar()
                                    int_4 = OptionMenu(root, c_int_4, command=SN, *interton_4)
                                    int_4.grid(row=3, column=1)
                                case "3":
                                    global c_int_3
                                    c_int_3 = StringVar()
                                    int_3 = OptionMenu(root, c_int_3, command=SN, *interton_3)
                                    int_3.grid(row=3, column=1)
                                case "2":
                                    global c_int_2
                                    c_int_2 = StringVar()
                                    int_2 = OptionMenu(root, c_int_2, command=SN, *interton_2)
                                    int_2.grid(row=3, column=1)
                                case "1":
                                    global c_int_1
                                    c_int_1 = StringVar()
                                    int_1 = OptionMenu(root, c_int_1, command=SN, *interton_1)
                                    int_1.grid(row=3, column=1)
                        global c_int_klasy
                        c_int_klasy = StringVar()
                        int_klasy = OptionMenu(root, c_int_klasy, command=wybor_klasy, *interton_klasy)
                        wyb_poziom.grid(row=2, column=0)
                        int_klasy.grid(row=2, column=1)
            global c_model_int
            c_model_int = StringVar()
            int_model = OptionMenu(root, c_model_int, command=wybor_int_model, *interton_model)
            wyb_rodzaj.grid(row=1, column=0)
            int_model.grid(row=1, column=1)


c_producent = StringVar()
producent = OptionMenu(root, c_producent, command=wybor_prod, *producenci)
producent.grid(row=0, column=1)
wyb_prod = Label(root, text="Wybierz producenta")
wyb_prod.grid(row=0, column=0)

#down

root.mainloop()