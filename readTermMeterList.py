import xml.etree.ElementTree as ET
import io
import teplomer
import gc
import psycopg2
import requests
import datetime as d


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


        for row in sqlData:
            checkDbData(list_ip, list_name)


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
def changeIp(ip_add,name):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    queryX = 'UPDATE teplomer SET teplomer_ip = %s WHERE teplomer_name = %s'

    dat = ip_add, name

    cursor.execute(queryX, (dat))

    conn.commit()
    conn.close()




def checkDbData(list_ip, list_name):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    ip = list_ip

    updatedIp = "('" + ip + "',)"

    print(list_name)

    queryX = "SELECT (teplomer_ip) FROM teplomer WHERE teplomer_name LIKE %s"

    dat = str(list_name)

    cursor.execute(queryX, (dat,))
    sqlRespose = cursor.fetchall()

    print(sqlRespose)
    print("/n" "ip is: " + ip)
    if(sqlRespose == []):
        print("záznam chybí")
        #potřeba insert
        insertToDbs(ip, list_name)

    else:
        print("záznam je a chcekni jestli ip sedí")
        if(sqlRespose[0] == updatedIp):
            print("ip is same")
        else:
            print("ip is diff")
            #update ip in db
            changeIp(ip,list_name)


def sendDataToDb(name):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    queryA = "SELECT teplomer_id, teplomer_ip FROM teplomer WHERE teplomer_name LIKE %s ORDER BY teplomer_id DESC"
    val = name

    cursor.execute(queryA,(name,))
    teplomer_data = cursor.fetchone()

    print(teplomer_data)

    ip_add_FromDB = teplomer_data[1]
    id_add_FromDB = teplomer_data[0]

    strIP = str(ip_add_FromDB)
    print(ip_add_FromDB)
    print(id_add_FromDB)

    page = requests.get("http://" + strIP + "/xml/?mode=sensor&type=list&id=01")
    xmlPage = page.content.decode("utf-8")
    f = io.StringIO(xmlPage)
    tree = ET.parse(f)
    root = tree.getroot()

    for child in root:
        if (child.tag == "name"):
            term_name = child.text
        if (child.tag == "current"):
            term_value = child.text


    timeStamp = str(d.datetime.now())

    print(term_value)
    print(timeStamp)


    query = "INSERT INTO teplota (teplota_value, teplomer_id, teplota_cas) VALUES (%s, %s, %s)"

    inputVal = term_value,id_add_FromDB,timeStamp

    cursor.execute(query,inputVal)
    conn.commit()
    conn.close()

sendDataToDb("TCZLIB151")


#insertToDbs("10.10.151.144","TCZLIB308")


#readTermMeter()
# print(termListFromXml)


#readDbsTermometers(termListFromXml)

#teplomer01


