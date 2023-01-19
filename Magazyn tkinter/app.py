from tkinter import *
from tkinter import messagebox


main = Tk()
main.title('Magazyn Slaska KA-MED')
main.geometry("400x400")

def import_ha():
    main.destroy()
    import hearing_aids

def import_haacc():
    main.destroy()
    import resources.ha_accessories

def import_acc():
    return
    #main.destroy()
    #import

ha_button = Button(main, text="Aparaty", command=import_ha)
ha_button.grid(row=0, column=0)

ha_acc_button = Button(main, text="Akcesoria do aparatów", command=import_haacc)
ha_acc_button.grid(row=0, column=1)

acc_button = Button(main, text="Pozostałe akcesoria")#, command=import_acc)
acc_button.grid(row=0, column=2)



main.mainloop()