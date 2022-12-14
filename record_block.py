from pynput import mouse
from pynput import keyboard
import pyautogui

from tkinter import *
import os
import time

import convert as cvt

class Record:

    def __init__(self, filename, failsafekey, pause_key, img_selection_key, text_extraction_key, returned, pool):
        
        #class variable declaration
        self.filename               = filename
        self.failsafekey            = failsafekey
        self.pause_key              = pause_key
        self.img_selection_key      = img_selection_key
        self.text_extraction_key    = text_extraction_key
        self.blockdata              = returned
        self.keypressed             = set()
        self.during_pause           = []
        self.data                   = []
        self.paused                 = False
        self.img_extraction_step    = 1
        self.img_extraction_name    = 1
        self.text_extraction_step   = 1
        self.text_extraction_name   = 1
        self.tempx                  = 0
        self.tempy                  = 0
        self.t = time.time()
        self.pool = pool
        

        self.start()
        import playsound
        self.pool.submit(playsound.playsound,"sounds/recording start.wav")
        self.run()

        self.data = self.data[2:-1]

        for index, block in enumerate(self.data):
            if block == "record paused":
                self.data.pop(index)
                self.data.pop(index-1)
        for index, block in enumerate(self.data):
            if block[0] == 2 and block[3] == 2 and len(block)==7:
                self.data[index].pop()
            if block[0] == 3 and block[3] == 2 and len(block)==7:
                self.data[index].pop()
            if block == "record de-paused":
                self.data.pop(index)
                for i in range(100000):
                    if self.data[index+i][0] == 1:
                        self.data.pop(index+i)
                        self.data.pop(index+i)
                        self.data.pop(index+i)
                        break
        self.process()
        self.pool.submit(playsound.playsound,"sounds/recording stop.wav") 

    def output(self):
        return self.blockdata

    #start check
    def start(self):

        def on_press(key):

            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.keypressed.add(k)

            if self.keypressed == self.failsafekey:
                self.kl.stop()

        def on_release(key):

            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.keypressed.discard(k)

        self.kl = keyboard.Listener(on_press=on_press,on_release=on_release)
        self.kl.start()
        self.kl.join()

    def run(self):

        try:
            self.oslist = os.listdir(f"screenshot/{self.filename}")
        except:
            self.oslist = []

        for i in range(1,10000):
            if str(i)+".png" not in self.oslist:
                self.count = i
                break 
            
        def on_click(x,y,button,pressed):


            if not self.paused:

                if self.during_pause:
                    self.data = self.data + self.during_pause
                    self.during_pause = []

                for i in range(1,10000):
                    if str(i)+".png" not in self.oslist:
                        self.count = i
                        break 

                pyautogui.screenshot(f'screenshot/{self.filename}/{self.count}.png',region=(x-20,y-20,40,40))
                self.count += 1

                if pressed:

                    if str(button) == "Button.left":
                        try:
                            self.data[-1].append(time.time()-self.t)
                        except:
                            pass
                        self.data.append([0,x,y,"left",1,self.count])
                        self.t = time.time()

                    elif str(button) == "Button.right":
                        try:
                            self.data[-1].append(time.time()-self.t)
                        except:
                            pass
                        self.data.append([0,x,y,"right",1,self.count])
                        self.t = time.time()
            
                if not pressed:

                    if str(button) == "Button.left":
                        try:
                            self.data[-1].append(time.time()-self.t)
                        except:
                            pass
                        self.data.append([0,x,y,"left",0,self.count])
                        self.t = time.time()

                    elif str(button) == "Button.right":
                        try:
                            self.data[-1].append(time.time()-self.t)
                        except:
                            pass
                        self.data.append([0,x,y,"right",0,self.count])
                        self.t = time.time()    

            elif self.paused:

                if not pressed:

                    if str(button) == "Button.left":

                        if self.keypressed == self.img_selection_key and self.img_extraction_step == 1:
                            print("img1")
                            self.img_extraction_step = 2
                            self.during_pause.append([2,x,y,1,self.img_extraction_name,0])

                        elif self.keypressed == self.img_selection_key and self.img_extraction_step == 2:
                            x1 = self.during_pause[-1][1]
                            y1 = self.during_pause[-1][2]

                            for i in range(1,10000):
                                if "img_extraction_"+str(i)+".png" not in self.oslist:
                                    self.img_extraction_name = i
                                    break 

                            print("img 2")  
                            minx = min(x1,x)
                            miny = min(y1,y)
                            maxx = max(x1,x)
                            maxy = max(y1,y)
                            pyautogui.screenshot(f'screenshot/{self.filename}/img_extraction_{self.img_extraction_name}.png',region=(minx,miny,maxx-minx,maxy-miny))
                            self.img_extraction_step = 1
                            self.during_pause.append([2,x,y,2,self.img_extraction_name,0.5])

                        if self.keypressed == self.text_extraction_key and self.text_extraction_step == 1:
                            print("txt1")
                            self.text_extractionpend([3,x,y,1,self.text_extraction_name,0])


                        elif self.keypressed == self.text_extraction_key and self.text_extraction_step == 2:
                            x1 = self.during_pause[-1][1]
                            y1 = self.during_pause[-1][2]

                            for i in range(1,10000):
                                if "text_extraction_"+str(i)+".png" not in self.oslist:
                                    self.text_extraction_name = i
                                    break 

                            print("txt 2")
                            minx = min(x1,x)
                            miny = min(y1,y)
                            maxx = max(x1,x)
                            maxy = max(y1,y)
                            pyautogui.screenshot(f'screenshot/{self.filename}/text_extraction_{self.text_extraction_name }.png',region=(minx,miny,maxx-minx,maxy-miny))
                            self.text_extraction_step = 1
                            self.during_pause.append([3,x,y,2,self.text_extraction_name,0.5])

        def on_scroll(x,y,dx,dy):

            if not self.paused:

                if self.during_pause:
                    self.data = self.data + self.during_pause
                    self.during_pause = []

                for i in range(1,10000):
                    if str(i)+".png" not in self.oslist:
                        self.count = i
                        break 

                pyautogui.screenshot(f'screenshot/{self.filename}/{self.count}.png',region=(x-20,y-20,40,40))
                self.count = self.count+ 1
                try:
                    self.data[-1].append(time.time()-self.t)
                except:
                    pass
                if dy == 1:
                    self.data.append([0,x,y,120,2,self.count])
                else:
                    self.data.append([0,x,y,-120,2,self.count])
                self.t = time.time()
        
        def on_press(key):

            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.keypressed.add(k)

            if self.keypressed == self.failsafekey:
                if self.during_pause:
                    self.data = self.data + self.during_pause
                    self.during_pause = []
                self.paused = True
                self.kl.stop()
                self.ml.stop()

            if self.keypressed == self.pause_key:
                import playsound
                self.paused = not self.paused
                if self.paused:
                    self.pool.submit(playsound.playsound,"sounds/recording pause.wav")
                    self.data.append("record paused")
                else:
                    self.pool.submit(playsound.playsound,"sounds/recording resume.wav")
                    self.data.append("record de-paused")

            if not self.paused:
                if self.during_pause:
                    self.data = self.data + self.during_pause
                    self.during_pause = []

                try:
                    self.data[-1].append(time.time()-self.t)
                except:
                    pass

                self.data.append([1,1,k,self.count])
                self.t = time.time()

        def on_release(key):

            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.keypressed.discard(k)

            if not self.paused:
                if self.during_pause:
                    self.data = self.data + self.during_pause
                    self.during_pause = []
                
                try:
                    self.data[-1].append(time.time()-self.t)
                except:
                    pass

                self.data.append([1,0,k,self.count])
                self.t = time.time()

        self.kl = keyboard.Listener(on_press=on_press,on_release=on_release)
        self.ml = mouse.Listener(on_click=on_click,on_scroll=on_scroll)
        self.kl.start()
        self.ml.start()
        self.kl.join()
        self.ml.join()

    def process(self):
        #Analyze blocks
        for index, command in enumerate(self.data):
            self.blockdata.append(cvt.process(command, self.filename, [0,0]))


def main(filename,failsafekey,pause_key,img_extraction_key,text_extraction_key,returned):
    from concurrent import futures
    pool = futures.ThreadPoolExecutor(max_workers=10)
    a = Record(filename,failsafekey,pause_key,img_extraction_key,text_extraction_key,returned, pool)
    block = a.output()
    for i in range(block.count(None)):
        block.remove(None)
    try:
        block[0][0] = len(block)
    except:
        print(block)
    block[0][2] = "new_block"
    return block


if __name__ == "__main__":
    
    a = []
    main("record_1",["ctrl_l","f10"],["ctrl_l","f9"],["ctrl_l","f1"],["ctrl_l","f2"],a)
    print(a)
