# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:14:01 2020

@author: KELOMPOK 9 PROGKOMP
"""


from os import system
import datetime
from tkinter import *

root = Tk()
q0 = Label(root, text="====================================================")
q1 = Label(root, text="  SELAMAT DATANG DI PROGRAM PERHITUNGAN NILAI GIZI    ")
T1 = Label(root, text="             Kelompok kami terdiri dari:             ")
z2 = Label(root, text="                                                     ")
T2 = Label(root, text="           1.Anggara Firmansyah  (I0319013)      ")
T3 = Label(root, text="           2.Aulia Ba'syafira W  (I0319017)       ")
T4 = Label(root, text="           3.Dirgantara Kusuma P (I0319026)       ")
T5 = Label(root, text="           4.Fatimah Jihan A     (I0319035)        ")
T6 = Label(root, text="           5.Anisa Agustina      (I0318013)         ")
q2 = Label(root, text="                                                     ")
q3 = Label(root, bg="red", fg="white", text="     Untuk melanjutkan program, Silahkan tutup pesan ini \nTerima Kasih   ")
q4 = Label(root, text="                                                     ")
q5 = Label(root, text="                                                     ")
q6 = Label(root, text="                                                     ")
q7 = Label(root, text="   Kelompok 9 Presents   ")
q8 = Label(root, text="====================================================")

q0.pack()
q1.pack()
T1.pack()
z2.pack()
T2.pack()
T3.pack()
T4.pack()
T5.pack()
T6.pack()
q2.pack()
q3.pack(fill=X)
q4.pack()
q5.pack()
q6.pack()
q7.pack()
q8.pack()

root.mainloop()

#dictionaryglobal
datagizi = {}
datagizicsv = {}

        
#fungsipendataanbayi
def databalita():
    #berfungsi menentukan kebenaran untuk menjalankan pengulangan
    identitas = True
    
    while identitas:
        
        #list untuk menampung data bayi
        databayi = []
        nama = str(input("Tuliskan nama bayi: "))
        databayi.append(nama)
        jenis_kelamin=(str(input("1). Laki-Laki\n2). Perempuan\nJenis Kelamin: ")))         
        #mendata bayi laki-laki
        if jenis_kelamin == ("1"):
            #fungsi pengolahan usia dari waktu pendataan realtime 
            tanggal= True
            while tanggal:   
                tanggaldata = datetime.datetime.now()  
                print("Inputkan tanggal lahir bayi\n\t-Program ini hanya di peruntukkan untuk balita.\n\t-Progam dapat menghasilkan hasil saat bayi lahir pada tahun 5 tahun sebelum tahun pendataan ini.")   
                tgl= int(input("Tanggal(1-31): "))
                if 1<= tgl <=31:
                    bln= int(input("Bulan(1-12): "))
                    if 1<= bln <=12:                    
                        thn= int(input("Tahun: "))
                    else:  
                        print("Mohon masukkan data yang sesuai")
                        tanggal = True    
                else:
                    print("Mohon masukkan data yang sesuai")
                    tanggal = True
       
                tgl_lahir=(f"{tgl}-{bln}-{thn}")
                databayi.append(tgl_lahir)
   
   
                yearvalue = tanggaldata.year
                monthvalue = tanggaldata.month
                dayvalue = tanggaldata.day
                tgl_data= (f"{dayvalue}-{monthvalue}-{yearvalue}")
                databayi.append(tgl_data)
    
                dhari = dayvalue - tgl
                if dhari >= 15:
                    dhari = 1
                else:
                    dhari = 0
                dbulan= monthvalue - bln
                dtahun= (yearvalue - thn)*12
                total= dhari + dtahun + dbulan
                usia= total               
                databayi.append(f"{usia} bulan")
                break
            databayi.append('Laki-Laki')            
            datamedian_laki= [
        [0,2.9,3.3,3.9],
        [1,3.9,4.5,5.1],
        [2,4.9,5.6,6.3],
        [3,5.7,6.4,7.2],
        [4,6.2,7,7.8],
        [5,6.7,7.5,8.4],
        [6,7.1,7.9,8.8],
        [7,7.4,8.3,9.2],
        [8,7.7,8.6,9.6],
        [9,8,8.9,9.9],
        [10,8.2,9.2,10.2],
        [11,8.4,9.4,10.5],
        [12,8.6,9.6,10.8],
        [13,8.8,9.9,11],
        [14,9,10.1,11.3],
        [15,9.2,10.3,11.5],
        [16,9.4,10.5,11.7],
        [17,9.6,10.7,12],
        [18,9.8,10.9,12.2],
        [19,10,11.1,12.5],
        [20,10.1,11.3,12.7],
        [21,10.3,11.5,12.9],
        [22,10.5,11.8,13.2],
        [23,10.7,12,13.4],
        [24,10.8,12.2,13.6],
        [25,11,12.4,13.9],
        [26,11.2,12.5,14.1],
        [27,11.3,12.7,14.3],
        [28,11.5,12.9,14.5],
        [29,11.7,13.1,14.8],
        [30,11.8,13.3,15],
        [31,12,13.5,15.2],
        [32,12.1,13.7,15.4],
        [33,12.3,13.8,15.6],
        [34,12.4,14,15.8],
        [35,12.6,14.2,16],
        [36,12.7,14.3,16.2],
        [37,12.9,14.5,16.4],
        [38,13,14.7,16.6],
        [39,13.1,14.8,16.8],
        [40,13.3,15,17],
        [41,13.4,15.2,17.2],
        [42,13.6,15.3,17.4],
        [43,13.7,15.5,17.6],
        [44,13.8,15.7,17.8],
        [45,14,15.8,18],
        [46,14.1,16,18.2],
        [47,14.3,16.2,18.4],
        [48,14.4,16.3,18.6],
        [49,14.5,16.5,18.8],
        [50,14.7,16.7,19],
        [51,14.8,16.8,19.2],
        [52,15,17,19.4],
        [53,15.1,17.2,19.6],
        [54,15.2,17.3,19.8],
        [55,15.4,17.5,20],
        [56,15.5,17.7,20.2],
        [57,15.6,17.8,20.4],
        [58,15.8,18,20.6],
        [59,15.9,18.2,20.8],
        [60,16,18.3,21]
        ]
            
            median=0
            for median in datamedian_laki:
                if usia in median:
                    bb = float(input("Berapa berat bayi?(kg): "))
                    databayi.append(f"{bb} kg")                   
                    if bb>median[2]:
                         indeks = round((bb - median[2])/(median[3]-median[2]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             status = 'Gizi Lebih'
                             break                           
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             status = 'Gizi Kurang'
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             status = 'Gizi Buruk'
                             break                           
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             status = 'Gizi Normal'
                             break                          
                    elif bb<median[2]:
                         indeks = round((bb - median[2])/(median[2] - median[1]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             status = 'Gizi Lebih'
                             break                            
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             status = 'Gizi Kurang'
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             status = 'Gizi Buruk'
                             break                             
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             status = 'Gizi Normal'
                             break                             
                    else:
                         
                         indeks = round((bb - median[2])/(median[2]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             status = 'Gizi Lebih'
                             break                          
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             status = 'Gizi Kurang'
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             status = 'Gizi Buruk'
                             break                           
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             status = 'Gizi Normal'
                             break                             
                elif usia >=60:
                    print("--------------------")
                    print("Maaf bayi anda tidak termasuk bayi balita.")
                    databayi.append('Bukan bayi balita')
                    break                
               
        #pendataan bayi perempuan
        elif jenis_kelamin == ("2"):            
            #fungsi pengolahan usia berdasarkan tanggal
            tanggal= True
            while tanggal:   
                tanggaldata = datetime.datetime.now()  
                print("Inputkan tanggal lahir bayi\n\t-Program ini hanya di peruntukkan untuk balita.\n\t-Hanya balita yang lahir 5 tahun sebelum pendataan ini.")   
                tgl= int(input("Tanggal(1-31): "))
                if 1<= tgl <=31:
                    bln= int(input("Bulan(1-12): "))
                    if 1<= bln <=12:                    
                        thn= int(input("Tahun: "))
                    else:  
                        print("Mohon masukkan data yang sesuai")
                        tanggal = True    
                else:
                    print("Mohon masukkan data yang sesuai")
                    tanggal = True
       
                tgl_lahir=(f"{tgl}-{bln}-{thn}")
                databayi.append(tgl_lahir)
   
   
                yearvalue = tanggaldata.year
                monthvalue = tanggaldata.month
                dayvalue = tanggaldata.day
                tgl_data = (f"{dayvalue}-{monthvalue}-{yearvalue}")
                databayi.append(tgl_data)
    
                dhari = dayvalue - tgl
                if dhari >= 15:
                    dhari = 1
                else:
                    dhari = 0
                dbulan= monthvalue - bln
                dtahun= (yearvalue - thn)*12
                total= dhari + dtahun + dbulan
                usia= total               
                databayi.append(f"{usia} bulan")
                break
            databayi.append('Perempuan')                         
            datamedian_perempuan = [
                     [0,2.8,3.2,3.7],
                     [1,3.6,4.2,4.8],
                     [2,4.5,5.1,5.8],
                     [3,5.2,5.8,6.6],
                     [4,5.7,6.4,7.3],
                     [5,6.1,6.9,7.8],
                     [6,6.5,7.3,8.2],
                     [7,6.8,7.6,8.6],
                     [8,7,7.9,9],
                     [9,7.3,8.2	,9.3],
                     [10,7.5,8.5,9.6],
                     [11,7.7,8.7,9.9],
                     [12,7.9,8.9,10.1],
                     [13,8.1,9.2,10.4],
                     [14,8.3,9.4,10.6],
                     [15,8.5,9.6,10.9],
                     [16,8.7,9.8,11.1],
                     [17,8.9,10,11.4],
                     [18,9.1,10.2,11.6],
                     [19,9.2,10.4,11.8],
                     [20,9.4,10.6,12.1],
                     [21,9.6,10.9,12.3],
                     [22,9.8,11.1,12.5],
                     [23,10,11.3,12.8],
                     [24,10.2,11.5,13],
                     [25,10.3,11.7,13.3],
                     [26,10.5,11.9,13.5],
                     [27,10.7,12.1,13.7],
                     [28,10.9,12.3,14],
                     [29,11.1,12.5,14.2],
                     [30,11.2,12.7,14.4],
                     [31,11.4,12.9,14.7],
                     [32,11.6,13.1,14.9],
                     [33,11.7,13.3,15.1],
                     [34,11.9,13.5,15.4],
                     [35,12,13.7,15.6],
                     [36,12.2,13.9,15.8],
                     [37,12.4,14,16],
                     [38,12.5,14.2,16.3],
                     [39,12.7,14.4,16.5],
                     [40,12.8,14.6,16.7],
                     [41,13,14.8,16.9],
                     [42,13.1,15,17.2],
                     [43,13.3,15.2,17.4],
                     [44,13.4,15.3,17.6],
                     [45,13.6,15.5,17.8],
                     [46,13.7,15.7,18.1],
                     [47,13.9,15.9,18.3],
                     [48,14,16.1,18.5],
                     [49,14.2,16.3,18.8],
                     [50,14.3,16.4,19],
                     [51,14.5,16.6,19.2],
                     [52,14.6,16.8,19.4],
                     [53,14.8,17,19.7],
                     [54,14.9,17.2,19.9],
                     [55,15.1,17.3,20.1],
                     [56,15.2,17.5,20.3],
                     [57,15.3,17.7,20.6],
                     [58,15.5,17.9,20.8],
                     [59,15.6,18,21],
                     [60,15.8,18.2,21.2],
                     ]
            median = 0
            for median in datamedian_perempuan:
                 if usia in median:
                     bb = float(input("Berapa berat bayi?(kg): "))
                     databayi.append(f"{bb} kg")
                     if bb>median[2]:
                        indeks = round((bb - median[2])/(median[3]-median[2]),2)
                        databayi.append(indeks)
                        if indeks > 2:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Lebih")
                            databayi.append('Gizi Lebih')
                            status = 'Gizi Lebih'
                            break
                        elif -3 <= indeks <= -2:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Kurang")
                            databayi.append('Gizi Kurang')
                            status = 'Gizi Kurang'
                            break
                        elif indeks < -3:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Buruk")
                            databayi.append('Gizi Buruk')
                            status = 'Gizi Buruk'
                            break
                        else:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Normal")
                            databayi.append('Gizi Normal')
                            status = 'Gizi Normal'
                            break
                     elif bb<median[2]:
                          indeks = round((bb - median[2])/(median[2] - median[1]),2)
                          databayi.append(indeks)
                          if indeks > 2:
                              print("--------------------")
                              print("Indeks Gizi =", round(indeks,2))
                              print("Status Gizi = Gizi Lebih")
                              databayi.append('Gizi Lebih')
                              status = 'Gizi Lebih'
                              break 
                          elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             status = 'Gizi Kurang'
                             break
                          elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             status = 'Gizi Buruk'
                             break
                          else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             status = 'Gizi Normal'
                             break
                     else:
                         indeks = round((bb - median[2])/(median[2]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             status = 'Gizi Lebih'
                             break
                         elif indeks -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             status = 'Gizi Kurang'
                             break
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             status = 'Gizi Buruk'
                             break
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')  
                             status = 'Gizi Normal'                         
                             break
                 elif usia >= 60:
                    print("Maaf bayi anda tidak termasuk bayi balita.")
                    databayi.append('Bukan bayi balita')
                    break
        else:
            print("Mohon memasukkan jenis kelamin yang sesuai")                        
        #berfungsi menyimpan data ke dictioary global dengan key of dict "nama"
        datagizi[nama]=databayi
        
        
        #berfungsi menanyakan perulangan untuk menambah data
        print("----------------")
        print("")
        print("Apakah ada yang perlu di inputkan lagi?")
        print("1). Ada\n2). Tidak Ada")
        ulang = input("# ")
        if ulang == ("1"):
            identitas = True
        elif ulang == ("2"):
            identitas = False
        else:
            print("Input anda salah!!\nMohon masukkan angka berdasarkan pilihan di atas")
            break
        import csv
        import os
        header=['NAMA', 'TANGGAL LAHIR', 'TANGGAL DATA', 'USIA', 'JENIS KELAMIN', 'BB(kg)', 'INDEKS', 'STATUS GIZI']
        
        with open('datagizi.csv','a', newline='\n') as filecsv:
            datagizicsv = {'NAMA' : nama, 'TANGGAL LAHIR': tgl_lahir, 'TANGGAL DATA' : tgl_data, 'USIA' : usia, 'JENIS KELAMIN' : jenis_kelamin, 'BB(kg)' : bb, 'INDEKS' : indeks, 'STATUS GIZI': status}
            
            writer = csv.DictWriter(filecsv, fieldnames = header)
            if os.stat('datagizi.csv').st_size == 0:
                writer.writeheader()  
            else:
                None
            writer.writerow(datagizicsv)    
            
#fungsi cek data berdasarkan nama            
def datanama():
    namabayi = True
    
    while namabayi:
        ceknama = str(input("Tuliskan nama bayi anda: "))
        if ceknama in datagizi:
            print(datagizi[ceknama][0])
            print(datagizi[ceknama][6])
            print(datagizi[ceknama][7])
        else:
            print("Maaf,nama bayi tidak tersedia.")
        print("----------------")
        print("")
        print("Apakah ingin cek lagi?")
        print("1). Ya\n2). Tidak")
        ulang = input("# ")
        if ulang == ("1"):
            namabayi = True
        else:
            namabayi = False      
            
        
while True:
    system ('cls')
    print("===================================================================")
    print("           Selamat Datang di Program Pendataan Balita")
    print("===================================================================")
    print("                   Posyandu Balita Indonesia")
    print("       Program ini berfungsi untuk mengetahui status balita.")
    print("    Status gizi didapat dari perhitungan BB terhadap usia balita.")
    print("       Perhitungan dilakukan berdasarkan tabel rujukan WHO.")
    print("         Data yang diinput akan masuk ke dalam file csv.")
    print("===================================================================")
    print("           Kami memiliki 3 fitur yang dapat digunakan")
    print("                (1) untuk pendataan gizi bayi")    
    print("                (2) untuk cek status gizi")
    print("                (3) untuk keluar program")
    print("            Silahkan pilih salah satu fitur: (angka)")
    print('                    Kelompok 9 Presents')
    print("==================================================================")
    print("           Klik ctrl + c untuk memulai ulang program")
    print("==================================================================")
    
    start = input("# ")
    if start== ("1"):
        system ("cls")
        databalita()
    elif start== ("2"):
        system ("cls")
        datanama()
    else:
        system ("cls")
        print("PROGRAM SELESAI\nDATA ANDA TELAH TERSIMPAN\nTERIMA KASIH")   
        break
