import requests
import sqlite3
import logging
import sys
import subprocess
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("sites.db")

logging.info("Соединение с базой данных установлено")

cur = connection.cursor()
cur.execute(""" 
CREATE TABLE IF NOT EXISTS sites(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    siteName TEXT,
    siteLink TEXT
);
""")

class DataBase:
    def __init__(self):
        pass

    def dbCheck(self, cursor):
        cursor.execute("SELECT * FROM sites;")
        sites = cursor.fetchall()
        for site in sites:
            print(site)

    def dbAdjust(self):
        subprocess.run([sys.executable, "DBadjst.py"], check=True)
        print("Скрипт DBadjst.py завершил выполнение.")
        return

    def dbDelete(self, cursor, site_id):
        try:
            cursor.execute("DELETE FROM sites WHERE id = ?;", (site_id,))
            print(f"Запись с ID {site_id} успешно удалена.")
        except Exception as e:
            print(f"Ошибка при удалении записи: {e}")

db = DataBase()
db.dbCheck(cur)
db.dbAdjust()
db.dbDelete(cur, 1)


connection.commit()
connection.close()