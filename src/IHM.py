import tkinter as tk

#Create the main window
root = tk.Tk()
root.title("IHM")
root.geometry("500x500")

headerLabel=tk.Label(root,text="Main menu", fg="blue", font=("Helvetica", 16))
headerLabel.pack()


def evaluate():
    if(float(entry.get)<3):
        chaine.configure(text="C'est moooooort")
    else: 
        chaine.configure(text="ogggay")
#Create a writing box with a legend

label = tk.Label(root, text="Taux d'abonnement")
label.bind("<Return>",evaluate)
label.pack()
entry = tk.Entry(root)
entry.pack()

#close the window 
leaveButton= tk.Button(root, text="Quitter", command=root.destroy)
leaveButton.pack(padx=1,pady=3)
#display the main window
root.mainloop()
