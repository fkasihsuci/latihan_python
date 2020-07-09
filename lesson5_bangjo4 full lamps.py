# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:48:56 2020

@author: Sony
"""


import time, threading
#import sys

merah  = 0
kuning = 1
hijau  = 2
warna = ["merah","kuning","hijau"]

lampuUtara = hijau
lampuSelatan = merah
lampuTimur = merah
lampuBarat = merah

def utara():
    print("INFO: Fungsi Utara Mulai")
    global lampuSelatan
    global lampuUtara
    global lampuBarat
    global lampuTimur
    counterProses = 3
    time.sleep(0.5)
    while 1:
        while (lampuUtara == merah): 
            time.sleep(0.25)
        berapaDetik = 3
        while (lampuUtara == kuning): 
           print ("Utara : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
           if berapaDetik == 0: 
               lampuUtara = hijau
               counterProses -= 1
           berapaDetik -= 1
           time.sleep(0.25)
        berapaDetik = 10
        while (lampuUtara == hijau):
            print("Utara : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
            if berapaDetik == 0: 
                lampuUtara=merah
                lampuSelatan=merah
                lampuTimur=merah
                lampuBarat=kuning 
                counterProses -= 1            
                print("--------------------------\n")
            berapaDetik -= 1
            time.sleep(0.25)          
        if counterProses == 0: break
    print("\nINFO: thread utara exit")

def selatan():
    print("INFO: Fungsi Selatan Mulai")
    global lampuSelatan
    global lampuUtara
    global lampuTimur
    global lampuBarat
    counterProses = 3
    time.sleep(0.5)
    while 1:
        while (lampuSelatan == merah): 
            time.sleep(0.25)
        berapaDetik = 3
        while (lampuSelatan == kuning): 
           print ("Selatan : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
           if berapaDetik == 0: 
               lampuSelatan = hijau
               counterProses -= 1
           berapaDetik -= 1
           time.sleep(0.25)
        berapaDetik=10
        while (lampuSelatan == hijau):
            print("Selatan : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
            #berapaDetik -= 1
            if berapaDetik == 0: 
                lampuUtara=merah
                lampuSelatan=merah
                lampuTimur= kuning
                lampuBarat=merah
                counterProses -= 1
                print("--------------------------\n")
            berapaDetik -= 1
            time.sleep(0.25)
        if counterProses == 0: break
    print("\nINFO: thread selatan exit")
    
def timur():
    print("INFO: Fungsi Timur Mulai")
    global lampuSelatan
    global lampuUtara
    global lampuBarat
    global lampuTimur
    counterProses = 3
    time.sleep(0.5)
    while 1:
        while (lampuTimur == merah): 
            time.sleep(0.2)
        berapaDetik = 3
        while (lampuTimur == kuning): 
           print ("Timur : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
           if berapaDetik == 0: 
               lampuTimur = hijau
               counterProses -= 1
           berapaDetik -= 1
           time.sleep(0.2)
        berapaDetik = 10
        while (lampuTimur == hijau):
            print("Timur : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
            #berapaDetik -= 1
            if berapaDetik == 0: 
                lampuUtara= kuning
                lampuSelatan=merah
                lampuTimur=merah
                lampuBarat=merah
                counterProses -= 1            
                print("--------------------------\n")
            berapaDetik -= 1
            time.sleep(0.2)          
        if counterProses == 0: break
    print("\nINFO: thread timur exit")

def barat():
    print("INFO: Fungsi Barat Mulai")
    global lampuSelatan
    global lampuUtara
    global lampuTimur
    global lampuBarat
    counterProses = 3
    time.sleep(0.5)
    while 1:
        while (lampuBarat == merah): 
            time.sleep(0.2)
        berapaDetik = 3
        while (lampuBarat == kuning): 
           print ("barat : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
           if berapaDetik == 0: 
               lampuBarat = hijau
               counterProses -= 1
           berapaDetik -= 1
           time.sleep(0.2)
        berapaDetik=10
        while (lampuBarat == hijau):
            print("Barat : U {} | S {} | T {} | B {} | Detik {}".format(warna[lampuUtara],warna[lampuSelatan],warna[lampuTimur],warna[lampuBarat],berapaDetik))
            if berapaDetik == 0:  
                lampuUtara=merah
                lampuSelatan=kuning
                lampuTimur=merah
                lampuBarat=merah
                counterProses -= 1
                print("--------------------------\n")
            berapaDetik -= 1
            time.sleep(0.2)
        if counterProses == 0: break
    print("\nINFO: thread barat exit")
    
        
if __name__ == "__main__":
    print("INFO: main start")
    threadUtara  = threading.Thread(target=utara, args=())
    threadSelatan= threading.Thread(target=selatan, args=())
    threadTimur= threading.Thread(target=timur, args=())
    threadBarat= threading.Thread(target=barat, args=())
    try:
        threadUtara.start()
        threadSelatan.start()
        threadTimur.start()
        threadBarat.start()
    except:
        print("ERROR: thread failed to create")