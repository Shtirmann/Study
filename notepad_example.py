import subprocess
import pyautogui
import time
from pywinauto.application import Application

counter = 1

while True:
	note = subprocess.Popen("notepad.exe")
	time.sleep(0.5)
	pyautogui.typewrite("THIS IS A NIGHTMARE, COMRADES!!!")
	time.sleep(0.5)
	pyautogui.hotkey("ctrl", "s")
	time.sleep(0.5)
	pyautogui.typewrite("Elephant Ears"+ str(counter))
	pyautogui.press('enter')
	note.kill()
	counter += 1