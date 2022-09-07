import requests
import xml.etree.ElementTree as ET
import datetime as d
import io
import teplomer
import psycopg2



def mainPepega():

    #nacist konfig xml list teplomeru a zinicializovat vsechny teplomery..
#    readTermMeterList()

    #nekonecnej loop, s get data a save data

    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    sql = "SELECT teplomer_id, teplomer_ip, teplomer_name FROM teplomer;"

    cursor.execute(sql)
    data = cursor.fetchall()

    retard = "10.10.197.151"
    print(retard)
    print(type(retard))
    for row in data:
         print("------")
         print(row[0])
         print(row[1])
         print(type(row[1]))
         print(row[2])
         pepega = row[1]
         if (pepega == retard):
              print("////////////////////schoda")


mainPepega()