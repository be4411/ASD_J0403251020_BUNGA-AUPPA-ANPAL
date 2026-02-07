#praktikum
#============================================
    #praktikum 1 : konsep ADT dan file handling
    #latihan dasar 1 : membaca seluruh isi file
#===========================================
data_list= []



#membuka file dengan mode read ("r")
with open("data_mahasiswa.txt","r") as file:
     isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("===Hasil Reaad===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)  


#membuka file per baris
print("===membaca file per baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r") as file:
     for baris in file:
          jumlah_baris = jumlah_baris + 1
          baris = baris.strip() #menghilangkan baris baru \n
          print("Baris ke-", jumlah_baris)
          print("isinya :", baris)


#============================================
    #praktikum 1 : konsep ADT dan file handling
    #latihan dasar 2 : parsing baris menjadi kolom data
#===========================================
data_list= []

with open("data_mahasiswa.txt", "r") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")#sparsing data berdasarkan karakter
        print("NIM :", nim, "Nama:", nama ,"Nilai: " , nilai)

    



#============================================
    #praktikum 1 : konsep ADT dan file handling
    #latihan dasar 3 : membaca file dan menyimpan ke list
#===========================================
data_list= []
with open("data_mahasiswa.txt", "r") as file :
         for baris in file:
              baris = baris.strip()
              #simpan sebagai list "(nim, nama, nilai)"
              data_list.append([nim,nama,int(nilai)])
            
print("==== data mahasiswa dalam LIST===")
print(data_list)

print("=== jumlah record dalam list===")
print("contoh record pertama: ", data_list[0])


#============================================
    #praktikum 1 : konsep ADT dan file handling
    #latihan dasar 4 : membaca file dan menyimpan ke dictionary
#=============================================

data_dict = {}#buat variabel untuk dict
with open("data_mahasiswa.txt", "r") as file :
     for baris in file :
          baris = baris.strip()
          nim,nama, nilai = baris.split(",")
          
          #simpan data mahasiswa ke dictionary dengan ke NIM
          data_dict[nim] = {                #key
               "nama" : nama,                #values
               "nilai" : int(nilai)         #values     
          }
print("===data mahasiswa dalam dictionary====")
print(data_dict)