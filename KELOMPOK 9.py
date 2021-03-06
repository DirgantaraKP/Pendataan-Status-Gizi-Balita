
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:14:01 2020
@author: KELOMPOK 9 PROGKOMP
"""


from os import system
import datetime
from tkinter import *
import tkinter.ttk
import tkinter as tk




#fungsi menutup jendela
def close_window():    
    root.destroy()

#Menambahkan fitur GUI menggunakan Tkinter
root = Tk()
root.title("\tDataGizi 1.0")
width = 500
height = 360
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
q0 = Label(root, text="====================================================")
q1 = Label(root, text="  SELAMAT DATANG DI PROGRAM PERHITUNGAN NILAI GIZI", font='Gungsuh 12')
T1 = Label(root, text="Kelompok kami terdiri dari:", font='Gungsuh 12')
T1.place(x= width/2, y= height/2)
z2 = Label(root, text="                                                      ")
T2 = Label(root, text="1.Anggara Firmansyah\t(I0319012)",font='Gungsuh 12')
T2.place(x= width/2, y= height/2)
T3 = Label(root, text="2.Aulia Ba'syafira W\t\t(I0319017)",font='Gungsuh 12')
T3.place(x= width/2, y= height/2)
T4 = Label(root, text="3.Dirgantara Kusuma P\t(I0319026)",font='Gungsuh 12')
T4.place(x= width/2, y= height/2)
T5 = Label(root, text="4.Fatimah Jihan A\t\t(I0319035)",font='Gungsuh 12')
T5.place(x= width/2, y= height/2)
T6 = Label(root, text="5.Anisa Agustina\t\t(I0318013)",font='Gungsuh 12')
T6.place(x= width/2, y= height/2)
q2 = Label(root, text="                                                     ")
q3 = Label(root, bg="red", fg="white", text="Untuk melanjutkan program, klik tombol 'NEXT'",font='Gungsuh 12')
q4 = Label(root, text="                                                     ")
q5 = Label(root, text="                                                     ")
q6 = Label(root, text="                                                     ")
q7 = Label(root, text="    Created by Kelompok 9   ",font='Gungsuh 12')
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
q3.pack()
q4.pack()
q5.pack()
q6.pack()
q7.pack()
q8.pack()

B = Button(root, text = "NEXT", command = close_window)
B.pack(anchor = S)
B.place(x= 225, y=275)

root.mainloop()        
#fungsipendataanbayi
def databalita():
    #berfungsi menentukan kebenaran untuk menjalankan pengulangan
    identitas = True   
    while identitas:
        import tkinter as tk
        
        root = tk.Tk()       
        root.title("\tDataGizi 1.0")
        #adalah paket pengaturan jendela
        width = 360
        height = 410
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        
        namastring= tk.StringVar(root)#menunjukkan inputan adalah string
        nomorstring= tk.StringVar(root)
        jkstring= tk.StringVar(root)
        tglstring= tk.StringVar(root)
        blnstring= tk.StringVar(root)
        thnstring= tk.StringVar(root)
        bbstring= tk.StringVar(root)
        def close():
            root.destroy()
            
        perintah0 = Label(root,bg='red',text= "Untuk memindahkan cursor tekan (TAB)",font="Times 12 bold",).pack(pady=2)
        
        perintah1 = Label(root,text= "Nama anak:",font="Times 11 bold",).pack()
        input1 = Entry(root,textvariable = namastring).pack()
        perintah = Label(root,text= "Nomor Induk Anak:",font="Times 11 bold",).pack()
        input1 = Entry(root,textvariable = nomorstring).pack()
        perintah2 = Label(root,text= "Jenis kelamin anak:\n(input dengan angka)\n(1).Laki-laki\n(2).Perempuan ",font="Times 11 bold",).pack()
        input2 = Entry(root,textvariable = jkstring).pack()
        perintah3= Label(root,text= "Tanggal lahir(1-31):",font="Times 11 bold",).pack()
        input3 = Entry(root,textvariable = tglstring).pack()
        perintah4= Label(root,text= "Bulan lahir(1-12):",font="Times 11 bold",).pack()
        input4 = Entry(root,textvariable = blnstring).pack()
        perintah5= Label(root,text= "Tahun lahir(yyyy):",font="Times 11 bold",).pack()
        input5 = Entry(root,textvariable = thnstring).pack()
        perintah6= Label(root,text= "Berat badan(kg):",font="Times 11 bold",).pack()
        input6 = Entry(root,textvariable = bbstring).pack()
        B = Button(root, text = "SUBMIT",font = 'Arial 11', command = close)
        B.pack(anchor = S,pady=5)
        root.mainloop()
        
        nama = namastring.get()
        if len(nama)== 0:
            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 400
            height = 25
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            Label(root,text="NAMA TIDAK BOLEH KOSONG", font= 'Gungsuh 12' ).pack(fill=X)
            root.mainloop()
            break
        nomor= nomorstring.get()
        if len(nomor)== 0:
            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 400
            height = 25
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            Label(root,text="NOMOR INDUK HARUS DIISI", font= 'Gungsuh 12' ).pack(fill=X)
            root.mainloop()
            break
            
        jenis_kelamin= jkstring.get()
        #mendata bayi laki-laki
        if jenis_kelamin == ("1"):
            #variabel ini berfungsi saat penulisan csv
            jk= 'Laki-Laki'
            #fungsi pengolahan usia dari waktu pendataan realtime 
            tanggaldata = datetime.datetime.now()           
            tgl= int(tglstring.get())
            if 1<= tgl <=31:
                bln= int(blnstring.get())
                if 1<= bln <=12:                    
                        thn= int(thnstring.get())
                else:
                     root = Tk()
                     root.title("\tDataGizi 1.0")
                     width = 500
                     height = 75
                     screen_width = root.winfo_screenwidth()
                     screen_height = root.winfo_screenheight()
                     x = (screen_width / 2) - (width / 2)
                     y = (screen_height / 2) - (height / 2)
                     root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                     root.resizable(0, 0)
                     a2=("Mohon masukkan data yang sesuai!.\nAnda akan kembali pada menu utama secara otomatis.")
                     p0 = Label(root,font= 'Gungsuh 12', text= a2 )
                     p0.pack(fill=X)       
                     root.mainloop()         
                     break  
            else:
                root = Tk()
                root.title("\tDataGizi 1.0")
                width = 500
                height = 75
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root.resizable(0, 0)
                a2=("Mohon masukkan data yang sesuai!.\nAnda akan kembali pada menu utama secara otomatis.")
                p0 = Label(root,fg='red',font= 'Gungsuh 12', text= a2 )
                p0.pack(fill=X)       
                root.mainloop()
                break   

            tgl_lahir=(f"{tgl}/{bln}/{thn}")                 
            yearvalue = tanggaldata.year
            monthvalue = tanggaldata.month
            dayvalue = tanggaldata.day
            tgl_data= (f"{dayvalue}/{monthvalue}/{yearvalue}")
            tglcsv= (f"{dayvalue}-{monthvalue}-{yearvalue}")
            
            #berfungsi untuk pembulatan hari usia
            dhari = dayvalue - tgl
            if dhari >= 15:
                dhari = 1
            elif 0<=dhari<15:
                dhari = 0
            else:
                dhari = -1
            dbulan= monthvalue - bln
            dtahun= (yearvalue - thn)*12
            total=(dhari + dtahun + dbulan)
            usia= total            
            usiatahun = round((total/12),1)                         
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
            for median in datamedian_laki:
                us = ([median][0][0])
                if usia == us:
                    bb = float(bbstring.get())                
                    if bb>median[2]:
                         indeks = round((bb - median[2])/(median[3]-median[2]),2)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             status = 'Gizi Lebih'
                                                        
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             status = 'Gizi Kurang'
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             status = 'Gizi Buruk'
                             break                           
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             status = 'Gizi Normal'
                             break                                           
                    elif bb<median[2]:
                         indeks = round((bb - median[2])/(median[2] - median[1]),2)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             status = 'Gizi Lebih'
                             break                            
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             status = 'Gizi Kurang'
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             status = 'Gizi Buruk'
                             break                             
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             status = 'Gizi Normal'
                             break                                       
                    else:
                         
                         indeks = round((bb - median[2])/(median[2]),2)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             status = 'Gizi Lebih'
                             break                          
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             status = 'Gizi Kurang'
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             status = 'Gizi Buruk'
                             break                           
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             status = 'Gizi Normal'
                             break                                 
                elif usia >60: 
                    bb = ('None')
                    root = Tk()
                    root.title("\tDataGizi 1.0")
                    width = 500
                    height = 50
                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    x = (screen_width / 2) - (width / 2)
                    y = (screen_height / 2) - (height / 2)
                    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                    root.resizable(0, 0)
                    a2=("Maaf anak anda bukan termasuk balita.")
                    a3=(f"Usia anak anda adalah {usiatahun} tahun")
                    p0 = Label(root,bg='red',font= 'Gungsuh 12', text= a2 )
                    p1 = Label(root,bg='red',font= 'Gungsuh 12', text= a3 )
                    p0.pack(fill=X)  
                    p1.pack(fill=X)  
                    root.mainloop()

                    indeks = ('None')
                    status =('None')
                    break 
                elif usia < 0:
                    usia = 'Usia undefined'
                    bb= 'None'
                    indeks = 'None'
                    status = 'None'  

                    root = Tk()
                    root.title("\tDataGizi 1.0")
                    width = 500
                    height = 50
                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    x = (screen_width / 2) - (width / 2)
                    y = (screen_height / 2) - (height / 2)
                    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                    root.resizable(0, 0)
                    a2=('Ada yang salah pada tanggal.')
                    a3=('Mohon inputkan tanggal dengan benar')
                    p0 = Label(root,bg='red',font= 'Gungsuh 12', text= a2 )
                    p1 = Label(root,bg='red',font= 'Gungsuh 12', text= a3 )
                    p0.pack(fill=X)  
                    p1.pack(fill=X)  
                    root.mainloop()

                    break
            
        #pendataan bayi perempuan
        elif jenis_kelamin == ("2"):
            #variabel ini berfungsi saat penulisan csv
            jk= 'Perempuan'                      
            #fungsi pengolahan usia dari waktu pendataan realtime 
            tanggaldata = datetime.datetime.now() 

            tgl= int(tglstring.get())
            if 1<= tgl <=31:
                bln= int(blnstring.get())
                if 1<= bln <=12:                    
                        thn= int(thnstring.get())      
                else:  
                     root = Tk()
                     root.title("\tDataGizi 1.0")
                     width = 500
                     height = 75
                     screen_width = root.winfo_screenwidth()
                     screen_height = root.winfo_screenheight()
                     x = (screen_width / 2) - (width / 2)
                     y = (screen_height / 2) - (height / 2)
                     root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                     root.resizable(0, 0)
                     a2=("Mohon masukkan data yang sesuai!.\nAnda akan kembali pada menu utama secara otomatis.")
                     p0 = Label(root,font= 'Gungsuh 12', text= a2 )
                     p0.pack(fill=X)       
                     root.mainloop()
                     break  
            else:
                root = Tk()
                root.title("\tDataGizi 1.0")
                width = 500
                height = 75
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root.resizable(0, 0)
                a2=("Mohon masukkan data yang sesuai!.\nAnda akan kembali pada menu utama secara otomatis.")
                p0 = Label(root,font= 'Gungsuh 12', text= a2 )
                p0.pack(fill=X)       
                root.mainloop()
                break
       
            tgl_lahir=(f"{tgl}/{bln}/{thn}")
            yearvalue = tanggaldata.year
            monthvalue = tanggaldata.month
            dayvalue = tanggaldata.day
            tgl_data= (f"{dayvalue}/{monthvalue}/{yearvalue}")
            tglcsv= (f"{dayvalue}-{monthvalue}-{yearvalue}")
            #berfungsi untuk pembulatan hari usia
            dhari = dayvalue - tgl
            if dhari >= 15:
                dhari = 1
            elif 0<=dhari<15:
                dhari = 0
            else:
                dhari = -1
            dbulan= monthvalue - bln
            dtahun= (yearvalue - thn)*12
            total= (dhari + dtahun + dbulan)
            usia= total          
            usiatahun = round((total/12),1)                       
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
                     [60,16,18.3,21]
                     ]
            
            for median in datamedian_perempuan:
                 us = ([median][0][0])
                 if usia == us:  
                     bb = float(bbstring.get())
                     if bb>median[2]:
                        indeks = round((bb - median[2])/(median[3]-median[2]),2)
                        if indeks > 2:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Lebih")
                            status = 'Gizi Lebih'
                            break
                        elif -3 <= indeks <= -2:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Kurang")
                            status = 'Gizi Kurang'
                            break
                        elif indeks < -3:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Buruk")
                            status = 'Gizi Buruk'
                            break
                        else:
                            print("--------------------")
                            print("Indeks Gizi =", round(indeks,2))
                            print("Status Gizi = Gizi Normal")
                            status = 'Gizi Normal'
                            break
                     elif bb<median[2]:
                          indeks = round((bb - median[2])/(median[2] - median[1]),2)
                          if indeks > 2:
                              print("--------------------")
                              print("Indeks Gizi =", round(indeks,2))
                              print("Status Gizi = Gizi Lebih")
                              status = 'Gizi Lebih'
                              break 
                          elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             status = 'Gizi Kurang'
                             break
                          elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             status = 'Gizi Buruk'
                             break
                          else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             status = 'Gizi Normal'
                             break
                     else:
                         indeks = round((bb - median[2])/(median[2]),2)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             status = 'Gizi Lebih'
                             break
                         elif indeks -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             status = 'Gizi Kurang'
                             break
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             status = 'Gizi Buruk'
                             break
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             status = 'Gizi Normal'                         
                             break
                 elif usia > 60:
                    bb = 'None'
                    root = Tk()
                    root.title("\tDataGizi 1.0")
                    width = 500
                    height = 50
                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    x = (screen_width / 2) - (width / 2)
                    y = (screen_height / 2) - (height / 2)
                    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                    root.resizable(0, 0)
                    a2=("Maaf anak anda bukan termasuk balita.")
                    a3=(f"Usia anak anda adalah {usiatahun} tahun")
                    p0 = Label(root,bg='red',font= 'Gungsuh 12', text= a2 )
                    p1 = Label(root,bg='red',font= 'Gungsuh 12', text= a3 )
                    p0.pack(fill=X)  
                    p1.pack(fill=X)  
                    root.mainloop()
                    
                    indeks = ('None')
                    status =('None')
                    break
                
                 elif usia < 0:                     
                    usia = 'Usia undefined'
                    bb= 'None'
                    indeks = 'None'
                    status = 'None'
                    root = Tk()
                    root.title("\tDataGizi 1.0")
                    width = 500
                    height = 50
                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    x = (screen_width / 2) - (width / 2)
                    y = (screen_height / 2) - (height / 2)
                    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                    root.resizable(0, 0)
                    a2=('Ada yang salah pada tanggal.')
                    a3=('Mohon inputkan tanggal dengan benar')
                    p0 = Label(root,bg='red',font= 'Gungsuh 12', text= a2 )
                    p1 = Label(root,bg='red',font= 'Gungsuh 12', text= a3 )
                    p0.pack(fill=X)  
                    p1.pack(fill=X)  
                    root.mainloop()
                    break
        else:
            #membersihkan layar supaya keterangan nampak dengan jelas
            system ('cls')

            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 500
            height = 50
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            a2=("Mohon memasukkan jenis kelamin yang sesuai perintah!!\nAnda akan kembali ke menu awal.")
            p0 = Label(root,bg='red',font= 'Gungsuh 12', text= a2 )
            p0.pack(fill=X)       
            root.mainloop()
            break

        
        import tkinter as tk
        #adalah paket pengaturan jendela
        root = tk.Tk()       
        root.title("\tDataGizi 1.0")
        width = 360
        height = 175
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
    
        namastring= tk.StringVar(root)#menunjukkan inputan adalah string
        def close():
            root.destroy()
        perintah1 = Label(root,text= "Apakah sudah yakin bahwa data diatas benar?\n(1).Sudah\n(2).Belum",font="Times 11 bold",).pack()
        perintah2 = Label(root,bg='red',fg='white',text= "(Input dengan angka)",font="Times 11 bold",).pack(pady=5)
        input1 = Entry(root,textvariable = namastring).pack()
        B = Button(root, text = "NEXT",font = 'Arial 11', command = close)
        B.pack(anchor = S,pady=5)
        root.mainloop() 
        a = namastring.get()
        
        
        if a == ("1"):
            import tkinter as tk       
            root = tk.Tk()       
            root.title("\tDataGizi 1.0")
            #adalah paket pengaturan jendela
            width = 360
            height = 175
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
        
            namastring= tk.StringVar(root)#menunjukkan inputan adalah string
            def close():
                root.destroy()
            perintah1 = Label(root,text= "Apakah ada yang ingin di inputkan lagi?\n(1). Ya\n(2). Tidak",font="Times 11 bold",).pack()
            perintah2 = Label(root,bg='red',fg='white',text= "(Input dengan angka)",font="Times 11 bold",).pack(pady=5)
            input1 = Entry(root,textvariable = namastring).pack()
            B = Button(root, text = "NEXT",font = 'Arial 11', command = close)
            B.pack(anchor = S,pady=5)
            root.mainloop() 
            ulang = namastring.get()

            if ulang == ("1"):
                #berfungsi menulis csv
                import csv
                import os
                header=['NAMA','NOMOR', 'TANGGAL LAHIR', 'TANGGAL DATA', 'USIA', 'JENIS KELAMIN', 'BB(kg)', 'INDEKS', 'STATUS GIZI']
        
                with open(f'datagizi_{tglcsv}.csv','a', newline='\n') as filecsv:
                    datagizibalitacsv = {'NAMA' : nama,'NOMOR' : nomor, 'TANGGAL LAHIR': tgl_lahir, 'TANGGAL DATA' : tgl_data, 'USIA' : usia, 'JENIS KELAMIN' : jk, 'BB(kg)' : bb, 'INDEKS' : indeks, 'STATUS GIZI': status}
        
                    writer = csv.DictWriter(filecsv, fieldnames = header)
                    if os.stat(f'datagizi_{tglcsv}.csv').st_size == 0:
                        writer.writeheader()                 
                    else:
                        None
                    if usia == us:
                        writer.writerow(datagizibalitacsv)      
                    else:
                        None
                    
                                
                                  
                identitas = True            
            elif ulang == ("2"):
                #berfungsi menulis csv
                import csv
                import os
                header=['NAMA','NOMOR', 'TANGGAL LAHIR', 'TANGGAL DATA', 'USIA', 'JENIS KELAMIN', 'BB(kg)', 'INDEKS', 'STATUS GIZI']
        
                with open(f'datagizi_{tglcsv}.csv','a', newline='\n') as filecsv:
                    datagizibalitacsv = {'NAMA' : nama,'NOMOR': nomor, 'TANGGAL LAHIR': tgl_lahir, 'TANGGAL DATA' : tgl_data, 'USIA' : usia, 'JENIS KELAMIN' : jk, 'BB(kg)' : bb, 'INDEKS' : indeks, 'STATUS GIZI': status}
        
                    writer = csv.DictWriter(filecsv, fieldnames = header)
                    if os.stat(f'datagizi_{tglcsv}.csv').st_size == 0:
                        writer.writeheader()                 
                    else:
                        None
                    if usia == us:
                        writer.writerow(datagizibalitacsv)      
                    else:
                        None
                    
                    
                      
                identitas = False       
            else:          
                root = Tk()
                root.title("\tDataGizi 1.0")
                width = 360
                height = 100
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root.resizable(0, 0)
                a2=("INPUT ANDA SALAH!!\nANDA AKAN KEMBALI KE MENU AWAL.\nDATA SEBELUMNYA TELAH TERSIMPAN.")
                p0 = Label(root,font= 'Gungsuh 12', text= a2 )
                p0.pack(fill=X)       
                root.mainloop()
                break   
        elif a == ("2"):
            continue    
        else:
            root = tk.Tk()       
            root.title("\tDataGizi 1.0")
            width = 360
            height = 25
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)

            Label(root,text="Mohon input dengan benar", font='Times 12 bold').pack(fill=X)
            root.mainloop()
            break
             
#fungsi cek data berdasarkan nama            
def datanama():
    namaanak = True  
    while namaanak:
        import csv
        import tkinter as tk
        
        root = tk.Tk()       
        root.title("\tDataGizi 1.0")
        #adalah paket pengaturan jendela
        width = 360
        height = 175
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        
        namastring= tk.StringVar(root)
        tglstring= tk.StringVar(root)
        jenengstring= tk.StringVar(root)
        def close():
            root.destroy()
        perintah3 = Label(root,text= "Nama anak:",font="Times 11 bold").pack()
        input3 = Entry(root,textvariable = jenengstring).pack()
        perintah1 = Label(root,text= "Nomor Induk Anak:",font="Times 11 bold").pack()
        input1 = Entry(root,textvariable = namastring).pack()
        perintah2 = Label(root,text= "Tanggal input data(d-m-yyyy):",font="Times 11 bold").pack()
        input2 = Entry(root,textvariable = tglstring).pack()
        
        
        
        B = Button(root, text = "CARI",font = 'Arial 11', command = close)
        B.pack(anchor = S,pady=5)
        root.mainloop()
        
        
        tglcsv = tglstring.get()
        if len(tglcsv) == 0:
            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 360
            height = 60
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            Label(root,text="TANGGAL TIDAK BOLEH KOSONG!!", font= 'Gungsuh 12' ).pack(fill=X)
            break
        nmr = namastring.get()    
        jeneng = jenengstring.get()
        #=======================menambahkan file csv ke dalam list
        data =[]
        try:
            with open(f'datagizi_{tglcsv}.csv','r') as f:
                readCSV = csv.reader(f,delimiter=',')
                for row in readCSV:
                    data.append(row)
            #========================mencari nama anak
            datacari =[]
            i = 0
            for a in data:
                if jeneng == a[0]:
                    if nmr == a[1]:
                        #===========memasukkan data ke dalam list sesuai inputan apabila nama dan nomor ada pada csv
                        datacari = data[i]
                    else:
                        root = Tk()
                        root.title("\tDataGizi 1.0")
                        width = 600
                        height = 25
                        screen_width = root.winfo_screenwidth()
                        screen_height = root.winfo_screenheight()
                        x = (screen_width / 2) - (width / 2)
                        y = (screen_height / 2) - (height / 2)
                        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        root.resizable(0, 0)
                        Label(root,text="NOMOR TIDAK COCOK ", font= 'Gungsuh 12' ).pack(fill=X)
                        root.mainloop()
                        
                i = i+1        
            if (len(datacari)>0):
                root= tk.Tk()
                root.title("\tDataGizi 1.0")     
                width = 440
                height = 280
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root.resizable(0, 0)
                            
                Label(root,text=f"Nama\t\t:{datacari[0]}",font= 'Cambria 12').pack()
                Label(root,text=f"Nomor\t\t:{datacari[1]}",font= 'Cambria 12').pack()
                Label(root,text=f"Tanggal Lahir\t:{datacari[2]}",font= 'Cambria 12').pack()
                Label(root,text=f"Tanggal Data\t:{datacari[3]}",font= 'Cambria 12').pack()
                Label(root,text=f"Usia\t:{datacari[4]}",font= 'Cambria 12').pack()
                Label(root,text=f"Jenis Kelamin\t:{datacari[5]}",font= 'Cambria 12').pack()
                Label(root,text=f"BB\t:{datacari[6]}kg",font= 'Cambria 12').pack()
                Label(root,text=f"Indeks\t:{datacari[7]}",font= 'Cambria 12').pack()
                Label(root,text=f"Status Gizi\t\t:{datacari[8]}",font= 'Cambria 12').pack()
                            
                B = Button(root, text = "CLOSE", command = close)
                B.pack(anchor = S)
                B.place(x= 195, y= 245)
                root.mainloop()
             
            else:
                root = Tk()
                root.title("\tDataGizi 1.0")
                width = 360
                height = 25
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root.resizable(0, 0)
                a2=("DATA TIDAK DITEMUKAN.")            
                p0 = Label(root,font= 'Gungsuh 12', text= a2 )           
                p0.pack(fill=X)       
                root.mainloop()
           
        except FileNotFoundError:#========== pemenuhan aspek penanganan eksepsi
            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 600
            height = 25
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            Label(root,text="ADA KESALAHAN PADA PENULISAN FORMAT TANGGAL/FILE TIDAK ADA ", font= 'Gungsuh 12' ).pack(fill=X)
            root.mainloop()
        
                
                 
        import tkinter as tk       
        root = tk.Tk()       
        root.title("\tDataGizi 1.0")
        #adalah paket pengaturan jendela
        width = 360
        height = 175
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        
        namastring= tk.StringVar(root)#menunjukkan inputan adalah string
        def close():
            root.destroy()
        perintah1 = Label(root,text= "Apakah ada yang ingin di cek lagi?\n(1). Ya\n(2). Tidak",font="Times 11 bold",).pack()
        perintah2 = Label(root,bg='red',fg='white',text= "(Input dengan angka)",font="Times 11 bold",).pack(pady=5)
        input1 = Entry(root,textvariable = namastring).pack(pady=5)
        
        
        B = Button(root, text = "NEXT",font = 'Arial 11', command = close)
        B.pack(anchor = S,pady=5)
        root.mainloop()
        
        ulang = namastring.get()

        if ulang == ("1"):
            namaanak = True
        elif ulang == ("2"):
            namaanak = False
        else:
            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 360
            height = 100
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            a2=("INPUT ANDA SALAH!!\nANDA AKAN KEMBALI KE MENU AWAL.\nSILAHKAN ULANG KEMBALI PROGRAM.")

            p0 = Label(root,bg='red',font= 'Gungsuh 12', text= a2 )

            p0.pack(fill=X)       
            root.mainloop()
            break   

#fungsi membaca csv        
def baca():
    
    import tkinter.ttk as ttk
    import csv

    root = Tk()
    root.title("Tabel Data Gizi Balita")
    width = 720
    height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    
    tglcsv = tk.StringVar(root)
    def close():
            root.destroy()
    perintah= Label(root,text="Ketik tanggal untuk melihat data gizi sesuai tanggal pendataan(d-m-yyyy)",font= 'Cambria 12').pack()
    input1= Entry(root,textvariable= tglcsv).pack()

    B = Button(root, text = "SUBMIT",font = 'Arial 11', command = close)
    B.pack(anchor = S,pady=5)
    root.mainloop()
    tl= tglcsv.get()
    if len(tl) == 0:
        root = Tk()
        root.title("\tDataGizi 1.0")
        width = 360
        height = 60
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        Label(root,text="TANGGAL TIDAK BOLEH KOSONG!!", font= 'Gungsuh 12' ).pack(fill=X)
        root.mainloop()

        interface = True
    #==================penanganan eksespsi
    try: 
        with open(f'datagizi_{tl}.csv') as f:
            root = Tk()
            root.title("Tabel Data Gizi Balita")
            width = 720
            height = 400
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)

            TableMargin = Frame(root, width=720)
            TableMargin.pack(side=TOP)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("NAMA","NOMOR", "TANGGAL LAHIR", "TANGGAL DATA",'USIA','JENIS KELAMIN','BB','INDEKS GIZI','STATUS GIZI'), height=400, selectmode="extended",
                                yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('NAMA', text="NAMA", anchor=W)
            tree.heading('NOMOR', text="NOMOR", anchor=W)
            tree.heading('TANGGAL LAHIR', text="TANGGAL LAHIR", anchor=W)
            tree.heading('TANGGAL DATA', text="TANGGAL DATA", anchor=W)
            tree.heading('USIA', text="USIA (bulan)", anchor=W)
            tree.heading('JENIS KELAMIN', text="JENIS KELAMIN", anchor=W)
            tree.heading('BB', text="BB (kg)", anchor=W)
            tree.heading('INDEKS GIZI', text="INDEKS GIZI", anchor=W)
            tree.heading('STATUS GIZI', text="STATUS GIZI", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=120)
            tree.column('#2', stretch=NO, minwidth=0, width=120)
            tree.column('#3', stretch=NO, minwidth=0, width=120)  
            tree.column('#4', stretch=NO, minwidth=0, width=120)
            tree.column('#5', stretch=NO, minwidth=0, width=120)
            tree.column('#6', stretch=NO, minwidth=0, width=120)
            tree.column('#7', stretch=NO, minwidth=0, width=120)
            tree.column('#7', stretch=NO, minwidth=0, width=120)
            
            tree.pack()
            
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                nama = row['NAMA']
                nmr = row['NOMOR']
                tl = row['TANGGAL LAHIR']
                dt = row['TANGGAL DATA']
                u = row['USIA']
                jk = row['JENIS KELAMIN']
                bb = row['BB(kg)']
                i = row['INDEKS']
                st = row['STATUS GIZI']
                tree.insert("", 0, values=(nama,nmr,tl,dt,u,jk,bb,i,st))
            root.mainloop()
    except FileNotFoundError:
            root = Tk()
            root.title("\tDataGizi 1.0")
            width = 600
            height = 25
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)
            Label(root,text="ADA KESALAHAN PADA PENULISAN FORMAT TANGGAL/FILE TIDAK ADA ", font= 'Gungsuh 12' ).pack(fill=X)
            root.mainloop()
   
#=============================fungsi tampilan menu    
interface = True                   
while interface:

    import tkinter as tk  
    #system('cls')     
    root = tk.Tk()       
    root.title("\tDataGizi 1.0")
    #adalah paket pengaturan jendela
    width = 500
    height = 270
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    
    namastring= tk.StringVar(root)#menunjukkan inputan adalah string
    def close():
        root.destroy()
    perintah1 = Label(root,text="Kami memiliki 4 fitur utama dalam program ini:",font="Cambria 14 ",).pack()
    perintah2 = Label(root,text="================================================").pack()
    i2 = Label(root, text="(1) untuk melakukan pendataan gizi balita",font='Cambria 12',justify=LEFT)
    i2.place(x= 200, y= height/2)
    i3 = Label(root, text="(2) untuk mengecek data balita (perorangan)",font='Cambria 12',justify=LEFT)
    i3.place(x= 200, y= height/2)
    i4 = Label(root, text="(3) untuk melihat data balita yang tercatat dalam CSV",font='Cambria 12',justify=LEFT)
    i4.place(x= 200, y= height/2)
    i5 = Label(root, text="(4) untuk keluar dari program",font='Cambria 12',justify=LEFT)
    i5.place(x= 200, y= height/2)
    i6 = Label(root, text="Silahkan pilih salah satu fitur kemudian ketik (angka)",font='Cambria 12')
    i6.place(x= width/2, y= height/2)    
    i2.pack()
    i3.pack()
    i4.pack()
    i5.pack()
    i6.pack()
    perintah2 = Label(root,text="================================================").pack()
    
    input1 = Entry(root,textvariable = namastring,fg='black',bg='white').pack()
    B = Button(root, text = "PILIH",font = 'Arial 11', command = close)
    B.pack(anchor = S)    
    B.place(x=225,y=225)   
    root.mainloop() 
        
    start = namastring.get()

    if start== ("1"):
        databalita()
    elif start== ("2"):
        datanama()
    elif start== ("3"):
        import csv
        import os
        tanggaldata = datetime.datetime.now()
        yearvalue = tanggaldata.year
        monthvalue = tanggaldata.month
        dayvalue = tanggaldata.day
        tglcsv= (f"{dayvalue}-{monthvalue}-{yearvalue}")
        header=['NAMA','NOMOR', 'TANGGAL LAHIR', 'TANGGAL DATA', 'USIA', 'JENIS KELAMIN', 'BB(kg)', 'INDEKS', 'STATUS GIZI']
        
        with open(f'datagizi_{tglcsv}.csv','a', newline='\n') as filecsv:
            writer = csv.DictWriter(filecsv, fieldnames = header)
            if os.stat(f'datagizi_{tglcsv}.csv').st_size == 0:
                writer.writeheader()                 
            else:
                None
        baca()
    elif start == ("4"):

        root = tk.Tk()

        root.title("\tDataGizi 1.0")
        width = 360
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        p0 = Label(root,bg='green',fg='white',font= 'Gungsuh 12', text="PROGRAM SELESAI")
        p0.pack(fill=X,pady=5)
        p1 = Label(root,bg='green',fg='white',font= 'Gungsuh 12', text="DATA ANDA TELAH TERSIMPAN")
        p1.pack(fill=X,pady=5)
        p2 = Label(root,bg='green',fg='white',font= 'Gungsuh 12', text="TERIMA KASIH")
        p2.pack(fill=X,pady=5)

        root.mainloop()
        break    
    else:
        system ("cls")

        root = tk.Tk()
        root.title("\tDataGizi 1.0")
        width = 360
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        p0 = Label(root,bg='red',font= 'Gungsuh 12', text="INPUT SALAH")
        p0.pack(fill=X,pady=5)
        p1 = Label(root,bg='red',font= 'Gungsuh 12', text="PROGRAM BERHENTI")
        p1.pack(fill=X,pady=5)
        p2 = Label(root,bg='red',font= 'Gungsuh 12', text="SILAHKAN MULAI ULANG PROGRAM KEMBALI")
        p2.pack(fill=X,pady=5)
        root.mainloop()
        break    
        

