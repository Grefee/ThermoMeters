import psycopg2


def checkDbData(list_ip, list_name):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    ip = list_ip

    print(list_name)

    queryX = "SELECT (teplomer_id, teplomer_ip, teplomer_name) FROM teplomer WHERE (teplomer_name = "+{}+")"

    dat = str(list_name)

 #   "SELECT teplomer_id, teplomer_ip, teplomer_name FROM teplomer;"

    cursor.execute(queryX, dat)
    sqlRespose = cursor.fetchall()

    print(sqlRespose)


checkDbData("192.168.1.1", "TCZLIB305")

