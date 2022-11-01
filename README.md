# Automation manager

## Prerequisite

- pip install tk (if you do not have tkinter) 
- pip install playsound
- pip install pynput
- pip install customtkinter
- pip install pyautogui
- pip install opencv-python
- pip install pytesseract (optional if you do not use text extraction)

## Run the app from GUI.py

## Overview

Automation manager is a tool to make and edit python scripts that automate your computer actions including keyboard, mouse and screenshot. 

## Step by step tutorial

- After opening your app, you can start recording under menubar -> action -> mainmenu -> start record. Hit failsafekey to start recording, hit pause key to pause, hit again to resume, and hit failsafekey again to stop recording.
*__Detailed recording tutorial under docs/recording tutorial__
- After recording your app, you can choose the recorded file under mainmenu, then you can edit your automation.
*__Detailed editing tutorial under docs/editing tutorial__
- After editing, you can choose a converting option and convert it to a python script. After that you can either run it directly or run from automation manager frame
*__Detailed managing tutorial under docs/managing tutorial__

## Specialty
 
#### Functions
There are two power functions provided in the app or the recording — the image extraction and text extraction ability. Without those two functions it's merely a repeat-what-you-do tool, but image extraction and text extraction allows data collections which are probably more needed. 

#### Flexibility
The combination of OpenCV and pyautogui enables some flexibility in the automation: When you record a mouse action, the app will take a screenshot and store it under the according screenshot folder. After converting, when runned, for every mouse action, the program will load in the according pictures and try to find the __exact__ match on the screen:
  - If __no__ matchings were detected, the cursor will go to the stored x,y coordinate
  - If __only__ one match is found on the screen, the x,y coordinate will update to the found location and perform the action
  - If __more than one__ match is found on the screen, the x,y coordinate will remain the stored value
 This allows limited reusability on your automations but it guarantees safety.

#### Convenience 
The automation editor in the app, especially merging blocks and adding for loops, allows easier editing and more conconvenient recording and editing process. 

#### Possibility
The ability of converting edited data into python source code enables further editing. The general framework is provided by the converted code, but experienced programmers can add more details directly to the code to increase its flexibility and functions. For example, one can add many functions between commands like store extracted text to clipboard, get the url for more convenient selenium web scraping, convert extracted image to videos... The combination of source-code generation, image extraction and text extraction opens up many possibilities for a much more powerful automations

## Motivations
The motivation of this project is pretty simple — let the computers do the work.  Since I learned about computers, I've always been amazed of how much the computer can do or what computers can do that we humans cannot, and that's the purpose of having those technology tools: free ourselves and let computers do all the hard work. I think, and hope, that this project achieves that in some way.

## Potential use
- Automate some part of your daily work you are bored of
- Automate games
- Data collection
- AI
- ...

## More to come
- While loop in logic command combobox
- If statement in logic command combobox
- Linking block information to code
- Add pre-made automations
- ...


