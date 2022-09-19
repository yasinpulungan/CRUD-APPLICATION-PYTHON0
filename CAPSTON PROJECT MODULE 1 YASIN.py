# DATABASE NILAI AKADEMIK SISWA/SISWI YAYASAN KECUP MANJAH
# CAPSTON PROJECT MODULE 1 JCDS
# RAHMAD YASIN PULUNGAN



data_siswa = {
            '12.022' : {'Nama' : 'Sinta', 'Kelas' : 'XII', 'Bertahan Hidup' : 67, 'Menyelesaikan Masalah' : 77, 'Pendewasaan' : 88},
            '09.012' : {'Nama' : 'Jojo', 'Kelas' : 'IX', 'Bertahan Hidup' : 90, 'Menyelesaikan Masalah' : 76, 'Pendewasaan' : 88},
            '06.020' : {'Nama' : 'Supri', 'Kelas' : 'I', 'Bertahan Hidup' : 99, 'Menyelesaikan Masalah' : 89, 'Pendewasaan' : 99}
            }

data_baru = {}

kode_kelas = {
    '01':'I',
    '02':'II',
    '03':'III',
    '04':'IV',
    '05':'V',
    '06':'VI',
    '07':'VII',
    '08':'VIII',
    '09':'IX',
    '10':'X',
    '11':'XI',
    '12':'XII'
}

# MENU AWAL TAMPILAN DATABASE
def Halo():
    print(f'''
    ========================================================
    SELAMAT DATANG DI DATABASE AKADEMIK YAYASAN KECUP MANJAH
    ========================================================
                        MENU UTAMA:
                        -----------
    1. TAMPILKAN DAFTAR AKADEMIK SISWA/I
    2. MENAMBAH NILAI AKADEMIK SISWA/I
    3. MENGUPDATE NILAI AKADEMIK SISWA/I
    4. MENGHAPUS NILAI AKADEMIK SISWA/I
    5. EXIT DATABASE
    ''')
    menu_awal = input("MASUKKAN TUJUAN ANDA [1-5] : ")
    print("="*50)
    if menu_awal == '1':
        print(" ")
        tampilkan()
    elif menu_awal == '2':
        tambahkan()
    elif menu_awal == '3':
        update()
    elif menu_awal == '4':
        hapuskan()
    elif menu_awal == '5':
        print("==========TERIMA KASIH TELAH BERKUNJUNG==========")
    else:
        print("==========PILIHAN YANG ANDA MASUKKAN TIDAK TERSEDIA==========")
        Halo()
       

# MENU 1 READ (TAMPILKAN)
def tampilkan():
    print(f'''
    ========================================================
                     DATA AKADEMIK SISWA/I
    ========================================================
                        MENU 1 :
                        --------
    1. TAMPILKAN SELURUH DAFTAR AKADEMIK SISWA/I
    2. TAMPILKAN DATA AKADEMIK SISWA/I TERTENTU
    3. KEMBALI KE MENU UTAMA
    ''')
    menu_tampilkan = input("MASUKKAN TUJUAN ANDA [1-3] : ")
    print("="*50)
    if menu_tampilkan== '1':
        tampil_seluruh()
    elif menu_tampilkan == '2':
        print(" ")
        tampil_tertentu()
    elif menu_tampilkan == '3':
        Halo()
    else : 
        print("==========PILIHAN YANG ANDA MASUKKAN TIDAK TERSEDIA==========")
        print(" ")
        tampilkan()
       
