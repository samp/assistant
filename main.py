import sqlite3

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from weather import Weather4Day, Weather10Day
from twitter import Twitter
from settings import Settings
from NotesRemindersAlarms import NotesRemindersAlarms, Notes, Reminders, Alarms
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button

# do moretwitter layout - dates etc

# do nra layouts
# do nra functions

# Make label height scale with number of lines
# clean up user input = first letter caps on names and locations
# clean code
# error trapping!!!


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM userInfo")
            username = cursor.fetchone()

        self.labelName = "Welcome, " + username[0] + "!"


class WeatherScreen(Screen):
    latestWeatherText = StringProperty()
    latestWeatherHigh = StringProperty()
    latestWeatherLow = StringProperty()
    latestLocation = StringProperty()

    def __init__(self, **kwargs):
        super(WeatherScreen, self).__init__(**kwargs)
        self.getWeather()

    def getWeather(self):
        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT city FROM userInfo")
            city = cursor.fetchone()
            cursor.execute("SELECT country FROM userInfo")
            country = cursor.fetchone()
        city = city[0]
        country = country[0]

        w = Weather4Day(country, city)
        self.latestLocation = "The weather in {}, {} is:".format(city, country)
        self.latestWeatherText = w.forecastTodayText()
        self.latestWeatherHigh = w.forecastTodayHigh() + "°C"
        self.latestWeatherLow = w.forecastTodayLow() + "°C"

    def getMoreWeather(self):
        city = self.inputCity.text
        country = self.inputCountry.text
        
        if city == "" or country == "":
            pass
        else:
            moreweather = self.manager.get_screen("moreweather")

            w = Weather10Day(country, city)

            textData = w.forecast10DaysText()
            moreweather.labelDay1Text.text = textData[0]
            moreweather.labelDay2Text.text = textData[1]
            moreweather.labelDay3Text.text = textData[2]
            moreweather.labelDay4Text.text = textData[3]
            moreweather.labelDay5Text.text = textData[4]
            moreweather.labelDay6Text.text = textData[5]
            moreweather.labelDay7Text.text = textData[6]
            moreweather.labelDay8Text.text = textData[7]
            moreweather.labelDay9Text.text = textData[8]
            moreweather.labelDay10Text.text = textData[9]

            highData = w.forecast10DaysHigh()
            moreweather.labelDay1High.text = highData[0] + "°C"
            moreweather.labelDay2High.text = highData[1] + "°C"
            moreweather.labelDay3High.text = highData[2] + "°C"
            moreweather.labelDay4High.text = highData[3] + "°C"
            moreweather.labelDay5High.text = highData[4] + "°C"
            moreweather.labelDay6High.text = highData[5] + "°C"
            moreweather.labelDay7High.text = highData[6] + "°C"
            moreweather.labelDay8High.text = highData[7] + "°C"
            moreweather.labelDay9High.text = highData[8] + "°C"
            moreweather.labelDay10High.text = highData[9] + "°C"

            lowData = w.forecast10DaysLow()
            moreweather.labelDay1Low.text = lowData[0] + "°C"
            moreweather.labelDay2Low.text = lowData[1] + "°C"
            moreweather.labelDay3Low.text = lowData[2] + "°C"
            moreweather.labelDay4Low.text = lowData[3] + "°C"
            moreweather.labelDay5Low.text = lowData[4] + "°C"
            moreweather.labelDay6Low.text = lowData[5] + "°C"
            moreweather.labelDay7Low.text = lowData[6] + "°C"
            moreweather.labelDay8Low.text = lowData[7] + "°C"
            moreweather.labelDay9Low.text = lowData[8] + "°C"
            moreweather.labelDay10Low.text = lowData[9] + "°C"

            days = w.dayList()
            moreweather.labelDay1Day.text = days[0]
            moreweather.labelDay2Day.text = days[1]
            moreweather.labelDay3Day.text = days[2]
            moreweather.labelDay4Day.text = days[3]
            moreweather.labelDay5Day.text = days[4]
            moreweather.labelDay6Day.text = days[5]
            moreweather.labelDay7Day.text = days[6]
            moreweather.labelDay8Day.text = days[7]
            moreweather.labelDay9Day.text = days[8]
            moreweather.labelDay10Day.text = days[9]
            
            self.manager.current = "moreweather"


