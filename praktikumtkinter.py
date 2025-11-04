import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()   
top.title= ("aplikasi prediksi prodi pilihan")
top.geometry= ("400x800")
top.configure(bg="#a087eb")

entries = []

label = tk.Label(top, text=f"Aplikasi Prediksi", bg="white")
label.pack(side=tk.TOP, pady=3)

# Gunakan perulangan untuk membuat 10 input nilai
for i in range(1, 11):
    label = tk.Label(top, text=f"Masukkan Nilai {i}:", bg="green")
    label.pack(side=tk.TOP, pady=3)
    
    entry = tk.Entry(top, bd=5)
    entry.pack(side=tk.TOP, pady=3)
    
    entries.append(entry)  # simpan ke list untuk nanti digunakan

# Fungsi untuk menampilkan hasil
def tampilkanNama():
    msg.showinfo("prodi",f"prodi Teknologi Informasi:")
tombolnama = tk.Button(top, text="Hasil Prediksi",command=tampilkanNama)
tombolnama.pack(side=tk.BOTTOM)

top.mainloop()

