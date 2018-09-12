# settings file: user changes name and location details
import sqlite3


class Settings:
    def __init__(self):
        self.db = sqlite3.connect("UserData.db")
        self.cursor = self.db.cursor()

    def changeName(self, name):
        self.cursor.execute("""UPDATE userInfo SET Name='{}'""".format(name))
        self.db.commit()

    def changeLocation(self, country, city):
        self.cursor.execute("""UPDATE userInfo SET Country='{}'""".format(country))
        self.cursor.execute("""UPDATE userInfo SET City='{}'""".format(city))
        self.db.commit()


class Setup:
    def __init__(self):
        self.db = sqlite3.connect("UserData.db")
        self.cursor = self.db.cursor()

    # Main setup method
    def completeSetup(self, name, country, city):
        sql = "CREATE TABLE userInfo (Name text, Country text, City text, LastTwitterSearch text, primary key(Name))"
        self.cursor.execute(sql)

        sql = """INSERT INTO userInfo (Name, Country, City, LastTwitterSearch) VALUES ('{}', '{}', '{}', 'kedst')""".format(name, country, city)
        self.cursor.execute(sql)

        # Alarms table
        sql = """CREATE TABLE Alarms (AlarmID integer, Title text, Days text, Time time, Date float, Repeats boolean, primary key(AlarmID))"""
        self.cursor.execute(sql)

        # Notes table
        sql = """CREATE TABLE Notes (NoteID integer, Title text, Content text, Date float, primary key(NoteID))"""
        self.cursor.execute(sql)

        # Reminders table
        sql = """CREATE TABLE Reminders (ReminderID integer, Title text, Content text, Days text, Time time, Date float, Repeats boolean, primary key(ReminderID))"""
        self.cursor.execute(sql)

        self.db.commit()
