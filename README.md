# Automation-manager

## prerequisite

- pip install tk (if you do not have that)
- pip install playsound
- pip install pynput
- pip install customtkinter
- pip install pyautogui
- pip install opencv-python
- pip install pytesseract (optional if you do not use text extraction)

## functions

### Overview

Automation manager is a tool to make and edit python scripts that automate your computer actions include keyboard, mouse and screenshot. 

### Step by step tutorio

- On the menubar, under action -> mainmenu, you are able to find the "start record" button. After clicking on it, get to the screen that you want to record and hit "failsafekey", normally defaulted to "left ctrl" + "f10" (You should hear a "recording start" sound if successful), then all your actions later on will be stored
- Perform your action.
- During the recording, you can always hit the pause key, normally defaulted to "left ctrl" + "f9" (You should hear a "recording pause" sound if successful). DUring the pause phase, everything you did will NOT be recorded until you depause (hit pause key again and you should hear a "recording resume" if successful) In addition, during pause, you can extract a certain part of your screen (essentailly screenshot) by clicking image extraction key twice, normally default to "left ctrl" + "f1" + "left click", the image area will be between the two left click. You can also extract texts from a certain part of your screen (essentailly analyzing the text from your screenshot) by clicking text extraction key twice, normally default to "left ctrl" + "f2" + "left click", the text extraction image area will be between the two left click. 
- You can pause multiple times and do multiple extractions, there's no limit on the length of the recording (well technically there is if you drag it too long it will take a while to process) 
- After you have performed all your actions, hit failsafekey again (normally defaulted to "left ctrl" + "f10") to stop record (you should hear a "recording stop
 if successul) 

