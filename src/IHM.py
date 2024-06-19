import tkinter as tk
from tkinter import ttk, messagebox
import config.config as cfg

def validate_entries():
    valid = True
    for title, charge_entry in charges_entries.items():
        value = charge_entry.get().replace('.', '', 1)
        if not value.isdigit():
            valid = False
            messagebox.showerror("Erreur de validation", f"Les valeurs pour {title} doivent être des nombres.")
            break
        if title == "Communication" and not (0 <= float(charge_entry.get()) <= 1):
            valid = False
            messagebox.showerror("Erreur de validation", "La valeur pour Communication doit être un pourcentage entre 0 et 1.")
            break
    """
    if not initial_attendance_entry.get().replace('.', '', 1).isdigit():
        valid = False
        messagebox.showerror("Erreur de validation", "La fréquentation de départ doit être un nombre.")
    """
    if not attendance_entry.get().replace('.', '', 1).isdigit():
        valid = False
        messagebox.showerror("Erreur de validation", "La fréquentation du bar doit être un nombre.")
    if not ticket_entry.get().replace('.', '', 1).isdigit():
        valid = False
        messagebox.showerror("Erreur de validation", "Le ticket moyen doit être un nombre.")
    if not margin_entry.get().replace('.', '', 1).isdigit():
        valid = False
        messagebox.showerror("Erreur de validation", "La marge doit être un nombre.")
    return valid

def submit():
    if validate_entries():
        cfg.chargesExit = {title: entry.get() for title, entry in charges_entries.items()}
        sports_attendance = {
            "Five": initial_attendance_five_entry.get(),
            "Beach": initial_attendance_beach_entry.get(),
            "Padel": initial_attendance_padel_entry.get()
        }
        duration = duration_var.get()
        initial_attendance = initial_attendance_var.get()
        attendance = attendance_var.get()
        if attendance == "Linéaire":
            attendance_info = f"lineaire, tauxAugmentation: { float(linear_entry.get())}"
        else:
            attendance_info = f"creu, durée: { int(dip_duration_entry.get())}, tauxBaisse: { float(dip_rate_entry.get())}%"
        cfg.configExit = {
            "dureeSimu": duration,
            "freqInitFive": sports_attendance["Five"],
            "freqInitBeach": sports_attendance["Beach"],
            "freqInitPadel": sports_attendance["Padel"],
            "evoFreq": attendance_info,
            "freqBar":  int(attendance_entry.get()),
            "ticketMoyenBar": ticket_entry.get(),
            "margeBar": margin_entry.get()
        }
        messagebox.showinfo("Information", "\n".join([f"{key}: {value}" for key, value in cfg.configExit.items()]))
        app.quit()
        app.destroy()


def show_information():
    messagebox.showinfo("Information", "La fréquentation du bar est le pourcentage de la capacité du bar utilisée en moyenne.\nPar exemple, si votre bar a une capacité de 100 personnes et qu'il est en moyenne rempli à 80%, la fréquentation du bar est de 80%.")

app = tk.Tk()
app.title("Simulation Financière")

# Fréquentation de départ
tk.Label(app, text="Fréquentation de départ (Five)(%):").grid(row=0, column=0, padx=10, pady=10)
initial_attendance_var = tk.StringVar()
initial_attendance_five_entry = tk.Entry(app, textvariable=initial_attendance_var)
initial_attendance_five_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Fréquentation de départ (Beach)(%):").grid(row=1, column=0, padx=10, pady=10)
initial_attendance_var = tk.StringVar()
initial_attendance_beach_entry = tk.Entry(app, textvariable=initial_attendance_var)
initial_attendance_beach_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Fréquentation de départ (Padel)(%):").grid(row=2, column=0, padx=10, pady=10)
initial_attendance_var = tk.StringVar()
initial_attendance_padel_entry = tk.Entry(app, textvariable=initial_attendance_var)
initial_attendance_padel_entry.grid(row=2, column=1, padx=10, pady=10)

