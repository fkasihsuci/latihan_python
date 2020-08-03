# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:17:23 2020

@author: Sony
"""

import psycopg2

def cek_name(_cust_id):
    conn = None
    try:
        try : 
            conn = psycopg2.connect(host="localhost",
                                    port=5432,
                                    database="postgres",
                                    user="postgres",
                                    password="xxx")
        except : print("ERROR: Failed to connect database")
        if conn is not None : print("-----------INFO: Database success to connect-----------")
        
        sql = conn.cursor()
        
        cmd = "SELECT customer_id, first_name, last_name  FROM customer where customer_id = " + _cust_id
      
        sql.execute(cmd)
        jumlahData = sql.rowcount
        
        if jumlahData > 0:
            data = sql.fetchone()
            print("Ada sebanyak {} dalam data".format(jumlahData))

            if data is not None:
                print("Customer id : {}".format(data[0]))
                print("Customer name : {}".format(data[1]))
               
        else:
            print("INFO: Data Tidak ditemukan")
            sql.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("-----------------ERROR: Command gagal dieksekusi-------------------")
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print('-----------------Database connection closed.-------------------')
   
        return data   

def cek_rental_history (_cust_id):
    conn = None 
    try:
        try : 
            conn = psycopg2.connect(host="localhost",
                                    port=5432,
                                    database="postgres",
                                    user="postgres",
                                    password="xxx")
        except : print("ERROR: Failed to connect database")
        if conn is not None : print("----------------INFO: Database success to connect--------------")
        
        sql = conn.cursor()
        
        cmd = "select rental_date,return_date from rental where customer_id ="+cust_id+ "order by inventory_id asc"

        sql.execute(cmd)
        jumlahData= sql.rowcount
        
        if jumlahData > 0 :
            data = sql.fetchall()
            print ("Ada sebanyak {} history peminjaman".format(jumlahData))
        else : 
            print("Data Tidak ditemukan")
            sql.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("-----------------ERROR: Command gagal dieksekusi-------------------")
        print(error)
        
    finally :
        if conn is not None:
            conn.close()
            print('-----------------Database connection closed.-------------------')
        return data

if __name__ == '__main__':
    print("----Main start----")
    cust_id = input("Masukkan Customer Id \n:: ")
    rental_history = None
    nama = cek_name(cust_id)
    if cust_id is not None: 
        print("MAIN INFO: Data Ditemukan : {}".format(nama))
        
        rental_history = cek_rental_history(cust_id)
    #if rental_history is not None:
       # print("MAIN INFO: Total Data :", len(rental_history))
    for row in range (len(rental_history)):
        print("Rental {} | Return {}".format(rental_history[0][0],rental_history[0][1]))
    print ("selesai")
    
      
        
