import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("430x650")
root.resizable(False, False)

WARNA_BG = "#1e2138"
WARNA_TEKS = "#ffffff"
WARNA_ENTRY = "#2f3350"
WARNA_AKSEN = "#7be0d6"
root.configure(bg=WARNA_BG)   

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),   # ukuran 16, tebal
    bg=WARNA_BG,
    fg=WARNA_TEKS
)
label_judul.grid(row=0, column=0, columnspan=2, pady=(25, 20))

daftar_entry = [] 
for i in range(10):
    nomor = i + 1  
    label_nilai = tk.Label(
        root,
        text=f"Nilai Mata Pelajaran {nomor}:",
        font=("Arial", 10, "bold"),
        bg=WARNA_BG,
        fg=WARNA_TEKS,
        anchor="e"               
    )
    label_nilai.grid(row=nomor, column=0, sticky="e", padx=(30, 10), pady=4)
    entry_nilai = tk.Entry(
        root,
        width=8,
        font=("Arial", 10),
        justify="center",
        bg=WARNA_ENTRY,
        fg=WARNA_TEKS,
        insertbackground=WARNA_TEKS,
        relief="flat",
        highlightthickness=1,
        highlightbackground="#4a4f73",
        highlightcolor=WARNA_AKSEN
    )
    entry_nilai.grid(row=nomor, column=1, sticky="w", pady=4)

    daftar_entry.append(entry_nilai) 

label_pilih = tk.Label(
    root,
    text="Pilih Jurusan Anda:",
    font=("Arial", 10, "bold"),
    bg=WARNA_BG,
    fg=WARNA_TEKS
)
label_pilih.grid(row=11, column=0, columnspan=2, pady=(25, 5))

daftar_jurusan = [
    "Teknologi Informasi",
    "Teknik Mesin",
    "Teknik Sipil",
    "Teknologi Elektro Medis",
    "Teknologi Rekayasa Otomotif",
    "Teknik Elektro",
    "Artificial Teknologi",
]

combo_jurusan = ttk.Combobox(
    root,
    values=daftar_jurusan,            
    state="readonly",                 
    width=28,                         
    height=7,                         
    justify="center",
    font=("Arial", 10)
)
combo_jurusan.current(0)              
combo_jurusan.grid(row=12, column=0, columnspan=2)

def hasil_prediksi():
    for entry in daftar_entry:
        entry.get()
    prodi = "Teknologi Informasi"
    label_hasil.config(text="Hasil Prediksi:\n" + prodi)
    
