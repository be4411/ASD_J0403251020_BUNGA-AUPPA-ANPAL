# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Bunga Auppa Anpal
# NIM : J0403251020
# Kelas : TPL-B2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------

NAMA_FILE = "pertemuan 2/stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(NAMA_FILE) :
    stok_dict = {}
    with open(NAMA_FILE, "r") as file :
        for baris in file:
            baris = baris.strip() 
            if not baris:
                continue
            parts = baris.split(",")
            if len(parts) == 3:
                kode, nama, stok = parts
                stok_dict[kode] = {
                        "nama": nama,
                        "stok": int(stok)
                    }
    return stok_dict

#buka_data = baca_stok(NAMA_FILE)
#print("jumlah data terbaca ", len(buka_data))

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_stok(NAMA_FILE,stok_dict):
    with open(NAMA_FILE, "w") as file :
        for KodeBarang in stok_dict:
            NamaBarang = stok_dict[KodeBarang]["nama"]
            stok = stok_dict[KodeBarang]["stok"]
            file.write(f"{KodeBarang},{NamaBarang},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0:
        print("\n--- Stok barang kosong ---")
        return
    
    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'KODE':<10} | {'NAMA BARANG':<20} | {'STOK':>5}")
    print("-" * 40)
    
    for KodeBarang in sorted(stok_dict.keys()):
        NamaBarang = stok_dict[KodeBarang]["nama"]
        stok = stok_dict[KodeBarang]["stok"]
        print(f"{KodeBarang:<10} | {NamaBarang:<20} | {stok:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        barang = stok_dict[kode]
        print("\n--- Barang Ditemukan ---")
        print(f"Kode : {kode}")
        print(f"Nama : {barang['nama']}")
        print(f"Stok : {barang['stok']}")
    else:
        print("\nBarang tidak ditemukan!.")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    KodeBarang= input("masukan kode barang baru: ").strip

    if KodeBarang in stok_dict:
        print("kode sudah digunakan")
        return
    
    NamaBarang = input("masukan nama barang:").strip
    try:
        stok_awal = int(input("masukan jumlah stok awal: "))
        stok_dict ={"nama": NamaBarang, "stok": stok_awal}
        print(f"barang {NamaBarang} berhasil ditambahkan")
    except ValueError:
        print("input stok harus angka. penambahan gagal")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    KodeBarang = input("masukan kode barang yang akan diupdate: ")

    if KodeBarang not in stok_dict :
        print("kode tidak ditemukan!")
        return
    
    print("1.Tambah stok")
    print("2. kurangi stok")
    pilihan = input("masukan pillihan 1/2: ").strip()
 
    try:
        jumlah = int(input("masukan jumlah perubahan: "))
        if pilihan == "1" :
            stok_dict[KodeBarang]["stok"] += jumlah
            print("update berhasil")
        elif pilihan == "2" :
            if stok_dict[KodeBarang]["stok"] - jumlah < 0:
                print("update gagal!")
            else:
                stok_dict[KodeBarang["stok"]] -= jumlah
                print("update berhasil")
        else:
            print("pilihan tidak ada")
    except ValueError :
        print("masukan angka 1/2")

# -------------------------------
# Program Utama
# -------------------------------

def main():
 stok_barang = baca_stok(NAMA_FILE)
 
 while True:
    print("\n=== MENU STOK KANTIN ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan kode")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Simpan ke file")
    print("0. Keluar")
    pilihan = input("Pilih menu: ").strip()
    if pilihan == "1":
        tampilkan_semua(stok_barang)
    elif pilihan == "2":
        cari_barang(stok_barang)
    elif pilihan == "3":
        tambah_barang(stok_barang)
    elif pilihan == "4":
        update_stok(stok_barang)
    elif pilihan == "5":
        simpan_stok(NAMA_FILE, stok_barang)
        print("Data berhasil disimpan.")
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
# Menjalankan program utama
if __name__== "__main__":
    main()
