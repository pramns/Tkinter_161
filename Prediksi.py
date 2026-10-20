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