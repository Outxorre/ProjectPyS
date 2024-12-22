import requests
import sqlite3
import cv2
import time
import sys
import logging
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

holderName = str(input("Введите имя сайта"))
holderLink = str(input("Ссылку на сайт с https"))

try:
    cur.execute("INSERT INTO sites (siteName, siteLink) VALUES (?, ?);", (holderName, holderLink))
    logging.info("SQL Запрос успешно выполнен, проверьте базу данных")

except Exception as e:
    logging.error(f"Произошла ошибка при выполнении SQL запроса: {e}")


cur.execute("SELECT * FROM sites;")

students = cur.fetchall()

for student in students:
    print(student)


connection.commit()
connection.close()

image_path = 'bro.jpg'
image1 = cv2.imread(image_path)
image_path = 'dima.jpg'
image2 = cv2.imread(image_path)
image_path = 'image.png'
image3 = cv2.imread(image_path)
image_path = 'scale_1200.jfif'
image4 = cv2.imread(image_path)


cv2.imshow('Zazu', image1)
time.sleep(5)
print("wait")
print("DESTROY")
cv2.destroyAllWindows()

sys.exit(0)