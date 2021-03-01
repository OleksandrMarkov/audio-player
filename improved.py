import tkinter as tkr
import pygame

player = tkr.Tk()
player.title("Audio player")
player.iconbitmap('icon.ico')
player.resizable(width=False, height=False)

pad = "50" # padding
btn_font = "Arial 28 italic bold"

song = "Song.mp3"

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(song)

def play():
	pygame.mixer.music.play()

def pause():
	pygame.mixer.music.pause()

def unpause():
	pygame.mixer.music.unpause()


btn_play = tkr.Button(player, background = "#FCDCDC", text = "PLAY", padx = pad, pady = pad, font = btn_font, command = play)
btn_play.pack(fill = "x") 

btn_pause = tkr.Button(player, background = "#B1FFE3", text = "PAUSE", padx = pad, pady = pad, font = btn_font, command = pause)
btn_pause.pack(fill = "x")

btn_unpause = tkr.Button(player, background = "#FDDAA2", text = "UNPAUSE", padx = pad, pady = pad, font = btn_font, command = unpause)
btn_unpause.pack(fill = "x")

player.mainloop()