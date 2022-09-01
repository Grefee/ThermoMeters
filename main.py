import requests
import xml.etree.ElementTree as ET
import datetime as d
import io
import readTermMeterList
import teplomer



def mainPepega():

    #nacist konfig xml list teplomeru a zinicializovat vsechny teplomery..
    readTermMeterList()

    #nekonecnej loop, s get data a save data
    i = 5
    while i < 4:
    teplomer.Teplomer.getData()
