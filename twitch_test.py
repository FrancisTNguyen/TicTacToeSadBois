from twitch.main import *

con = connectToTwitch()

while True:
    getTwitchInput(con)
