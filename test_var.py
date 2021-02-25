import tkinter as tkr
import pygame

player = tkr.Tk()


player.title("Audio player")
player.geometry("205x340")


file = "Song.mp3"


def play():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()

def ExitPlayer():
	pygame.mixer.music.stop()


button1 = tkr.Button(player, width = 5, height = 3, text = "PLAY", command = play)
button1.pack(fill = "x") 

button2 = tkr.Button(player, width = 5, height = 3, text = "STOP", command = ExitPlayer)
button2.pack(fill = "x")

label1 = tkr.LabelFrame(player, text = "Song name")
label1.pack(fill = "both", expand = "yes")
contents1 = tkr.Label(label1, text = file)
contents1.pack()


player.mainloop()