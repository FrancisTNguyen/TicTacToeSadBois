from .settings import *
import socket
import re
import pyautogui


def connectToTwitch():
    twitch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    twitch.connect((HOST, PORT))
    twitch.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    twitch.send("NICK {}\r\n".format(NICK).encode("utf-8"))

    connected = True

    while connected:
        chat = twitch.recv(4096).decode("utf-8")

        for line in chat.split("\n"):
            line = line.strip("\r\n")

            if line == "PING :tmi.twitch.tv":
                twitch.send("PONG :tmi.twitch.tv".encode("utf-8"))
            elif line == ":tmi.twitch.tv 376 {} :>".format(NICK):
                print("Connection to twitch successful... joining bot channel...")
                twitch.send("JOIN #{}\r\n".format(CHAN).encode("utf-8"))
            elif line == ":{}.tmi.twitch.tv 366 {} #{} :End of /NAMES list".format(NICK, NICK, NICK):
                print("Joined bot channel... ready to take commands...")
            else:
                if line == "":
                    continue
                else:
                    tokens = line.split(":", 2)
                    user = tokens[1].split("!", 1)[0]

                    try:
                        msg = tokens[2]
                    except:
                        msg = ""

                    if user in OWNER:
                        if msg == "!quit":
                            connected = False
                            pyautogui.keyDown('q')
                            pyautogui.keyUp('q')

                    if msg == "!play":
                        pyautogui.keyDown('p')
                        pyautogui.keyUp('p')
                    elif msg == "1":
                        pyautogui.keyDown('1')
                        pyautogui.keyUp('1')
                    elif msg == "2":
                        pyautogui.keyDown('2')
                        pyautogui.keyUp('2')
                    elif msg == "3":
                        pyautogui.keyDown('3')
                        pyautogui.keyUp('3')
                    elif msg == "4":
                        pyautogui.keyDown('4')
                        pyautogui.keyUp('4')
                    elif msg == "5":
                        pyautogui.keyDown('5')
                        pyautogui.keyUp('5')
                    elif msg == "6":
                        pyautogui.keyDown('6')
                        pyautogui.keyUp('6')
                    elif msg == "7":
                        pyautogui.keyDown('7')
                        pyautogui.keyUp('7')
                    elif msg == "8":
                        pyautogui.keyDown('8')
                        pyautogui.keyUp('8')
                    elif msg == "9":
                        pyautogui.keyDown('9')
                        pyautogui.keyUp('9')
                    pass

    twitch.close()
