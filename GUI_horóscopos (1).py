import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import csv

# Diccionario de horóscopos básicos
horoscopos = {
    "Aries": "Tendrás energía renovada. Confía en tus decisiones.",
    "Tauro": "Buen momento para asuntos financieros. Sé paciente.",
    "Géminis": "Habrá sorpresas, mantente flexible y curioso.",
    "Cáncer": "El hogar será tu refugio. Cuida tus emociones.",
    "Leo": "Tu liderazgo brilla. Oportunidades en lo profesional.",
    "Virgo": "Organiza tus ideas. Día productivo.",
    "Libra": "Equilibra tu vida personal y profesional.",
    "Escorpio": "Intuición elevada. Escucha tu voz interior.",
    "Sagitario": "Aventura y nuevos aprendizajes están cerca.",
    "Capricornio": "Esfuerzo recompensado. Mantén el enfoque.",
    "Acuario": "Innovación. Hoy tus ideas impactarán.",
    "Piscis": "Conexiones emocionales importantes. Sé sincero.",
}

# Función para obtener signo zodiacal
def obtener_signo(dia, mes):
    signos = [
        (20, "Capricornio"), (19, "Acuario"), (20, "Piscis"),
        (20, "Aries"), (21, "Tauro"), (21, "Géminis"),
        (23, "Cáncer"), (23, "Leo"), (23, "Virgo"),
        (23, "Libra"), (22, "Escorpio"), (22, "Sagitario"), (31, "Capricornio")
    ]
    if dia > signos[mes - 1][0]:
        return signos[mes][1]
    else:
        return signos[mes - 1][1]

# Función principal
def generar_horoscopo():
    nombre = entry_nombre.get()
    fecha_str = entry_fecha.get()

    try:
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha inválido. Usa dd/mm/yyyy.")
        return

    signo = obtener_signo(fecha.day, fecha.month)
    horoscopo = horoscopos[signo]

    # Mostrar en la interfaz
    resultado.set(f"{nombre}, tu signo es {signo}.\nHoróscopo: {horoscopo}")

    # Guardar en archivo
    with open("registros_horoscopo.csv", "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, fecha_str, signo, horoscopo])

    messagebox.showinfo("Guardado", "Tus datos han sido registrados.")

# Interfaz gráfica
root = tk.Tk()
root.title("Lectura de Horóscopos")
root.geometry("400x300")

ttk.Label(root, text="Nombre:").pack(pady=5)
entry_nombre = ttk.Entry(root, width=40)
entry_nombre.pack()

ttk.Label(root, text="Fecha de nacimiento (dd/mm/yyyy):").pack(pady=5)
entry_fecha = ttk.Entry(root, width=40)
entry_fecha.pack()

ttk.Button(root, text="Obtener horóscopo", command=generar_horoscopo).pack(pady=10)

resultado = tk.StringVar()
ttk.Label(root, textvariable=resultado, wraplength=350, justify="center").pack(pady=10)

root.mainloop()
