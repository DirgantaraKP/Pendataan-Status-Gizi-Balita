#===================================================================
#NIM Dictionary v1.0
#
#Dibuat oleh Satrio Fachri Chaniago (IGO)
#            I0319096
#            Mahasiswa S1 Teknik Industri UNS
#            Angkatan 2019
#
#Versi ini merupakan versi pertama
#
#List Fitur:
#   +Pendataan menggunakan konsep Dictionary
#   +Dictionary yang tersimpan hanya dalam satu kali Run Program 
#   +Penggunaan system("cls") yang menghasilkan interface pada prompt lebih nyaman
#   +Interface yang komunikatif
#   +Dapat dijalankan langsung dari file .py nya tanpa perlu starting prompt terlebih dahulu 
#    dan program tidak autobreak sehingga memudahkan user apabila menggunakan 
#    tanpa melalui starting prompt
#
#Saran dan Masukan untuk pengembangan sangat diperlukan
#Terimakasih
#
#===================================================================

#Import Sistem untuk ("cls") atau terminal clear
from os import system


#=================
#Dictionary Utama
#=================
nimdict = {}
    
    
#=================================
#Definisi untuk Proses DIctionary
#=================================
def datamahasiswa():
    #Menentukan kelanjutan
    nimdict_next = True
    
    while nimdict_next:
        #Inputan
        print ("")
        NIM = input("Input NIM: ")
    
        datamhs = []
        datamhs.append(input ("Nama         : "))
        datamhs.append(input ("Alamat       : "))
        datamhs.append(input ("Tempat Lahir : "))
        datamhs.append(input ("Tanggal Lahir: "))
        datamhs.append(input ("Telepon/HP   : "))
        datamhs.append(input ("Ukuran Sepatu: "))
        datamhs.append(input ("Tinggi Badan : "))
    
        #Menyimpan hasil input
        nimdict[NIM] = datamhs
    
        #Pengulangan
        print ("")
        print ("Apakah ada yang perlu di inputkan lagi?")
        print ("YA    (1)")
        print ("TIDAK (2)")
    
        ulang = input("> ")
        if ulang == ("1"):
            nimdict_next = True
        else:
            nimdict_next = False
           
           

def datanim():
    #Menentukan Kelanjutan
    nimdict_key_next = True
    
    while nimdict_key_next:
        #Inputan
        print ("")
        print ("Masukkan NIM untuk melihat data berkaitan.")
        print ("")
        nimdict_key = input("> ")
        print ("")
        
        if nimdict_key in nimdict:
            print (nimdict[nimdict_key])
        else:
            print ("Input SALAH! Ulangi input!")
    
        #Pengulangan
        print ("")
        print ("Apakah ada yang perlu di inputkan lagi?")
        print ("YA    (1)")
        print ("TIDAK (2)")
    
        ulang = input("> ")
        if ulang == ("1"):
            nimdict_key_next = True
        else:
            nimdict_key_next = False


#===============================         
#TAMPILAN MUKA AWAL (INTERFACE)
#===============================
while True:
    print ("==================================================================")
    print ("                        PROGRAM NIM DICTIONARY                    ")
    print ("==================================================================")
    print ("            Program ini digunakan untuk mendata mahasiswa         ")
    print ("         Program berjalan menggunakan cara Python Dictionary      ")
    print ("      NIM digunakan sebagai parameter utama (key of dictionary)   ")
    print ("     Data yang diinputkan hanya berlaku dalam sekali RUN Program  ")
    print ("")
    print ("      Jika terjadi ERROR, klik ctrl + c lalu mulai ulang program  ")
    print ("")
    print ("==================================================================")
    print ("                               MENU AWAL                          ")
    print ("==================================================================")
    print ("")
    print ("                   Klik (1) Untuk INPUT Data Mahasiswa            ")
    print ("                   Klik (2) Untuk CEK Data Mahasiswa              ")
    print ("                   Klik (3) Untuk KELUAR dari Program             ")
    print ("")

    mulai = input("> ")
    if mulai == ("1"):
        system ("cls")
        print ("==================================================================")
        print ("                         PROGRAM NIM DICTIONARY                   ")
        print ("==================================================================")
        print ("                          INPUT DATA MAHASISWA                    ")
        print ("")
        datamahasiswa()
            
    elif mulai == ("2"):
        system ("cls")
        print ("==================================================================")
        print ("                         PROGRAM NIM DICTIONARY                   ")
        print ("==================================================================")
        print ("                           CEK DATA MAHASISWA                     ")
        print ("")
        datanim()
    
    elif mulai == ("3"):
        system ("cls")
        print ("")
        print ("PROGRAM TERHENTI!")
        print ("")
        break
        
    else:
        system ("cls")
        print ("")
        print ("Input SALAH!")
        print ("PROGRAM TERHENTI!")
        print ("")
        break


