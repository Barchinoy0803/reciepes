import pymysql

class Database:
    def __init__(self):
        self.connectToDataBase()
        self.createDataBase()
        self.createTable()

    def connectToDataBase(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='0803'
        )
        self.cursor = self.db.cursor()

    def createDataBase(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS reciepe')
        self.cursor.execute('USE reciepe')

    def createTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reciepes(
                            reciepe_id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(30),
                            ingredients TEXT,
                            instructions TEXT)''')
        
    def addReciepe(self, name, ingredients, instructions):
        self.cursor.execute("SELECT * FROM reciepes WHERE name = %s", (name)) 
        result = self.cursor.fetchall()
        if len(result) == 0:
            self.cursor.execute("INSERT INTO reciepes(name, ingredients, instructions) VALUES (%s, %s, %s)", (name, ingredients, instructions))
            self.db.commit()
            return "Successfully✔"
        else:
            return "This reciepe is already exist. Please, choose another name."    

    def getAllReciepes(self):
        self.connectToDataBase()
        self.createDataBase()
        self.cursor.execute('SELECT * FROM reciepes')
        return self.cursor.fetchall()

    def getReciepeByName(self, name):
        self.cursor.execute('SELECT * FROM reciepes where name = %s', (name))
        return self.cursor.fetchall()[0]
    
    def updateReciepe(self, oldName, newData):
        self.cursor.execute('UPDATE reciepes SET name = %s, ingredients = %s, instructions = %s WHERE name = %s',(newData['name'], newData['ingredients'], newData['prepare'], oldName))
        self.db.commit()


    def deleteReciepe(self, name):
        self.cursor.execute('DELETE FROM reciepes WHERE name = %s', (name))
        self.db.commit()

    def searchByIngredients(self, ingredient):
        ingredient = "%" + ingredient + "%"  
        self.cursor.execute('SELECT * FROM reciepes WHERE ingredients LIKE %s', (ingredient))
        return self.cursor.fetchall()

    def searchByReciepes(self, reciepe):
        self.cursor.execute('SELECT * FROM reciepes WHERE name = %s', (reciepe))
        return self.cursor.fetchall()