class MoreWeatherScreen(Screen):
    def __init__(self, **kwargs):
        super(MoreWeatherScreen, self).__init__(**kwargs)


class TwitterScreen(Screen):
    recentTweet = StringProperty()
    recentUsername = StringProperty()

    def __init__(self, **kwargs):
        super(TwitterScreen, self).__init__(**kwargs)
        self.latestTweet()

    def latestTweet(self):
        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT LastTwitterSearch FROM userInfo")
            username = cursor.fetchone()

        username = username[0]
        t = Twitter()
        self.recentTweet = t.userLatest(username)
        self.recentUsername = "Latest tweet from @" + username

    def getMoreTweets(self):
        un = self.inputTwitterUsername.text
        if un == "":
            pass
        else:
            moretwitter = self.manager.get_screen("moretwitter")
            t = Twitter()
            tweets = t.user10(un)
            moretwitter.labelTwitterUsername.text = "Latest tweets from @" + un
            moretwitter.labelTweet1.text = tweets[0]
            moretwitter.labelTweet2.text = tweets[1]
            moretwitter.labelTweet3.text = tweets[2]
            moretwitter.labelTweet4.text = tweets[3]
            moretwitter.labelTweet5.text = tweets[4]
            moretwitter.labelTweet6.text = tweets[5]
            moretwitter.labelTweet7.text = tweets[6]
            moretwitter.labelTweet8.text = tweets[7]
            moretwitter.labelTweet9.text = tweets[8]
            moretwitter.labelTweet10.text = tweets[9]
            self.parent.current = "moretwitter"


class MoreTwitterScreen(Screen):
    def __init__(self, **kwargs):
        super(MoreTwitterScreen, self).__init__(**kwargs)

    def refreshTwitter(self):
        twitter = self.manager.get_screen("twitter")
        username = twitter.inputTwitterUsername.text

        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            sql = """UPDATE userInfo SET LastTwitterSearch='{}'""".format(username)
            cursor.execute(sql)
            db.commit()

        t = Twitter()
        twitter.recentUsername = "Latest tweet from @" + username
        twitter.recentTweet = t.userLatest(username)
        self.parent.current = "twitter"


class NotesScreen(Screen):
    def __init__(self, **kwargs):
        super(NotesScreen, self).__init__(**kwargs)

    def newNote(self):
        self.parent.current = "newnotes"

    def notesByTime(self):
        morenotes = self.manager.get_screen("morenotes")

        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            sql = """SELECT NoteID, Title, Content FROM Notes ORDER BY Date"""
            cursor.execute(sql)
            data = cursor.fetchall()
            sql = """SELECT Count(NoteID) FROM Notes"""
            cursor.execute(sql)
            count = cursor.fetchall()
            count = count[0][0]
            print(data)

        for i in range(count):
            titlelabel = Label(text="gfgd")
            contentlabel = Label(text="ghhhfh")
            morenotes.layoutMoreNotes.add_widget(titlelabel)

        self.parent.current = "morenotes"

    def notesByTitle(self):
        self.parent.current = "morenotes"


class NewNotesScreen(Screen):
    def __init__(self, **kwargs):
        super(NewNotesScreen, self).__init__(**kwargs)

    def createNote(self):
        title = self.inputNewNoteTitle.text
        content = self.inputNewNoteContent.text

        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            sql = """SELECT Count(NoteID) FROM Notes"""
            cursor.execute(sql)
            count = cursor.fetchall()
            count = count[0][0]

        if title == "" or content == "" or count >= 10:
            pass
        elif count < 10:
            n = Notes()
            n.create(title, content)
            self.parent.current = "notes"


class MoreNotesScreen(Screen):
    pass


class RemindersScreen(Screen):
    pass


class AlarmsScreen(Screen):
    pass


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

    def changeName(self):
        name = self.inputNewName.text
        if name == "":
            pass
        else:
            s = Settings()
            s.changeName(name)

    def changeLocation(self):
        city = self.inputNewCity.text
        country = self.inputNewCountry.text
        if city == "" or country == "":
            pass
        else:
            s = Settings()
            s.changeLocation(country, city)

    def restartSetup(self):
        pass


class MyScreenManager(ScreenManager):
    pass


class AssistantApp(App):
    def b(self):
        self.title = 'Assistant'


if __name__ == "__main__":
    app = AssistantApp()
    Window.size = (360, 640)
    app.run()