# Durée de la simulation
tk.Label(app, text="Durée de la simulation:").grid(row=3, column=0, padx=10, pady=10)
duration_var = tk.StringVar()
duration_combobox = ttk.Combobox(app, textvariable=duration_var)
duration_combobox['values'] = ("Trimestre", "Semestre", "Annee", "3 ans")
duration_combobox.grid(row=3, column=1, padx=10, pady=10)

# Évolution de la fréquentation
tk.Label(app, text="Évolution de la fréquentation:").grid(row=4, column=0, padx=10, pady=10)
attendance_var = tk.StringVar()
attendance_combobox = ttk.Combobox(app, textvariable=attendance_var)
attendance_combobox['values'] = ("Linéaire", "Avec creu")
attendance_combobox.grid(row=4, column=1, padx=10, pady=10)

# Linéaire: Taux d'augmentation
linear_label = tk.Label(app, text="Taux d'augmentation (%):")
linear_entry = tk.Entry(app)
# Avec creu: Durée du creu et Taux de baisse
dip_duration_label = tk.Label(app, text="Durée du creu (mois):")
dip_duration_entry = tk.Entry(app)
dip_rate_label = tk.Label(app, text="Taux de baisse (%):")
dip_rate_entry = tk.Entry(app)

# Fonction pour afficher les champs correspondant au choix de l'évolution de la fréquentation
def show_hide_fields(*args):
    if attendance_var.get() == "Linéaire":
        linear_label.grid(row=5, column=0, padx=10, pady=10)
        linear_entry.grid(row=5, column=1, padx=10, pady=10)
        dip_duration_label.grid_forget()
        dip_duration_entry.grid_forget()
        dip_rate_label.grid_forget()
        dip_rate_entry.grid_forget()
    else:
        linear_label.grid_forget()
        linear_entry.grid_forget()
        dip_duration_label.grid(row=5, column=0, padx=10, pady=10)
        dip_duration_entry.grid(row=5, column=1, padx=10, pady=10)
        dip_rate_label.grid(row=6, column=0, padx=10, pady=10)
        dip_rate_entry.grid(row=6, column=1, padx=10, pady=10)

# Appel de la fonction au changement de sélection
attendance_var.trace_add("write", show_hide_fields)

# Charges
tk.Label(app, text="Charges:").grid(row=7, column=0, padx=10, pady=10)

charges_entries = {}
for i, (title, value) in enumerate(cfg.charges.items()):
    tk.Label(app, text=title).grid(row=i+8, column=0, padx=10, pady=10)
    charge_entry = tk.Entry(app)
    charge_entry.insert(0, value)
    charge_entry.grid(row=i+8, column=1, padx=10, pady=10)
    charges_entries[title] = charge_entry

# Bar
tk.Label(app, text="Bar").grid(row=1, column=2, padx=10, pady=10)
attendance_bar_label = tk.Label(app, text="Fréquentation du bar (%):")
attendance_bar_label.grid(row=2, column=2, padx=10, pady=10)
attendance_entry = tk.Entry(app)
attendance_entry.grid(row=2, column=3, padx=10, pady=10)
info_button = tk.Button(app, text="Information", command=show_information)
info_button.grid(row=2, column=4, padx=10, pady=10)
ticket_label = tk.Label(app, text="Ticket moyen (€):")
ticket_label.grid(row=3, column=2, padx=10, pady=10)
ticket_entry = tk.Entry(app)
ticket_entry.grid(row=3, column=3, padx=10, pady=10)
margin_label = tk.Label(app, text="Marge (%):")
margin_label.grid(row=4, column=2, padx=10, pady=10)
margin_entry = tk.Entry(app)
margin_entry.grid(row=4, column=3, padx=10, pady=10)

# Bouton de soumission
submit_button = tk.Button(app, text="Soumettre", command=submit)
submit_button.grid(row=11, column=2, columnspan=2, pady=20)

# Initialiser l'affichage des champs correspondant au choix actuel
show_hide_fields()

app.mainloop()