# Menu sub read 1
def tampil_seluruh():
    if len(data_siswa) != 0:
        print(" ")
        print("===============================================================================================")
        print("======================================DATA SISWA===============================================")
        for i in data_siswa :
            print("- Nomer Induk : {} : | ~Nama\t\t\t: {}\t|\n \t\t\t | ~Kelas\t\t\t: {}\t|\n \t\t\t | ~Bertahan Hidup\t\t: {}\t|\n \t\t\t | ~Meyelesaikan Masalah\t: {}\t|\n \t\t\t | ~Pendewasaan\t\t\t: {}\t|".format(i, data_siswa[i]['Nama'], data_siswa[i]['Kelas'], data_siswa[i]['Bertahan Hidup'], data_siswa[i]['Menyelesaikan Masalah'], data_siswa[i]['Pendewasaan']) )
            print("===============================================================================================")
        print(" ")
        tampilkan()
    else:
        print("===================================DATA SISWA TIDAK TERSEDIA========================================")
        print(" ")
        tampilkan()

# Menu sub read 2
def tampil_tertentu():
    nomer_induk =input("MASUKKAN NOMER INDUK SISWA/I [DENGAN FORMAT ANGKA XX.XXX] : ")
    print(" ")
    print("===============================================================================================")
    print("======================================DATA SISWA===============================================")
    if nomer_induk in data_siswa.keys():
        print("- Nomer Induk : {} : | ~Nama\t\t\t: {}\t|\n \t\t\t | ~Kelas\t\t\t: {}\t|\n \t\t\t | ~Bertahan Hidup\t\t: {}\t|\n \t\t\t | ~Meyelesaikan Masalah\t: {}\t|\n \t\t\t | ~Pendewasaan\t\t\t: {}\t|".format(nomer_induk, data_siswa[nomer_induk]['Nama'], data_siswa[nomer_induk]['Kelas'], data_siswa[nomer_induk]['Bertahan Hidup'], data_siswa[nomer_induk]['Menyelesaikan Masalah'], data_siswa[nomer_induk]['Pendewasaan']) )
        print("===============================================================================================")
        print(" ")
        tampilkan()
    else: 
        print("============================DATA SISWA TIDAK TERSEDIA======================================")
        print(" ")
        tampilkan()
      

# MENU 2 CREATE (TAMBAHKAN)
def tambahkan():
    print(f'''
    ========================================================
                     DATA AKADEMIK SISWA/I
    ========================================================
                        MENU 2 :
                        --------
    1. MENAMBAHKAN DATA AKADEMIK BARU SISWA/I 
    2. KEMBALI KE MENU UTAMA
    ''')
    menu_tambahkan = input("MASUKKAN TUJUAN ANDA [1-2] : ")
    print("="*50)
    (" ")
    if menu_tambahkan == '1':
        tambah_data()
    elif menu_tambahkan == '2':
        Halo()
    else : 
        print("==========PILIHAN YANG ANDA MASUKKAN TIDAK TERSEDIA==========")
        print(" ")
        tampilkan()

# Menu sub create 1
def tambah_data() :
    print("==========MENAMBAHKAN DATA==========")
    tambah_ni()

def tambah_ni():
    global nomer_induk
    nomer_induk =input("MASUKKAN NOMER INDUK SISWA/I [DENGAN FROMAT ANGKA XX.XXX] : ")
    if nomer_induk in data_siswa.keys():
        print("==========DATA SUDAH TERDAFTAR==========")
        tambahkan()
    x=0
    if len(nomer_induk)==6:
        x+=1
    else: 
        print("NOMER INDUK TIDAK VALID : \tJUMLAH KARAKTER TIDAK TIDAK MEMENUHI FORMAT BAKU")
        tambah_ni()
    if nomer_induk [2]== ".":
        x+=1
    else:
        print("NOMER INDUK TIDAK VALID : \tTERDAPAT KARATER TIDAK SESUAI FORMAT BAKU")
        tambah_ni()
    if nomer_induk [ :2].isdigit() and nomer_induk[3:].isdigit():
        x+=1
    else :
        print("NOMER INDUK TIDAK VALID : \tTERDAPAT KARATER TIDAK SESUAI FORMAT BAKU")
        tambah_ni()
    if nomer_induk [:2] in kode_kelas.keys():
        x+=1
    else:    
        print("NOMER INDUK TIDAK VALID : \tDUA DIGIT PERTAMA HANYA BISA DI ISI KODE KELAS 01-12")
        tambah_ni()
    if x == 4 :
        tambah_nama()
       
