from flaskext.mysql import MySQL
from app import app
import random
import string
import datetime

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'flask'
app.config['MYSQL_DATABASE_PASSWORD'] = 'q7$L2J9REhiVfJytDgz%'
app.config['MYSQL_DATABASE_DB'] = 'urlshortener'
app.config['MYSQL_DATABASE_HOST'] = 'dev-mysql'
mysql.init_app(app)
con = mysql.connect()
cursor = con.cursor()


def addUrl(generatedId, fullUrl): #adds data to the database
    now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    addcommand = f"INSERT INTO `urls`(ID,url,created) VALUES ('{generatedId}','{fullUrl}','{now}');"
    cursor.execute(addcommand)
    con.commit()
    pass

def getUrl(id):
    command = f"SELECT url FROM `urls` WHERE `ID` = '{id}';"
    cursor.execute(command)
    x = cursor.fetchone()
    return str(x)

def getID(): # gets random 6 character id, ensures that it doesn't exist in the db already
    id = generateID()
    while checkIfIdExists(id):
        id = generateID()
        continue
    return id

def generateID(): #generates random 6 character id
    id = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(6))
    return id

def checkIfIdExists(id):
    #command to check if an ID already exists in the database, 1 exists, 0 doesn't
    command = (f"SELECT EXISTS(SELECT * FROM `urls` WHERE `ID` = '{id}');")
    cursor.execute(command)
    x = cursor.fetchone()
    x = x[0] #recreate x here, the output from the comand is 0, or 1, otherwise
    return x


    

    