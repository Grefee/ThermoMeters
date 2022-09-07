import xml.etree.ElementTree as ET
import io
import teplomer
import gc
import psycopg2


global termListFromXml
termListFromXml = []

def readTermMeter():
    with io.open("xmlConfig.xml", "r",encoding="utf-8") as xmlPage:
        f = ET.parse(xmlPage)
        root = f.getroot()
    for child in root:
        if (child.tag == "temp"):
            for var in child:
                if(var.tag == "id"):
                    id = var.text
                    int(id)
                if(var.tag == "name"):
                    name = var.text
                if(var.tag == "ip"):
                    ip_add = var.text
            print(id, name, ip_add)
            objName = "teplomer" + str(id)
            objName = teplomer.Teplomer(id, name, ip_add)

            termListFromXml.append(objName)
            #over jestli uz teplomer neexistuje pokud ano, zmenit ip addresu pokud ne zalozit novej

def readDbsTermometers(termListFromXml):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    sql = 'SELECT teplomer_id, teplomer_ip, teplomer_name FROM teplomer;'

    cursor.execute(sql)
    sqlData = cursor.fetchall()


    ### DBs DATA ULOZENY V OBJEKTU SQLDATA
    print("Print each row and it's columns values")
    for row in sqlData:
        print("ID  = ", row[0], "\n")
        print("IP  = ", row[1], "\n")
        print("Name  = ", row[2], "\n")


    ### LIST DATA ULOZENY V LISTU

    for teplomerItem in termListFromXml:
        list_ip = teplomerItem.name
        list_name = teplomerItem.id

        # print("///////////////")
        # print("///////////////")
        # print(list_ip)
        # print(list_name)

        checkDbData(list_ip,list_name)

        for row in sqlData:
            print("porovnávám dbs IP: "+row[1]+"  s IP xmlka: " +list_ip)
            print("porovnávám dbs Name: "+row[2]+" s Name xmlka: "+list_name +  "\n")

            #
            # if (list_ip == row[1]):
            #     for row in sqlData:
            #         if(list_name == row[2]):
            #             print("schoda")
            # elif (list_ip == row[1]):
            #     for row in sqlData:
            #         if(list_name != row[2]):
            #             print("neschoda")
            # elif (list_ip != row[1]):
            #     for row in sqlData:
            #         if(list_name == row[2]):
            #             print("neschoda")
            # else:
            #     insertToDbs(list_ip, list_name)

            if (list_name == row[2]):
                print("stejné jméno")
                if (list_ip == row[1]):
                    "stejné obojí.."
                else:
                    print("stejne jmeno jiná ip..")

            insertToDbs(list_ip, list_name)

            #
            # if (list_name == row[2] and list_ip == row[1]):
            #     print("do nothing! - same name")
            #
            # elif(list_name == row[2] and list_ip != row[1]):
            #     print("jina ip add .. treba insert()" )
            # elif (list_name != row[2] and list_ip != row[1]):
            #     print("//////////onoji jiny .. treba insert()")
            # elif(list_name != row[2]):
            #     print("neexistuje Insert new()")
            #     insertToDbs(list_ip, list_name)


def checkDbData(list_ip, list_name):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    queryX = 'SELECT teplomer_id, teplomer_ip, teplomer_name FROM teplomer WHERE teplomer_name LIKE (%s)'


    cursor.execute(queryX, list_name)
    sqlRespose = cursor.fetchall()

    print(sqlRespose)


def insertToDbs(ip_add,name):
#zapsat do database
#establish conn
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    queryX = 'INSERT INTO teplomer (teplomer_ip, teplomer_name) VALUES (%s, %s)'
#            print("-------"+ip_add+"----------"+name)
    val = (ip_add, name)
    print(queryX)

    cursor.execute(queryX, val)
    conn.commit()

    conn.close()
def changeIp(ip_add):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    queryX = 'UPDATE INTO teplomer (teplomer_ip, teplomer_name) VALUES (%s, %s)'


readTermMeter()
# print(termListFromXml)


readDbsTermometers(termListFromXml)

#teplomer01