def tambah_nama():
    global nama
    nama = str(input("MASUKKAN NAMA SISWA/I : ")).title()
    data_baru["Nama"]= nama
    tambah_kelas()

def tambah_kelas():
    global kelas_siswa
    kelas_siswa = input ("MASUKKAN KELAS SISWA/I [01-12]: ")
    x=0
    if len(kelas_siswa)==2:
        x+=1
        if kelas_siswa [:].isdigit():
            x+=1
            if kelas_siswa in kode_kelas.keys():
                data_baru["Kelas"] = kode_kelas[kelas_siswa]
                tambah_bh()
            else:

                print("KODE KELAS TIDAK SESUAI : DUA DIGIT PERTAMA HANYA BISA DI ISI KODE KELAS 01-12")
                tambah_kelas()
        else:
            print("KODE KELAS TIDAK SESUAI : HANYA MASUKKAN ANGKA")
            tambah_kelas()
    else:
        print("KODE KELAS TIDAK SESUAI : MASUKKAN JUMLAH KARAKTER YANG TEPAT")
        tambah_kelas()

def tambah_bh():
    global bertahan_hidup
    bertahan_hidup = int(input("MASUKKAN NILAI BERTAHAN HIDUP SISWA/I : "))
    data_baru["Bertahan Hidup"] = bertahan_hidup
    tambah_mm()

def tambah_mm():
    global menyelesaikan_masalah
    menyelesaikan_masalah = int(input("MASUKKAN NILAI MENYELESAIKAN MASALAH SISWA/I : "))
    data_baru["Menyelesaikan Masalah"] = menyelesaikan_masalah
    tambah_pen()

def tambah_pen():
    global pendewasaan
    pendewasaan = int(input("MASUKKAN NILAI PENDEWASAAN SISWA/I : "))
    data_baru["Pendewasaan"] = pendewasaan
    simpan_data()
  
# Opsi simpan data
def simpan_data():
    simpan = str.upper(input("APAKAH ANDA YAKIN UNTUK MENYIMPAN DATA [YES/NO] : "))
    global data_baru
    global data_siswa
    if simpan == 'YES':
        print("")
        print("==========DATA TERSIMPAN==========")
        data_siswa[nomer_induk] = data_baru
        tambahkan()
    elif simpan == 'NO':
        data_siswa = data_siswa
        print("")
        print("==========DATA TIDAK TERSIMPAN=========")
        tambahkan()
    else:
        print("MASUKKAN PILHAN DENGAN BENAR")
        simpan_data()   


# MENU 3 UPDATE
def update():
    print(f'''
    ========================================================
                     DATA AKADEMIK SISWA/I
    ========================================================
                        MENU 3 :
                        --------
    1. MENGUPDATE DATA AKADEMIK BARU SISWA/I 
    2. KEMBALI KE MENU UTAMA
    ''')
    menu_update = input("MASUKKAN TUJUAN ANDA [1-2] : ")
    print("="*50)
    (" ")
    if menu_update == '1':
        update_data()
    elif menu_update == '2':
        Halo()
    else : 
        print("==========PILIHAN YANG ANDA MASUKKAN TIDAK TERSEDIA==========")
        print(" ")
        update()

#Menu sub update 1
def update_data():
    global update_nomer_induk
    update_nomer_induk = input("MASUKKAN NOMER INDUK SISWA/I YANG INGIN DI UPDATE [DENGAN FORMAT ANGKA XX.XXX] : ")
    if update_nomer_induk in data_siswa.keys() :
        print(" ")
        print("===============================================================================================")
        print("======================================DATA SISWA===============================================")
        print("- Nomer Induk : {} : | ~Nama\t\t\t: {}\t|\n \t\t\t | ~Kelas\t\t\t: {}\t|\n \t\t\t | ~Bertahan Hidup\t\t: {}\t|\n \t\t\t | ~Meyelesaikan Masalah\t: {}\t|\n \t\t\t | ~Pendewasaan\t\t\t: {}\t|".format(update_nomer_induk, data_siswa[update_nomer_induk]['Nama'], data_siswa[update_nomer_induk]['Kelas'], data_siswa[update_nomer_induk]['Bertahan Hidup'], data_siswa[update_nomer_induk]['Menyelesaikan Masalah'], data_siswa[update_nomer_induk]['Pendewasaan']) )
        print("===============================================================================================")
        print(" ")
        notif_update()
    else: 
        print("============================DATA SISWA TIDAK TERSEDIA======================================")
        print(" ")
        update()

