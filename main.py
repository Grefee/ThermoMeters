import requests
import xml.etree.ElementTree as ET
import datetime as d
import io
import teplomer
import psycopg2
import readTermMeterList as R
import time



def mainPepega():

    R.readTermMeter()
    R.readDbsTermometers(R.termListFromXml)



    i = 5
    while i > 1:
        for item in R.termListFromXml:

            R.sendDataToDb(item.id)

        #počkej 20s
        time.sleep(20)


mainPepega()