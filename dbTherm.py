import psycopg2

try:
    connection = psycopg2.connect(
        host = "WCZLIB1040\SQLEXPRESS01",
        database = "Teplomery",
        username = "GLOBAL\hujerp",
        password = "69y101E345a8+-*/",
    )

except:
    print("Cannot access dbs..")