def data_yg_diedit():
    data_update = input("MASUKKAN KOLOM YANG INGIN DI EDIT : ").title()
    if data_update in data_siswa[update_nomer_induk]:
        data_ubah = input("MASUKKAN NILAI/KARAKTER {} BARU : ".format(data_update)).upper()
        j = 1
        while j != 0:
            simpan_update = input("APAKAH ANDA YAKIN UNTUK MENGUPDATE DATA [YES/NO] : ").upper()
            if simpan_update == 'YES':
                data_siswa[update_nomer_induk][data_update] = data_ubah
                print("")
                print("==========DATA TELAH TERUPDATE==========")
                update()
                j = 0
            elif simpan_update == 'NO':
                print("")
                print("==========UDPATE DATA TELAH DIBATALKAN=========")
                update()
                j = 0
            else:
                j = 1
    else:
        print("==========MASUKKAN KOLOM DATA DENGAN BENAR==========")
        data_yg_diedit()

def notif_update():
    opsi_update = input('''MASUKKAN PILHAN ANDA, 
YES --> UNTUK LANJUT UPDATE 
NO  --> UNTUK BATALKAN UPDATE
[YES/NO] : ''').upper()
    if opsi_update == 'YES' :
        data_yg_diedit()
    elif opsi_update =='NO' :
        print("")
        print("==========UDPATE DATA TELAH DIBATALKAN=========")
        update()
    else :
        print("MASUKKAN PILIHAN DENGAN BENAR")
        notif_update()


# MENU 4 DELETE
def hapuskan():
    print(f'''
    ========================================================
                     DATA AKADEMIK SISWA/I
    ========================================================
                        MENU 4 :
                        --------
    1. MENGHAPUS DATA AKADEMIK BARU SISWA/I 
    2. KEMBALI KE MENU UTAMA
    ''')
    menu_hapus = input("MASUKKAN TUJUAN ANDA [1-2] : ")
    print("="*50)
    (" ")
    if menu_hapus == '1':
        hapus_data()
    elif menu_hapus == '2':
        Halo()
    else : 
        print("==========PILIHAN YANG ANDA MASUKKAN TIDAK TERSEDIA==========")
        print(" ")
        hapuskan()

# Menu sub delete 1
def hapus_data():
    global hapus_nomer_induk
    hapus_nomer_induk = input("MASUKKAN NOMER INDUK SISWA/I YANG INGIN DI HAPUS [DENGAN FORMAT ANGKA XX.XXX] : ")
    if hapus_nomer_induk in data_siswa :
       notif_hapus()
    else: 
        print("============================DATA SISWA TIDAK TERSEDIA======================================")
        print(" ")
        hapuskan()

def notif_hapus():
    opsi_hapus = input('''MASUKKAN PILHAN ANDA, 
YES --> UNTUK LANJUT HAPUS DATA
NO  --> UNTUK BATALKAN HAPUS DATA
[YES/NO] : ''').upper()
    if opsi_hapus == "YES":
        print(" ")
        print("===========DATA SISWA TELAH DIHAPUS===========")
        data_siswa.pop(hapus_nomer_induk)
        hapuskan()
    elif opsi_hapus == "NO" :
        print(" ")
        print("===========HAPUS DATA TELAH DIBATALKAN===========")
        hapuskan()
    else :
        notif_hapus()

Halo()




