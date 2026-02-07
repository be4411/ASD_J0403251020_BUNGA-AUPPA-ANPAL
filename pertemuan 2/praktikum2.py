#============================================
#praktikum 2 : konsep ADT dan file handling (Studi kasus)
#latihan dasar 1 :membuat load data
#=============================================

nama_file ="data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file) :
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r") as file :
        for baris in file :
             baris = baris.strip() #menghilangkan karakter baris baru

             parts = baris.split(",")
             if len(parts) != 3 :
                 continue
             nim,nama, nilai_str = parts
             nilai_int = int(nilai_str)
             nim,nama, nilai = baris.split(",") #pecah menjadi data satuan
          
          #simpan data dalam dictionary(key,value)
        data_dict[nim] = {                #key
               "nama" : nama,                #values
               "nilai" : int(nilai)         #values     
        }
    return data_dict

#memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
print("jumlah data terbaca ", len(buka_data))


#============================================
#praktikum 2 : konsep ADT dan file handling (Studi kasus)
#latihan dasar 2 :membuat fungsi menampilkan data
#=============================================
data_dict = {}
def tampilkan_data(data_dict) :
    if len(data_dict)== 0 :
        print("data kosong")
        return
    
    #membuat header tabel
    print("\n==== Daftar mahasiswa===")
    print(f"{'NIM':<10}| {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)

    '''
    untuk tampilan yang rapi, atur f-string formating
     {'NIM' : <10} artinya :
     tampilkan nim <= rata kiri dengan lebar 10 karakter
     {'Nama': <12}
    tampilkan nim <= rata kiri dengan lebar kolom 12 karakter
    {'Nilai': >5}
    tampilkan nim <= rata kanan dengan lebar kolom 5 karakter
    '''

    for nim in sorted(data_dict):
        nama= data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim :<10} | {nama:<12} | {nilai:>5}")
#memanggil fungsi menampilkan data
#tampilkan_data(buka_data)

#============================================
#praktikum 2 : konsep ADT dan file handling (Studi kasus)
#latihan dasar 3 :membuat fungsi mencari data
#=============================================

def cari_data (data_dicari) :
    #mencari data mahasiswa  berdasarkan NIM
    nim_cari = input("masukan NIM yang dicari ").strip()
    if nim_cari in data_dict :
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']

        print("\n=== Data Mahasiswa Ditemukan")
        print(f"NIM      : {nim_cari}")
        print(f"Nama      : {nama}")
        print(f"Nilai      : {nilai}")


#============================================
#praktikum 2 : konsep ADT dan file handling (Studi kasus)
#latihan dasar 4 :membuat fungsi update nilai
#=============================================

def update_nilai(data_dict):

    #cari nim mahas
    nim = input("masukan NIM mahasiswa yang akan di update").strip()
    if nim not in data_dict :
        print ("NIM tidak ditemukan")
        return
    try:
        nilai_baru = int(input("masukan nilai baru (0-100):").strip())
    except ValueError :
        print("nilai harus berupa angka. update dibatalkan")
        return 
    if nilai_baru < 0 or nilai_baru > 100:
        print("nilai harus antara 0 sampai 100. update dibatalkan")

    nilai_lama= data_dict[nim]["nilai"]
    #memasukan nilai baru ke dictionary
    data_dict[nim]['nilai'] = nilai_baru

    print(f"update berhasil. nilai{nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)

#============================================
#praktikum 2 : konsep ADT dan file handling (Studi kasus)
#latihan dasar 5 :membuat fungsi perubahan data ke file
#=============================================

def simpan_data(nama_file,data_dict):
    with open(nama_file, "w") as file :
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buka_data)
#print("data berhasil disimpan")


#============================================
#praktikum 2 : konsep ADT dan file handling (Studi kasus)
#latihan dasar 6:membuat menu program
#=============================================

def main():
    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True :
    print("\n=== MENU DATA MAHASISWA===")
    print("1. Tampilkan semua data")
    print("2. Cari data berdaSASRKAN NIM")
    print("3. Update nilai mahasiswa ")
    print("4. Simpan data ke file ")
    print("0. Keluar")
                

    pilihan = input("pilihan menu : ").strip()

    if pilihan == "1" :
        tampilkan_data(buka_data)
    elif pilihan == "2":
        cari_data(buka_data)
    elif pilihan =="3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
        print("data berhasil disimpan")
    elif pilihan == "0":
        print("program selesai")
        break

    else :
        print("pilihan tidak valid")

if __name__ == "__main__" :
    main()