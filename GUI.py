"""
Modules need:
pip install playsound
pip install pynput
pip install customtkinter
pip install pyautogui
pip install opencv-python
pip install pytesseract    #optional if you do not use text extraction
"""

from pynput import keyboard
import customtkinter

from concurrent import futures
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import importlib
import os
import time
import json
import sys
import copy

import record_test_2 as rc
import record_block as rcb
import convert as cvt

class Window():

    def __init__(self, root, title, geometry):
        
        with open("status.json", "w") as f:
            json.dump({"status" : 1}, f, indent=4)
    
        self.root   = root 
        self.height = self.root.winfo_screenheight()
        self.width  = self.root.winfo_screenwidth()
        self.root.title(title)
        self.root.geometry(f"{self.width}x{self.height}")

        self.initializing_app()
        self.initializing_menubar()
        self.initializing_frame()
        self.initializing_variable()
        self.initializing_mainmenu()
        self.initializing_option()
        self.initializing_filemanagement()
        self.initializing_automationmanager()
        self.initializing_advanced_option()
        self.root.mainloop() 

#*_____________________________________________________________________________________________________________________________________________________________
#* Initializing method

    def initializing_app(self):
        with open("setting.json","r") as r:
            self.setting = json.load(r)

        self.style                    = self.setting["style"] 
        self.failsafekey              = self.setting["failsafekey"]
        self.isfullscreen             = self.setting["fullscreen"]
        self.toggle_fullscreen        = self.setting["toggle_fullscreen"]
        self.stop_fullscreen          = self.setting["stop_fullscreen"]
        self.p_path                   = self.setting["p_path"]
        self.pause_key                = self.setting["pause_key"]
        self.img_extraction_key       = self.setting["img_extraction_key"]
        self.text_extraction_key      = self.setting["text_extraction_key"]
        self.choose_path              = self.setting["if_choose_path"]
        self.time_gap                 = self.setting["time_gap"]
        self.app_theme                = self.setting["app_theme"]
        self.threading_check_interval = self.setting["threading_check_interval"]

        if self.app_theme == "light":
            self.total_color = "#CFCFD3"
            self.foreground = "black"
            self.button_enter_color = "#7A7A83"
            self.button_leave_color = "#ADADAE"
            self.main_color = "white"
        elif self.app_theme == "dark":
            self.total_color = "black"
            self.foreground = "white"
            self.button_enter_color = "#FFFFFF"
            self.button_leave_color = "#CCCED0"
            self.main_color = "black"
        elif self.app_theme == "sky blue":
            self.total_color = "sky blue"
            self.foreground = "black"
            self.button_enter_color = "#4E88DD"
            self.button_leave_color = "#58AFFC"
            self.main_color = "#C1E1FE"
        elif self.app_theme == "vibrant":
            self.total_color = "purple"
            self.foreground = "white"
            self.button_enter_color = "orange"
            self.button_leave_color = "yellow"
            self.main_color = "black"
        elif self.app_theme == "hacker":
            self.total_color = "black"
            self.foreground = "#20C20E"
            self.button_enter_color = "#14de47"
            self.button_leave_color = "#20C20E"
            self.main_color = "black"

        self.hexacolor = "#7D7E78"
        self.listbox_style = MULTIPLE

        self.root.configure(bg = self.main_color)
        self.root.attributes("-fullscreen",self.isfullscreen)
        self.root.bind(self.toggle_fullscreen, self.fullscreen)
        self.root.bind(self.stop_fullscreen, self.end_fullscreen)

    def initializing_menubar(self):
        menubar = Menu(self.root)
        help = Menu(menubar, tearoff = 0,bg = self.total_color, fg = self.foreground)
        file = Menu(menubar, tearoff = 0,bg = self.total_color, fg = self.foreground)
        system = Menu(menubar, tearoff = 0,bg = self.total_color, fg = self.foreground)
        menubar.add_cascade(label = "Actions", menu = file)
        menubar.add_cascade(label = "help", menu = help)
        menubar.add_cascade(label = "system", menu = system)
        file.   add_command(label = 'MainMenu'              ,command = lambda: self.show_frame(0))
        file.   add_command(label = 'Filemanagement'        ,command = lambda: self.show_frame(6))
        file.   add_command(label = 'Options'               ,command = lambda: self.show_frame(1))
        file.   add_command(label = 'Advanced Options'      ,command = lambda: self.show_frame(2))
        file.   add_command(label = 'Automation Management' ,command = lambda: self.show_frame(7))
        help.   add_command(label = 'General'               ,command = self.show_help_general)
        help.   add_command(label = 'About the app itself'  ,command = self.show_help_app)
        help.   add_separator()
        help.   add_command(label = 'How to record'         ,command = self.show_help_record)
        help.   add_command(label = 'How to edit'           ,command = self.show_help_edit)
        help.   add_command(label = 'How to execute'        ,command = self.show_help_execute)
        system. add_command(label = 'app reboot'            ,command = self.app_reboot)
        system. add_command(label = 'Exit'                  ,command = self.root.destroy)
        self.root.config(menu = menubar)

    def initializing_frame(self):
        self.Menu                 = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800,height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Menu                 .grid(row = 0,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.Option               = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800,height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Option               .grid(row = 0,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.AdvancedOption       = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800,height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.AdvancedOption       .grid(row = 0,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.Logicbg              = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = (self.width-840), height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Logicbg              .grid(row = 0,column = 1,sticky = NSEW,padx = 10,pady = 10)
        self.Logic                = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = (self.width-840), height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Logic                .grid(row = 0,column = 1,sticky = NSEW,padx = 10,pady = 10)
        self.Displaybg            = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800, height = (self.height-477), corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Displaybg            .grid(row = 1,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.Display              = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800, height = (self.height-477), corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Display              .grid(row = 1,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.Blockbg              = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = (self.width-840), height = (self.height-477), corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Blockbg              .grid(row = 1,column = 1,sticky = NSEW,padx = 10,pady = 10)
        self.Block                = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = (self.width-840), height = (self.height-477), corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Block                .grid(row = 1,column = 1,sticky = NSEW,padx = 10,pady = 10)        
        self.Filemanagement       = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800,height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.Filemanagement       .grid(row = 0,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.automationmanagement = customtkinter.CTkFrame(self.root,relief=self.style,fg_color = self.total_color,width = 800,height = 417, corner_radius=0, border_color = self.button_leave_color, border_width = 2)
        self.automationmanagement .grid(row = 0,column = 0,sticky = NSEW,padx = 10,pady = 10)
        self.frames = [self.Menu,self.Option,self.AdvancedOption,self.Logic,self.Display,self.Block,self.Filemanagement,self.automationmanagement]
        self.frames[0].tkraise()

    def initializing_variable(self):
        if self.choose_path:
            messagebox.showinfo("Select tesseract path", "Please choose a tesseract path for text recognition")
            self.p_path = filedialog.askopenfilename()
            os.mkdir("img_extraction")
            os.mkdir("record_folder")
            os.mkdir("screenshot")
            os.mkdir("text_extraction")
            if self.p_path:
                self.setting["p_path"] = self.p_path
            self.setting["if_choose_path"] = False
            with open("setting.json","w") as f:
                json.dump(self.setting,f,indent = 4)

        self.recordlist = os.listdir("record_folder")
        self.record_name = "record_1"
        for i in range(1000):
            if f"{self.record_name}.json" in self.recordlist:
                self.record_name = f"record_{i+2}"
                continue
            break

        self.gridmap = [[[0 for x in range(20)] for x in range(20)] for y in range(8)]
        self.varmap  = [[[0 for x in range(20)] for x in range(20)] for y in range(8)]
        self.blockdata = [[] for i in range(20)]
        self.thread_pool = []
        self.lstxy = [0,0]
        self.activation_hotkey = set()
        self.execution_timer = 0
        self.reusable = False

    def initializing_mainmenu(self):
        self.addlabel   (0,0,0,"Choose an action:")
        self.addrcbutton(0,1,0,"start record",rc.main,rspan = 2)
        self.addlabel   (0,1,1,"choose a name for your new record:")
        self.addentry   (0,2,1,"<KeyPress>","<Return>",None,self.addfile)
        self.addlabel   (0,4,0,f"Your record will be saved as \"{self.record_name}.json\"",cspan = 3)
        self.addbutton  (0,1,3,"convert to py script",command = self.execute,rspan = 2)
        self.addlabel   (0,1,4,"Choose a file from records:")
        self.addcombobox(0,2,4,self.recordlist,self.selectfile)
        self.addlabel   (0,3,4,"Choose a converting option(default to timer):")
        self.addcombobox(0,4,4,["timer","hotkey activation"],self.choose_convert_option)
        self.addbutton  (0,5,0,"reload recorded data",self.reload_recorded_data)

    def initializing_option(self):
        self.addlabel   (1,0,0,"Options:")
        self.addrkbutton(1,1,0,"Record failsafe key 1",0,self.record_failsafekey)
        self.addrkbutton(1,1,1,"Record failsafe key 2",1,self.record_failsafekey)
        self.addlabel   (1,1,2,f"The current failsafe key is {self.failsafekey}")
        self.addrkbutton(1,2,0,"Record pause key 1",0,self.record_pause_key)
        self.addrkbutton(1,2,1,"Record pause key 2",1,self.record_pause_key)
        self.addlabel   (1,2,2,f"The current pause key is {self.pause_key}")
        self.addrkbutton(1,3,0,"Record image extraction key 1",0,self.record_img_extraction_key)
        self.addrkbutton(1,3,1,"Record image extraction key 2",1,self.record_img_extraction_key)
        self.addlabel   (1,3,2,f"The current image extraction key is {self.img_extraction_key}+left click")
        self.addrkbutton(1,4,0,"Record text extraction key 1",0,self.record_text_extraction_key)
        self.addrkbutton(1,4,1,"Record text extraction key 2",1,self.record_text_extraction_key)
        self.addlabel   (1,4,2,f"The current text extraction key is {self.text_extraction_key}+left click")
        self.addbutton  (1,5,0,"If full screen",self.if_fullscreen)
        self.addlabel   (1,5,1,f"Open on full screen: {bool(self.isfullscreen)}")
        self.addcombobox(1,8,0,["light","dark","sky blue","vibrant","hacker"],self.choose_app_theme)
        self.addlabel   (1,8,1,f"The current theme of the app is {self.app_theme}")
        self.addcombobox(1,9,0,["flat", "groove", "raised", "ridge", "solid", "sunken"],self.choose_theme)
        self.addlabel   (1,9,1,f"The current theme of the frame is {self.style}")
        self.addbutton  (1,11,0,"Save setting",self.save_setting)
        self.addbutton  (1,12,0,"Restore default setting",self.restore_setting)

    def initializing_filemanagement(self):
        self.addlabel(6,0,0,"Here you can delete your previously recorded data and their associations")
        self.addscrollbar(6,1,1,rspan = 7)
        self.addlistbox(6,1,0,height=15,rspan = 7)
        for index,file in enumerate(self.recordlist):
            self.gridmap[6][1][0].insert(END,file)
        self.addbutton(6,1,2,"delete selected record and its associations",command = self.delete_file)

    def initializing_automationmanager(self):
        self.addlabel    (7,0,0,"Automation management:")
        self.addlabel    (7,1,0,"Existing pyscripts:")
        self.addscrollbar(7,2,1,rspan = 7)
        self.addlistbox  (7,2,0,height=15,rspan = 7)
        self.addlabel    (7,1,2,"Active automations:")
        self.addscrollbar(7,2,3,rspan = 7)
        self.addlistbox  (7,2,2,height=15,rspan = 7)
        self.addlabel    (7,1,4,"Finished automations:")
        self.addscrollbar(7,2,5,rspan = 7)
        self.addlistbox  (7,2,4,height=15,rspan = 7)
        self.addbutton   (7,1,6,"Execute selected scripts", self.execute_selected_scripts)
        self.addbutton   (7,2,6,"Clear finished automation", self.clear_pool)
        self.addbutton   (7,3,6,"terminate selected thread", self.terminate_thread)
        self.load_script()
        thread_pool_executor.submit(self.check_thread_status)

    def initializing_advanced_option(self):
        self.addlabel (2,0,0,"Advanced Option")
        self.addbutton(2,1,0,"Re-choose tesseract path", self.re_choose_tesseract_path)
        self.addlabel (2,1,1,f"The current tesseract path is {self.p_path}")
        self.addlabel (2,2,0,"Choose a record time gap")
        self.addentry (2,2,1,"None",None,None,None,default=self.time_gap)
        self.addlabel (2,3,0,f"the current threading check interval is {self.threading_check_interval} seconds")
        self.addentry (2,3,1,None,None,None,None,default=self.threading_check_interval)
        self.addbutton(2,10,0,"Save setting",self.save_advanced_setting)
        self.addbutton(2,11,0,"Restore default setting",self.restore_setting)

#*______________________________________________________________________________________________________________________________________________________________
#* Threading method

    def terminate_thread(self):
        """terminate selected running thread"""
        for file in self.gridmap[7][2][2].curselection():
            with open("manager.json","r") as f:
                data = json.load(f)
            data[self.gridmap[7][2][2].get(file)] = 0
            with open("manager.json","w") as f:
                json.dump(data, f, indent=4)            

    def execute_selected_scripts(self):
        """execute selected script as threads"""
        for index, script in enumerate(self.gridmap[7][2][0].curselection()):
            with open("manager.json","r") as f:
                data = json.load(f)
            data[self.gridmap[7][2][0].get(script)[:-3]] = 1
            with open("manager.json","w") as f:
                json.dump(data, f, indent=4)
            self.thread_pool.append([importlib.import_module(f"pyscript.{self.gridmap[7][2][0].get(script)[:-3]}").execute(),self.gridmap[7][2][0].get(script)[:-3]])     

    def check_thread_status(self):
        """every given second check the status of every running thread in the thread pool"""
        with open("status.json", "r") as f:
            a = json.load(f)["status"]
        while a:
            time.sleep(self.threading_check_interval)
            with open("status.json", "r") as f:
                a = json.load(f)["status"]
            for thread in self.thread_pool:
                if thread[0].running():
                    if thread[1] not in self.gridmap[7][2][2].get(0,END):
                        self.gridmap[7][2][2].insert(END,thread[1])
                elif thread[0].done():
                    if thread[1] in self.gridmap[7][2][2].get(0,END):
                        for index, string in enumerate(self.gridmap[7][2][2].get(0,END)):
                            if string == thread[1]:
                                self.gridmap[7][2][2].delete(index, index+1)
                    if thread[1] not in self.gridmap[7][2][4].get(0,END):
                        self.gridmap[7][2][4].insert(END,thread[1])
            
    def clear_pool(self):
        """clear every finished thread from thread pool"""
        for thread in self.thread_pool:
            if thread[0].done():
                self.thread_pool.remove(thread)
        self.addlistbox(7,2,4,height=15,rspan = 7)

    def load_script(self):
        """load every existed scripts from pyscript folder into the first listbox"""
        for script in os.listdir("pyscript"):
            if script!="__init__.py" and script[-3:] == ".py":
                self.gridmap[7][2][0].insert(END,script)

#*_____________________________________________________________________________________________________________________________________________________________
#* tkinter & custom tkinter method

    def show_frame(self,frame):
        """raise the selected frame from self.frames"""
        self.frames[frame].tkraise()

    def refresh(original_function):
        """wrapper function for every "add" functions, clear the existing widget"""
        def wrapper_function(*args,**kwargs):
            self,frame,row,column = args[0:4]
            if  self.gridmap[frame][row][column]:
                self.gridmap[frame][row][column].grid_remove()
            self.gridmap[frame][row][column] = None
            original_function(*args,**kwargs)
        return wrapper_function  

    def refresh_widget(self,frame,row,column):
        """refresh selected tkinter widget"""
        if self.gridmap[frame][row][column]:
            self.gridmap[frame][row][column].grid_remove()
        self.gridmap[frame][row][column] = None  

    @refresh
    def addtext(self,frame,row,column, width = 0, height = 0, rspan = 1, cspan = 1):
        """add a tkinter Text widget"""
        self.gridmap[frame][row][column] = Text(self.frames[frame])
        self.gridmap[frame][row][column].grid(row = row, column = column, padx = 2, pady = 2, sticky = NSEW, rowspan = rspan, columnspan = cspan)
        if width:
            self.gridmap[frame][row][column].config(width = width)
        if height:
            self.gridmap[frame][row][column].config(height = height)
        self.gridmap[frame][row][column].config(fg=self.foreground, insertbackground=self.foreground,wrap="none", bg=self.total_color)

    @refresh
    def addrkbutton(self,frame,row,column,text,index,command,cspan = 1,rspan = 1):
        """add a record button for hotkey record, command run as a thread"""
        self.gridmap[frame][row][column] = customtkinter.CTkButton(self.frames[frame],text = text, hover_color = self.button_enter_color, fg_color = self.button_leave_color, corner_radius=0,command = lambda:thread_pool_executor.submit(command, index))
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2,pady = 2, sticky = NSEW, columnspan = cspan, rowspan = rspan)     

    @refresh
    def addlabel(self,frame,row,column,text,cspan = 1,rspan = 1, img = None):
        """add a customtkinter label"""
        self.gridmap[frame][row][column] = customtkinter.CTkLabel(self.frames[frame],text = text, image = img, compound = LEFT, text_color=self.foreground)
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2,pady = 2, sticky = NSEW, columnspan = cspan, rowspan = rspan)
        
    @refresh
    def addbutton(self,frame,row,column,text,command,cspan = 1,rspan = 1):
        """add a customtkinter button"""
        self.gridmap[frame][row][column] = customtkinter.CTkButton(self.frames[frame],text = text,command = command, hover_color = self.button_enter_color, fg_color = self.button_leave_color, corner_radius=0)
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2,pady = 2, sticky = NSEW, columnspan = cspan, rowspan = rspan)        

    @refresh
    def addrcbutton(self,frame,row,column,text,command,cspan = 1,rspan = 1):
        """add a record button for command record, command run as a thread"""
        self.gridmap[frame][row][column] = customtkinter.CTkButton(self.frames[frame],text = text, hover_color = self.button_enter_color, fg_color = self.button_leave_color, corner_radius=0,command = lambda:thread_pool_executor.submit(command,self.record_name,set(self.failsafekey),set(self.pause_key),set(self.img_extraction_key),set(self.text_extraction_key),self.record_name))
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2,pady = 2, sticky = NSEW, columnspan = cspan, rowspan = rspan)                

    @refresh
    def addonepbutton(self,frame,row,column,text,command,p1,cspan = 1,rspan = 1):
        """add a customtkinter button with one parameter"""
        self.gridmap[frame][row][column] = customtkinter.CTkButton(self.frames[frame],text = text, hover_color = self.button_enter_color, fg_color = self.button_leave_color, corner_radius=0,command = lambda:command(p1))
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2,pady = 2, sticky = NSEW, columnspan = cspan, rowspan = rspan)         

    @refresh
    def addtwopbutton(self,frame,row,column,text,command,p1,p2,cspan = 1,rspan = 1):
        """add a customtkinter button with two parameter"""
        self.gridmap[frame][row][column] = customtkinter.CTkButton(self.frames[frame],text = text, hover_color = self.button_enter_color, fg_color = self.button_leave_color, corner_radius=0,command = lambda:command(p1,p2))
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2,pady = 2, sticky = NSEW, columnspan = cspan, rowspan = rspan)         

    @refresh
    def addentry(self,frame,row,column,key1,key2,command1,command2,cspan = 1,rspan = 1, default = ""):
        """add a customtkinter entry"""
        self.gridmap[frame][row][column] = customtkinter.CTkEntry(self.frames[frame], text_color=self.foreground, bg_color=self.total_color, fg_color=self.main_color)
        self.gridmap[frame][row][column].insert(END, default)
        if command1:
            self.gridmap[frame][row][column].bind(key1,command1)
        if command2:
            self.gridmap[frame][row][column].bind(key2,command2)
        self.gridmap[frame][row][column].grid(row = row, column = column, padx = 2,pady = 2, sticky=NSEW, columnspan = cspan, rowspan = rspan)    

    @refresh
    def addcombobox(self,frame,row,column,options,command): 
        """add a customtkinter combobox, also generates a customtkinter.StringVar() object"""
        self.varmap[frame][row][column] = customtkinter.StringVar()
        self.gridmap[frame][row][column] = customtkinter.CTkComboBox(self.frames[frame],values = options, variable=self.varmap[frame][row][column], command = command,corner_radius=0, text_color=self.foreground,fg_color = self.total_color, border_color = self.button_leave_color, dropdown_color=self.total_color,dropdown_text_color=self.foreground, button_hover_color=self.button_enter_color, button_color = self.button_leave_color)
        self.gridmap[frame][row][column].grid(row = row, column = column, padx = 2,pady = 2, sticky=NSEW)  

    @refresh
    def addlistbox(self,frame,row,column, height = 10, rspan = 1, cspan = 1):
        """add a tkinter listbox"""
        self.gridmap[frame][row][column] = Listbox(self.frames[frame],height=height,yscrollcommand = self.gridmap[frame][row][column+1].set, selectmode=self.listbox_style)
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2, pady = 2, sticky=NSEW, rowspan = rspan, columnspan = cspan)
        self.gridmap[frame][row][column].config(highlightbackground="#0b5162", highlightcolor="#0b5162", fg=self.foreground,bg=self.total_color, highlightthickness=2, relief="solid")

    @refresh
    def addscrollbar(self,frame,row,column, rspan = 1, cspan = 1):
        """add a tkinter scrollbar"""
        self.gridmap[frame][row][column] = Scrollbar(self.frames[frame])
        self.gridmap[frame][row][column].grid(row = row,column = column, padx = 2, pady = 2, sticky=NSEW, rowspan = rspan, columnspan = cspan)

#*_____________________________________________________________________________________________________________________________________________________________
#* display helper message functions:

    def show_help_record(self):
        try:
            self.canvas
        except:
            self.canvas = Canvas(self.root,width = 800,height = 600)
            self.canvas.grid(row = 0,column = 0,rowspan = 2,columnspan = 2)
            self.root.bind("<Escape>",self.quit_canvas)
        self.canvas.delete("all")
        self.canvas.create_text(400,300,text= f"""
How to record:
1. Click the record button to start initializing the record, once you are ready, click start record hotkey(default to left ctrl + f10)
2. Once it starts, do whatever you want to record, while doing so, if you want to pause the record, you can click the pause hotkey
(default to left ctrl + f9)
3. A powerful feature of this app is it's image extraction and text extraction ability, which enables during the pause,
you can hit image extraction hotkey(default to left ctrl + f1 + mouse left click), hit the hotkey twice to get the image you want to
extract from the screen. The image will be the space in between your two clicks. Same thing to text extraction, hit the text extraction 
hotkey(default to left ctrl + f2 + left mouse click), hit the hotkey twice to get the image you want to extract your text from. 
The image will be the space in between your two clicks, and the text will be extracted once the automation is performed. 
        """)  
    
    def show_help_edit(self):
        try:
            self.canvas
        except:
            self.canvas = Canvas(self.root,width = 800,height = 600)
            self.canvas.grid(row = 0,column = 0,rowspan = 2,columnspan = 2)
            self.root.bind("<Escape>",self.quit_canvas)
        self.canvas.delete("all")
        self.canvas.create_text(400,300,text= f"""
Functions of the editor:
1. After the record, you are able to view your previous records detailedly by selecting the combobox next to it
2. After the selection, you will see that on the main automation column all your actions will be displayed. However,
it includes press and release key, which might be confusuing, to make it clear, click the "automerge block" on the 
right side, then the system will detect all your click and keyinput command and merge them
3. For every block of the command, you can select on it and click enter you are able to see the detail of the block,
including the block data and the original generated python source code. You will be able to edit everything about
the block and after you finish click "save" to save it. You can also click "restore defualt" to restore original
data or code. (changing merged blocks are currently nor supported)
4. For some more complex editing, you can click on the "change combobox style" to change the selection style, which makes 
manipulating more convenient. You can then select multiple blocks and click "add workspace" down below to add a new work
space consist of all the previously selected blocks. You can edit the blocks and then you can choose to either
"Merge to main"(replace main automation wuth current workspace) or "Concatenate to main" (add the blocks onto the end of the
main automation)
5. Another thing you can do is that you can select "Merge blocks" to merge all the blocks you selected into one, merged block's
information can be displayed by "up a command" and "down a command" buttons on the button of the display screen. Besides that,
you can simply record a new block and the new block will show up the on end of the main automation.
6. You can always delete the currently selected block if you do not want them
7. After editing, if you click the convert button on the main screen, the current main automation will be saved into a .py file
in the "pyscript" folder. There's several options to convert: timed and reusable hotkey and non reusable hotkey.
Don't forget to record your hotkey if you pick hotkey activation, reusable means that you can essentially make it as
a custom hotkey that performs a sequence of action, but for safety, please execute reusable script in automation manager frame
You can then convert it from either your computer or from automation manager frame. You can also edit it directly from the 
source python file.
        """)  

    def show_help_execute(self):
        try:
            self.canvas
        except:
            self.canvas = Canvas(self.root,width = 800,height = 600)
            self.canvas.grid(row = 0,column = 0,rowspan = 2,columnspan = 2)
            self.root.bind("<Escape>",self.quit_canvas)
        self.canvas.delete("all")
        self.canvas.create_text(400,300,text= f"""
How to execute:
1. After you finish editing and converted it to python source code, you can directly open it from pyscript and execute
and edit it directly
2. Another thing you can do is to go into automation manager under Action, on the very left there's all your records and if you
click the execute selected scripts, it will be runned as a thread in which is shown in the middle column, once it's finished, it
will then show up on the right column. You can clear the finished thread by clicking "clear finished automation", you can also
terminate a active thread by clicking terminate selected thread
3. During the execution, if something unexpected happens, you can always move your cursor to the corner of the screen and the script
will be stopped.
        """)    

    def show_help_general(self):
        try:
            self.canvas
        except:
            self.canvas = Canvas(self.root,width = 800,height = 600)
            self.canvas.grid(row = 0,column = 0,rowspan = 2,columnspan = 2)
            self.root.bind("<Escape>",self.quit_canvas)
        self.canvas.delete("all")
        self.canvas.create_text(400,300,text= f"""
Functions:
1. This app is able to record all your mouse inputs and your keyboard inputs
2. During pause, you can add in image extraction and text extraction step
3. The App also serves as an editor for your recordings in which you can manage and modify it
4. After modify, you can convert the data in which the data is going to be stored in a .py file in pyscript and ready to execute
5. You can execute and manage your scripts through the automation manager
5. The execution algorithm has a image recognition system which allows certain flexibility

A simple walk through:
1.Hit record button
2.When you are ready, hit start record hotkey (default to left ctrl + f10)
3.Perform your action
4.If you want to pause the app, hit pause record hotkey (default to left )
5.click reload recorded data, choose the file, do some editing if you need to
6.choose a convertion option and click "convert to py script"
7.Run it directly by opening source code or run it through automation manager
        """)

    def show_help_app(self):
        try:
            self.canvas
        except:
            self.canvas = Canvas(self.root,width = 800,height = 600)
            self.canvas.grid(row = 0,column = 0,rowspan = 2,columnspan = 2)
            self.root.bind("<Escape>",self.quit_canvas)
        self.canvas.delete("all")
        self.canvas.create_text(400,300,text= f"""
App setting:
1. In the option screen, you are able to change the app's theme (light, dark and skyblue)
*dark mode is my favorate btw"
2. You can choose to toggle full screen or not when next time the app is started
3. In case something unexpected happen, try app reboot under "system" on the menubar
        """)

#*_____________________________________________________________________________________________________________________________________________________________
#* change option function / app function

    def save_setting(self):
        """save the current setting to setting.json"""
        data ={
    "failsafekey": self.failsafekey,
    "style": self.style,
    "fullscreen" : self.isfullscreen,
    "toggle_fullscreen" : self.toggle_fullscreen,
    "stop_fullscreen" : self.stop_fullscreen,
    "p_path": self.p_path,
    "pause_key": self.pause_key,
    "img_extraction_key": self.img_extraction_key,
    "text_extraction_key": self.text_extraction_key,
    "if_choose_path": self.choose_path,
    "time_gap": self.time_gap,
    "app_theme": self.app_theme,
    "threading_check_interval": self.threading_check_interval
}
        with open(f"setting.json","w") as f:
            json.dump(data,f,indent = 4)        
        messagebox.showinfo(title=None, message="Restart or reboot for changed settings to work")

    def restore_setting(self):
        """restore the default setting to current option"""
        data ={
    "failsafekey": ["ctrl_l","f10"],
    "style": "solid",
    "fullscreen": 0,
    "toggle_fullscreen": "<Control_L>q",
    "stop_fullscreen": "<Escape>",
    "p_path": "D:/Code/tesseract.exe",
    "pause_key": ["ctrl_l","f9"],
    "img_extraction_key": ["ctrl_l","f1"],
    "text_extraction_key": ["ctrl_l","f2"],
    "if_choose_path": True,
    "time_gap": 0,
    "app_theme": "light",
    "threading_check_interval": 1
}
        with open(f"setting.json","w") as f:
            json.dump(data,f,indent = 4)  
        messagebox.showinfo(title=None, message="Restart or reboot for changed settings to work")

    def choose_theme(self,event):
        """choose theme for tkinter frame (useless it seems for now)"""
        self.style = self.gridmap[1][9][0].get()
        self.addlabel(1,9,1,f"The current theme of the frame is {self.style}")

    def re_choose_tesseract_path(self):
        """re-choose the tesseract path (used in advanced option)"""
        self.p_path = filedialog.askopenfilename()
        if self.p_path:
            self.setting["p_path"] = self.p_path
        with open("setting.json","w") as f:
            json.dump(self.setting,f,indent = 4)
        self.addlabel (2,1,1,f"The current tesseract path is {self.p_path}")

    def quit_canvas(self,event):
        """destory the canvas (for "show help" functions)"""
        self.canvas.grid_remove()
        del self.canvas
        self.root.unbind("Escape")
        self.root.bind(self.toggle_fullscreen, self.fullscreen)
        self.root.bind(self.stop_fullscreen, self.end_fullscreen)

    def choose_app_theme(self,event):
        """choose the theme for the app (light, dark, sky blue, vibrant, hacker)"""
        self.app_theme = self.gridmap[1][8][0].get()
        self.addlabel   (1,8,1,f"The current theme of the app is {self.app_theme}")

    def end_fullscreen(self,event):
        """end fullscreen"""
        self.root.attributes("-fullscreen", False)

    def fullscreen(self,event):
        """toggle fullscreen"""
        self.root.attributes("-fullscreen", True)

    def if_fullscreen(self):
        """self.isfullscreen = not self.isfullscreen"""
        self.isfullscreen = not self.isfullscreen
        self.addlabel(1,5,1,f"Open on full screen: {self.isfullscreen}")

    def app_reboot(self):
        """reboot the app"""
        with open("status.json", "w") as f:
            json.dump({"status" : 0}, f, indent=4)
        time.sleep(1)
        with open("status.json", "w") as f:
            json.dump({"status" : 1}, f, indent=4)
        self.initializing_app()
        self.initializing_menubar()
        self.initializing_frame()
        self.initializing_variable()
        self.initializing_mainmenu()
        self.initializing_option()
        self.initializing_filemanagement()
        self.initializing_automationmanager()
        self.initializing_advanced_option()    

#*_____________________________________________________________________________________________________________________________________________________________
#* key-record function

    def record_activation_hotkey(self,index):
        def on_press(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.activation_hotkey.add(k)
            self.addlabel(0,6,4,f"Current activaton hotkey is {self.activation_hotkey}")
            return False
        with keyboard.Listener(on_press=on_press,) as listener:
            listener.join()

    def record_failsafekey(self,index):
        def on_press(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.failsafekey[index] = k
            self.addlabel(1,1,2,f"The current failsafe is {self.failsafekey}")
            return False
        with keyboard.Listener(on_press=on_press,) as listener:
            listener.join()

    def record_pause_key(self,index):
        def on_press(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.pause_key[index] = k
            self.addlabel(1,2,2,f"The current pause key is {self.pause_key}")
            return False
        with keyboard.Listener(on_press=on_press,) as listener:
            listener.join()

    def record_img_extraction_key(self,index):
        def on_press(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.img_extraction_key[index] = k
            self.addlabel(1,3,2,f"The current image extraction key is {self.img_extraction_key}")
            return False
        with keyboard.Listener(on_press=on_press,) as listener:
            listener.join()

    def record_text_extraction_key(self,index):
        def on_press(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\",'\\')
            self.text_extraction_key[index] = k
            self.addlabel(1,4,2,f"The current text extraction key is {self.text_extraction_key}")
            return False
        with keyboard.Listener(on_press=on_press,) as listener:
            listener.join()

#*_____________________________________________________________________________________________________________________________________________________________
#* core-logic function

    def delete_file(self):
        """delete select file and its associations (filemanagement)"""
        for index, file in enumerate(self.gridmap[6][1][0].curselection()):
            try:
                os.remove(f"record_folder\{self.gridmap[6][1][0].get(file)}")
            except:
                pass
            try:
                os.remove(f"pyscript\{self.gridmap[6][1][0].get(file)[:-5]}.py")
            except:
                pass
            try:
                for f in os.listdir(f"screenshot\{self.gridmap[6][1][0].get(file)[:-5]}"):
                    os.remove(f"screenshot\{self.gridmap[6][1][0].get(file)[:-5]}\{f}")
                os.rmdir(f"screenshot\{self.gridmap[6][1][0].get(file)[:-5]}")
            except:
                pass
        self.reload_recorded_data()

    def reload_recorded_data(self):
        """reload record data (mainmenu)"""
        self.recordlist = os.listdir("record_folder")
        self.addcombobox(0,2,4,self.recordlist,self.selectfile)
        self.addscrollbar(6,1,1,rspan = 7)
        self.addlistbox(6,1,0,height=15,rspan = 7)
        for index,file in enumerate(self.recordlist):
            self.gridmap[6][1][0].insert(END,file)
        
    def choose_convert_option(self,event):
        """choose convert option (mainmenu)"""
        if self.gridmap[0][4][4].get() == "timer":
            self.execution_timer = 3
            self.addentry(0,5,4,"<Return>",None,self.display_execution_timer,None,default=self.execution_timer)
            self.addlabel(0,6,4,f"Current execution timer is {self.execution_timer}")
            try:
                self.gridmap[0][7][4].grid_remove()
            except:
                pass
            self.gridmap[0][7][4] = 0
        elif self.gridmap[0][4][4].get() == "hotkey activation":
            self.activation_hotkey = set()
            self.addrkbutton(0,5,4,"Record a new activation hotkey(stackable)",0,command = self.record_activation_hotkey)
            self.addlabel(0,6,4,f"Current activaton hotkey is {self.activation_hotkey}")
            self.addbutton(0,7,4,"clear activation hotkey",command = self.clear_activation_hotkey)
            self.addbutton(0,8,4,"If reusable", command = self.if_reusable)
            if self.reusable:
                self.addlabel(0,9,4,"Reusable")
            else:
                self.addlabel(0,9,4,"Not reusable")

    def if_reusable(self):
        """toggle on/off reusability of the converted python script (mainmenu)"""
        self.reusable = not self.reusable
        if self.reusable:
            self.addlabel(0,9,4,"Reusable")
        else:
            self.addlabel(0,9,4,"Not reusable")
            
    def clear_activation_hotkey(self):
        """clear activation hotkey (mainmenu)"""
        self.activation_hotkey = set()
        self.addrkbutton(0,5,4,"Record a new activation hotkey(stackable)",0,command = self.record_activation_hotkey)
        self.addlabel(0,6,4,f"Current activaton hotkey is {self.activation_hotkey}")
        self.addbutton(0,7,4,"clear activation hotkey",command = self.clear_activation_hotkey)

    def display_execution_timer(self,event):
        """display execution_timer (mainmenu)"""
        self.execution_timer = int(self.gridmap[0][5][4].get())
        self.addlabel(0,6,4,f"Current execution timer is {self.execution_timer}")

    def save_advanced_setting(self):
        """save advanced settinh, call save_setting function (advanced option)"""
        self.time_gap = int(self.gridmap[2][2][1].get())
        self.threading_check_interval = int(self.gridmap[2][3][1].get())
        self.save_setting()
    
    def addfile(self,event):
        """get/generate and display default/user-entered new record name"""
        self.record_name = self.gridmap[0][2][1].get()
        if not self.record_name:
            self.record_name = "record_1"
            for i in range(1000):
                if f"{self.record_name}.json" in self.recordlist:
                    self.record_name = f"record_{i+2}"
                    continue
                break
        self.addlabel(0,4,0,f"Your record will be saved as \"{self.record_name}.json\"",cspan = 3)

    def save_block_data(self,lst, dimension = 0):
        """save block data from display information frame (display information)"""
        if dimension:
            if dimension == 1:
                lst[dimension-1][2]    = self.gridmap[4][2][1].get()
            lst[dimension-1][3][1] = self.gridmap[4][3][1].get()
            lst[dimension-1][3][3] = self.gridmap[4][5][1].get()
            lst[dimension-1][3][2] = self.gridmap[4][4][1].get()
            if lst[dimension-1][3][0] == 0:
                lst[dimension-1][3][4] = self.gridmap[4][6][1].get()
                lst[dimension-1][3][5] = self.gridmap[4][7][1].get()
                lst[dimension-1][3][6] = self.gridmap[4][8][1].get()
            elif lst[dimension-1][3][0] == 1:      
                lst[dimension-1][3][4] = self.gridmap[4][6][1].get()
            else: 
                lst[dimension-1][3][0] = self.gridmap[4][6][1].get()
                lst[dimension-1][3][4] = self.gridmap[4][7][1].get()
                lst[dimension-1][3][-1] = self.gridmap[4][8][1].get()
        else:
            lst[3][1] = self.gridmap[4][3][1].get()
            lst[3][2] = self.gridmap[4][4][1].get()
            lst[3][3] = self.gridmap[4][5][1].get()
            lst[2]    = self.gridmap[4][2][1].get()
            if lst[3][0] == 0:
                lst[3][4] = self.gridmap[4][6][1].get()
                lst[3][5] = self.gridmap[4][7][1].get()
                lst[3][6] = self.gridmap[4][8][1].get()
            elif lst[3][0] == 1:   
                lst[3][4] = self.gridmap[4][6][1].get() 
            else:
                lst[3][0] = self.gridmap[4][6][1].get()
                lst[3][4] = self.gridmap[4][7][1].get()
                lst[3][-1] = self.gridmap[4][8][1].get()
        self.refresh_listbox()

    def refresh_listbox(self):
        """refresh every listbox in workspace frame (workspace)"""
        for index, row in enumerate(self.blockdata):
            try:
                self.gridmap[5][1][index*2].delete(0,END)
            except:
                pass 
            for id,block in enumerate(row):
                try:
                    if type(block[0]) == list:
                        self.gridmap[5][1][index*2].insert(END, block[0][2]+f"__{str(id+1)}____"[:6])
                    elif type(block[2]) == str:
                        self.gridmap[5][1][index*2].insert(END, block[2]+f"__{str(id+1)}____"[:6])
                except:
                    pass

    def change_listbox_style(self):
        """change all the listboxs' style in workspace frame(workspace)"""
        if self.listbox_style == MULTIPLE:
            self.listbox_style = SINGLE
        elif self.listbox_style == SINGLE:
            self.listbox_style = EXTENDED
        elif self.listbox_style == EXTENDED:
            self.listbox_style = MULTIPLE
        for listbox in range(0,10,2):
            try:
                self.gridmap[5][1][listbox].config(selectmode = self.listbox_style)
            except:
                pass
        self.addlabel(5,2,10,f"Current listbox style is: {self.listbox_style}")

    def selectfile(self,event):
        """read, convert and display selected file in workspace (mainmenu)"""
        block_row = 0
        self.blockdata[block_row] = []
        self.filename = self.varmap[0][2][4].get()[:-5]
        with open(f"record_folder/{self.filename}.json","r") as r:
            self.command = json.load(r)
        for command in self.command:
            if cvt.process(command,self.filename,self.lstxy):
                self.blockdata[block_row].append(cvt.process(command,self.filename,self.lstxy))
        self.addlabel(5,0,0,"Main automation:")
        self.addscrollbar(5,1,1,rspan = 7)
        self.addlistbox(5,1,0,height=15,rspan = 7)
        for index,block in enumerate(self.blockdata[block_row]):
            self.gridmap[5][1][0].insert(END, block[2]+f"__{str(index+1)}____"[:6])
        self.gridmap[5][1][1].config(command = self.gridmap[5][1][0].yview)
        self.gridmap[5][1][0].bind("<Return>",lambda event, row = 1, column = 2:self.find_block(row,column))
        self.gridmap[5][1][0].bind("<w>",lambda event, column = 0:self.move_up_selected_blocks(column))
        self.gridmap[5][1][0].bind("<s>",lambda event, column = 0:self.move_down_selected_blocks(column))
        self.addonepbutton(5,9,0,"Add another workspace",self.addworkspace,2)
        self.addonepbutton(5,10,0,"Delete main automation",self.delete_workspace,2)
        self.addlabel     (0,3,0,f"You choose to modify or execute the record: \n\"{self.filename}\"",cspan = 3)
        self.addlabel     (5,0,9,"Block action")
        self.addbutton    (5,1,9,"Record a new block",self.record_new_block)
        self.addbutton    (5,2,9,"Delete selected block", self.delete_selected_block)
        self.addbutton    (5,3,9,"Merge selected blocks", self.merge_selected_block)
        self.addbutton    (5,4,9,"Auto merge blocks", self.auto_merge_block)
        self.addlabel     (5,0,10,"Listbox action")
        self.addbutton    (5,1,10,"Change listbox style",self.change_listbox_style)
        self.addlabel     (5,2,10,f"Current listbox style is: {self.listbox_style}")

    def addworkspace(self,column):
        """add another workspace, loading all selected block, max to 4 (workspace)"""
        if column <=6:
            self.addlabel(5,0,column,f"Workspace {column//2}:")
            self.addscrollbar(5,1,column+1,rspan = 7)
            self.addlistbox(5,1,column,height=15,rspan = 7)
            self.blockdata[column//2] = [[] for i in range(len(self.gridmap[5][1][column-2].curselection()))]
            for index, block in enumerate(self.gridmap[5][1][column-2].curselection()):
                self.gridmap[5][1][column].insert(END, self.gridmap[5][1][column-2].get(block)[:-6]+f"__{str(index+1)}____"[:6])
                if type(self.blockdata[column//2-1][block][0]) == list:
                    self.blockdata[column//2][index] = []
                    for command in self.blockdata[column//2-1][block]:
                        try:
                            self.blockdata[column//2][index].append(copy.deepcopy(command[:1])+[command[1].copy()]+copy.deepcopy(command[2:]))
                        except:
                            self.blockdata[column//2][index].append(copy.deepcopy(command))
                else:       
                    try:
                        self.blockdata[column//2][index] = copy.deepcopy(self.blockdata[column//2-1][block][:1])+[self.blockdata[column//2-1][block][1].copy()]+copy.deepcopy(self.blockdata[column//2-1][block][2:])
                    except:
                        self.blockdata[column//2][index] = copy.deepcopy(self.blockdata[column//2-1][block])
            self.gridmap[5][1][column+1].config(command = self.gridmap[5][1][column].yview)        
            self.gridmap[5][1][column].bind("<Return>",lambda event, row = column//2+1, column = column+2:self.find_block(row,column))
            self.gridmap[5][1][column].bind(   "<w>"  ,lambda event, column = column:self.move_up_selected_blocks(column))
            self.gridmap[5][1][column].bind(   "<s>"  ,lambda event, column = column:self.move_down_selected_blocks(column))
            self.addonepbutton(5,9,column,"Add another workspace",self.addworkspace,column+2)        
            self.addonepbutton(5,10,column,"Delete this workspace",self.delete_workspace,column+2)
            self.addonepbutton(5,11,column,"Merge to main",self.merge_to_main,column)
            self.addonepbutton(5,12,column,"Concatenate to main",self.concatenate_to_main,column) 
    
        else:
            messagebox.showinfo(title=None, message="Too many workspaces!")

    def delete_workspace(self,column):
        """delete selected workspace (workspace)"""
        for i,row in enumerate(self.gridmap[5]):
            try:
                row[column-2].grid_remove()
            except:
                pass
            try:
                row[column-1].grid_remove()
            except:
                pass
            self.gridmap[5][i][column-2] = 0
            self.gridmap[5][i][column-1] = 0

    def move_up_selected_blocks(self,column):
        """move up all selected blocks (workspace)"""
        for index, block in enumerate(self.gridmap[5][1][column].curselection()):
            if block >= 1:
                self.gridmap[5][1][column].insert(block-1,self.gridmap[5][1][column].get(block))
                self.gridmap[5][1][column].delete(block+1,block+1)
                self.gridmap[5][1][column].selection_set(block-1)
                temp = self.blockdata[column//2][block]
                self.blockdata[column//2][block] = self.blockdata[column//2][block-1]
                self.blockdata[column//2][block-1] = temp
            else:
                break

    def move_down_selected_blocks(self,column):
        """move down all selected blocks (workspace)"""
        for index, block in enumerate(self.gridmap[5][1][column].curselection()):
            if block < self.gridmap[5][1][column].index("end")-1:
                self.gridmap[5][1][column].insert(block+2,self.gridmap[5][1][column].get(block))
                self.gridmap[5][1][column].delete(block,block)
                self.gridmap[5][1][column].selection_set(block+1)
                temp = self.blockdata[column//2][block]
                self.blockdata[column//2][block] = self.blockdata[column//2][block+1]
                self.blockdata[column//2][block+1] = temp
            else:
                break 

    def auto_merge_block(self):
        """automatically detect "keyinput"/"keypressed"/"double click", merge and update the blocks as well as the data (workspace)"""
        for id, workspace in enumerate(self.blockdata):
            for index, block in enumerate(workspace):
                try:
                    if type(self.blockdata[id][index][0]) == list:
                        for position, element in enumerate(self.blockdata[id][index][0]):
                            try:
                                if self.blockdata[id][index][position][3][0] == 0:
                                    if  self.blockdata[id][index][position][3][-1] <=0.1 and self.blockdata[id][index][position][3][4] == 1 and self.blockdata[id][index][position+1][3][4] == 0:
                                        self.blockdata[id][index][position][0] = 1
                                        self.blockdata[id][index][position][2] = "Mouse click"
                                        self.blockdata[id][index][position][3][3] = "click"
                                        self.blockdata[id][index][position][3][-1] += self.blockdata[id][index][position+1][3][-1]
                                        self.blockdata[id][index][position][5] = self.blockdata[id][index][position][5].replace("pyautogui.mouseDown","pyautogui.click")
                                        self.blockdata[id][index][position] = self.blockdata[id][index][position]
                                        for i in range(len(self.blockdata[id][index][position][5])):
                                            string = self.blockdata[id][index][position][5]
                                            if string[-i-5:-i]=="sleep": 
                                                self.blockdata[id][index][position][5] = string.replace(string[-i-5:],f"sleep({self.blockdata[id][index][position][3][-1]})\n")
                                                break
                                        self.blockdata[id][index][position+1] = 0
                                if self.blockdata[id][index][position][3][3] != "keyinput" and self.blockdata[id][index][position][0] == 1 and self.blockdata[id][index][position+1][0] == 1 and self.blockdata[id][index][position][3][-1] < 0.4 and self.blockdata[id][index][position][3][3] != "Double click" and self.blockdata[id][index][position+1][3][3] != "Double click":
                                    self.blockdata[id][index][position][0] = 1
                                    self.blockdata[id][index][position][2] = "Double click"
                                    self.blockdata[id][index][position][3][3] = "Double click"
                                    self.blockdata[id][index][position][3][-1] += self.blockdata[id][index][position+1][3][-1]
                                    self.blockdata[id][index][position][5] = self.blockdata[id][index][position][5].replace("pyautogui.click","pyautogui.doubleClick")
                                    for i in range(len(self.blockdata[id][index][position][5])):
                                        string = self.blockdata[id][index][position][5]
                                        if string[-i-5:-i]=="sleep": 
                                            self.blockdata[id][index][position][5] = string.replace(string[-i-5:],f"sleep({self.blockdata[id][index][position+1][3][-1]})\n")
                                            break
                                    self.blockdata[id][index][position] = self.blockdata[id][index][position]
                                    self.blockdata[id][index][position+1] = 0
                                elif self.blockdata[id][index][position][3][1] == 1:
                                    if  self.blockdata[id][index][position][3][-1] <= 0.1 and self.blockdata[id][index][position][3][1] == 1 and self.blockdata[id][index][position+1][3][1] == 0:
                                        self.blockdata[id][index][position][0] = 1
                                        self.blockdata[id][index][position][2] = f"Keyinput {self.blockdata[id][index][position][3][2]}"
                                        self.blockdata[id][index][position][3][3] = "keyinput"
                                        self.blockdata[id][index][position][3][-1] += self.blockdata[id][index][position+1][3][-1]
                                        self.blockdata[id][index][position][5] = self.blockdata[id][index][position][5].replace("pyautogui.keyDown","pyautogui.press")
                                        self.blockdata[id][index][position] = self.blockdata[id][index][position]
                                        for i in range(len(self.blockdata[id][index][position][5])):
                                            string = self.blockdata[id][index][position][5]
                                            if string[-i-5:-i]=="sleep": 
                                                self.blockdata[id][index][position][5] = string.replace(string[-i-5:],f"sleep({self.blockdata[id][index][position][3][-1]})\n")
                                                break
                                        self.blockdata[id][index][position+1] = 0
                            except:
                                pass
                        for count in range(self.blockdata[id][index].count(0)):
                            self.blockdata[id][index].remove(0)                 
                    else:
                        try:
                            if self.blockdata[id][index][3][0] == 0:
                                if  self.blockdata[id][index][3][-1] <=0.1 and self.blockdata[id][index][3][4] == 1 and self.blockdata[id][index+1][3][4] == 0:
                                    self.blockdata[id][index][0] = 1
                                    self.blockdata[id][index][2] = "Mouse click"
                                    self.blockdata[id][index][3][3] = "click"
                                    self.blockdata[id][index][3][-1] += self.blockdata[id][index+1][3][-1]
                                    self.blockdata[id][index][5] = self.blockdata[id][index][5].replace("pyautogui.mouseDown","pyautogui.click")
                                    self.blockdata[id][index] = self.blockdata[id][index]
                                    for i in range(len(self.blockdata[id][index][5])):
                                        string = self.blockdata[id][index][5]
                                        if string[-i-5:-i]=="sleep": 
                                            self.blockdata[id][index][5] = string.replace(string[-i-5:],f"sleep({self.blockdata[id][index][3][-1]})\n")
                                            break
                                    self.blockdata[id][index+1] = 0	

                            if self.blockdata[id][index][3][3] != "keyinput" and self.blockdata[id][index][0] == 1 and self.blockdata[id][index+1][0] == 1 and self.blockdata[id][index][3][-1] < 0.4 and self.blockdata[id][index][3][3] != "Double click" and self.blockdata[id][index+1][3][3] != "Double click":
                                self.blockdata[id][index][0] = 1
                                self.blockdata[id][index][2] = "Double click"
                                self.blockdata[id][index][3][3] = "Double click"
                                self.blockdata[id][index][3][-1] = self.blockdata[id][index+1][3][-1]
                                self.blockdata[id][index][5] = self.blockdata[id][index][5].replace("pyautogui.click","pyautogui.doubleClick")
                                for i in range(len(self.blockdata[id][index][5])):
                                    string = self.blockdata[id][index][5]
                                    if string[-i-5:-i]=="sleep": 
                                        self.blockdata[id][index][5] = string.replace(string[-i-5:],f"sleep({self.blockdata[id][index+1][3][-1]})\n")
                                        break
                                self.blockdata[id][index] = self.blockdata[id][index]
                                self.blockdata[id][index+1] = 0
                            elif self.blockdata[id][index][3][1] == 1:
                                if  self.blockdata[id][index][3][-1] <= 0.1 and self.blockdata[id][index][3][1] == 1 and self.blockdata[id][index+1][3][1] == 0:
                                    self.blockdata[id][index][0] = 1
                                    self.blockdata[id][index][2] = f"Keyinput {self.blockdata[id][index][3][2]}"
                                    self.blockdata[id][index][3][3] = "keyinput"
                                    self.blockdata[id][index][3][-1] += self.blockdata[id][index+1][3][-1]
                                    self.blockdata[id][index][5] = self.blockdata[id][index][5].replace("pyautogui.keyDown","pyautogui.press")
                                    self.blockdata[id][index] = self.blockdata[id][index]
                                    for i in range(len(self.blockdata[id][index][5])):
                                        string = self.blockdata[id][index][5]
                                        if string[-i-5:-i]=="sleep": 
                                            self.blockdata[id][index][5] = string.replace(string[-i-5:],f"sleep({self.blockdata[id][index][3][-1]})\n")
                                            break
                                    self.blockdata[id][index+1] = 0	
                        except:
                            pass
                except:
                    pass
            for count in range(workspace.count(0)):
                self.blockdata[id].remove(0)
        self.refresh_listbox()

    def record_new_block(self):
        """record a new block (workspace)"""
        self.blockdata[9].append([])
        a = thread_pool_executor.submit(rcb.main,self.filename,set(self.failsafekey),set(self.pause_key),set(self.img_extraction_key),set(self.text_extraction_key), self.blockdata[9][-1])
        self.addonepbutton(5,5,9,"Display new block",self.display_block_information,self.blockdata[9][-1])
        self.addbutton(5,6,9,"add new block to main",self.add_new_block_to_main)

    def add_new_block_to_main(self):
        """add the newly recorded block to main (workspace)"""
        self.blockdata[0].append(self.blockdata[9][-1])
        self.refresh_listbox()

    def delete_selected_block(self):
        """delete all selected blocks in the workspace (workspace)"""
        for i in range(5):
            try:
                for index, block in enumerate(self.gridmap[5][1][i*2].curselection()):
                    self.gridmap[5][1][i*2].delete(block,block)
                    self.blockdata[i][block] = 0
                for count in range(self.blockdata[i].count(0)):
                    self.blockdata[i].remove(0)
            except:
                pass
        self.refresh_listbox()
    
    def merge_selected_block(self):
        """merge all selected blocks in the workspace (workspace)"""
        temp = 0
        dimension = 0
        for i in range(5):
            newblock = []
            if type(self.gridmap[5][1][i*2])!=int:
                if self.gridmap[5][1][i*2].curselection():
                    for index, block in enumerate(self.gridmap[5][1][i*2].curselection()):
                        newblock.append(self.blockdata[i][block])
                        dimension += 1
                        temp = i
                    if len(newblock) == 1:
                        newblock = newblock[0]
                        newblock[0] = dimension
                    newblock[0][0] = dimension
                    self.blockdata[i].append(newblock)
                    break
        self.refresh_listbox()
        self.gridmap[5][1][temp*2].selection_set(END)

    def concatenate_to_main(self,column):
        """concatenate the current workspace's blocks onto main (workspace)"""
        for index, command in enumerate(self.blockdata[column//2]):
            try:
                self.blockdata[0].append(copy.deepcopy(command[:1])+[command[1].copy()]+copy.deepcopy(command[2:]))
            except:
                self.blockdata[column//2][index] = copy.deepcopy(command)
        self.refresh_listbox()        

    def merge_to_main(self,column):
        """replace main automation with selected workspace (workspace)"""
        self.blockdata[0] = []
        for index, command in enumerate(self.blockdata[column//2]):
            try:
                self.blockdata[0].append(copy.deepcopy(command[:1])+[command[1].copy()]+copy.deepcopy(command[2:]))
            except:
                self.blockdata[column//2][index] = copy.deepcopy(command)
        self.refresh_listbox()

    def find_block(self,row,column):
        """helper function for display block information, find the closed selected block and deepcopy it (workspace)"""
        for block in self.gridmap[5][1][column-2].curselection():
            row = row-1
            column = block
            self.default_block_value = []
            temp = self.blockdata[row][column]
            for i in range(len(temp)):
                if type(temp[i]) == list:
                    if type(temp[i][1]) != int:
                        try:
                            self.default_block_value.append([copy.deepcopy(temp[i][0])]+[temp[i][1].copy()]+copy.deepcopy(temp[i][2:]))
                        except:
                            self.default_block_value.append(copy.deepcopy(temp[i]))
                else:
                    try:
                        self.default_block_value.extend([copy.deepcopy(temp[0])]+[temp[1].copy()]+copy.deepcopy(temp[2:]))
                    except:
                        self.default_block_value.extend(copy.deepcopy(temp))
                    break
            break
        self.display_block_information(self.blockdata[row][column])

    def display_block_information(self,lst, dimension = 0):
        """display selected block information tp display information frame (display information)"""
        for r in range(10):
            for c in range(10):
                self.refresh_widget(4,r,c)
                self.refresh_widget(3,r,c)
        if type(lst[0]) == list:
            
            self.addlabel(3,0,0,"Block code:")
            self.addtext(3,1,0,rspan = 10)
            for index, block in enumerate(lst):
                self.gridmap[3][1][0].insert(END,block[5])
            self.addonepbutton(3,11,0,"Save code", self.save_code,lst)
            self.addonepbutton(3,12,0,"restore default code", self.restore_default_code, lst)
            self.addcombobox(3,0,1,["Add repeats"],self.pick_logic)

            self.addlabel(4,0,0,"Block infomation:")
            self.addlabel(4,1,0,"Block type:")        
            self.addentry(4,1,1,None,None,None,None,default=lst[0][0])
            self.addlabel(4,2,0,"Block name:")
            self.addentry(4,2,1,None,None,None,None,default=lst[0][2])

            if lst[dimension][3][0] == 0:
                self.addlabel(4,3,0,"X position:")
                self.addentry(4,3,1,None,None,None,None,default=lst[dimension][3][1])
                self.addlabel(4,4,0,"Y position:")
                self.addentry(4,4,1,None,None,None,None,default=lst[dimension][3][2])
                self.addlabel(4,5,0,"Action state:")
                self.addentry(4,5,1,None,None,None,None,default=lst[dimension][3][3])
                self.addlabel(4,6,0,"Action type:")
                self.addentry(4,6,1,None,None,None,None,default=lst[dimension][3][4])
                self.addlabel(4,7,0,"Image name:")
                self.addentry(4,7,1,None,None,None,None,default=lst[dimension][3][5])
                self.addlabel(4,8,0,"Waiting time:")
                self.addentry(4,8,1,None,None,None,None,default=lst[dimension][3][-1])
                self.addlabel(4,1,2,"Screenshot:")
                try:
                    self.img = (PhotoImage(file = f"screenshot/{self.filename}/{lst[dimension][3][5]}.png"))    
                    self.addlabel(4,2,2,None,img=self.img, cspan = 10, rspan = 10)       
                except:
                    self.addlabel(4,2,2,"No image recorded for this block", cspan = 10, rspan = 10)   

            elif lst[dimension][3][0] == 1:
                self.addlabel(4,3,0,"Action state:")
                self.addentry(4,3,1,None,None,None,None,default=lst[dimension][3][1])
                self.addlabel(4,4,0,"Key pressed:")
                self.addentry(4,4,1,None,None,None,None,default=lst[dimension][3][2])
                self.addlabel(4,5,0,"Image name:")
                self.addentry(4,5,1,None,None,None,None,default=lst[dimension][3][3])
                self.addlabel(4,6,0,"Waiting time:")
                self.addentry(4,6,1,None,None,None,None,default=lst[dimension][3][-1])
                self.addlabel(4,1,2,"Screenshot:")
                try:
                    self.img = (PhotoImage(file = f"screenshot/{self.filename}/{lst[dimension][3][3]}.png"))    
                    self.addlabel(4,2,2,None,img=self.img, cspan = 10, rspan = 10)
                except:
                    self.addlabel(4,2,2,"No image recorded for this block", cspan = 10, rspan = 10)  

            else:
                self.addlabel(4,3,0,"X position:")
                self.addentry(4,3,1,None,None,None,None,default=lst[dimension][3][1])
                self.addlabel(4,4,0,"Y position:")
                self.addentry(4,4,1,None,None,None,None,default=lst[dimension][3][2])
                self.addlabel(4,5,0,"Action state:")
                self.addentry(4,5,1,None,None,None,None,default=lst[dimension][3][3])
                self.addlabel(4,6,0,"Action type:")
                self.addentry(4,6,1,None,None,None,None,default=lst[dimension][3][0])
                self.addlabel(4,7,0,"Image name:")
                self.addentry(4,7,1,None,None,None,None,default=lst[dimension][3][4])
                self.addlabel(4,8,0,"Waiting time:")
                self.addentry(4,8,1,None,None,None,None,default=lst[dimension][3][-1])
                self.addlabel(4,1,2,"Screenshot:")
                try:
                    self.img = (PhotoImage(file = f"screenshot/{self.filename}/img_extraction_{lst[dimension][3][4]}.png"))
                    if self.img.width()>300 or self.img.height()>300:
                        self.img = self.img.subsample(max(self.img.width()//300, self.img.height()//300))
                    self.addlabel(4,2,2,None,img=self.img, cspan = 10, rspan = 10)
                except:
                    self.addlabel(4,2,2,"No image recorded for this block", cspan = 10, rspan = 10)

            if dimension <lst[0][0]-1:
                self.addtwopbutton(4,11,1,"Up a command",self.display_block_information, lst, dimension+1)
            else:
                self.refresh_widget(4,11,1)
            if dimension >= 1:
                self.addtwopbutton(4,12,1,"Down a command",self.display_block_information, lst, dimension-1)   
            else:
                self.refresh_widget(4,12,1)    
            self.addtwopbutton(4,9,1,"Save block data",self.save_block_data, lst, dimension+1)
            self.addtwopbutton(4,13,1,"restore default block value",self.restore_default_block_value,lst, dimension+1)   
        else:
            self.addlabel(3,0,0,"Block code:")
            self.addtext(3,1,0,rspan = 10)
            self.gridmap[3][1][0].insert(END,lst[5])
            self.addonepbutton(3,11,0,"Save code", self.save_code,lst)
            self.addonepbutton(3,12,0,"restore default code", self.restore_default_code, lst)
            self.addcombobox(3,0,1,["Add repeats"],self.pick_logic)

            self.addlabel(4,0,0,"Block infomation:")
            self.addlabel(4,1,0,"Block type:")        
            self.addentry(4,1,1,None,None,None,None,default=lst[0])
            self.addlabel(4,2,0,"Block name:")
            self.addentry(4,2,1,None,None,None,None,default=lst[2])
            if lst[3][0] == 0:
                self.addlabel(4,3,0,"X position:")
                self.addentry(4,3,1,None,None,None,None,default=lst[3][1])
                self.addlabel(4,4,0,"Y position:")
                self.addentry(4,4,1,None,None,None,None,default=lst[3][2])
                self.addlabel(4,5,0,"Action state:")
                self.addentry(4,5,1,None,None,None,None,default=lst[3][3])
                self.addlabel(4,6,0,"Action type:")
                self.addentry(4,6,1,None,None,None,None,default=lst[3][4])
                self.addlabel(4,7,0,"Image name:")
                self.addentry(4,7,1,None,None,None,None,default=lst[3][5])
                self.addlabel(4,8,0,"Waiting time:")
                self.addentry(4,8,1,None,None,None,None,default=lst[3][-1])
                self.addlabel(4,1,2,"Screenshot:")
                try:
                    self.img = (PhotoImage(file = f"screenshot/{self.filename}/{lst[3][5]}.png"))    
                    self.addlabel(4,2,2,None,img=self.img, cspan = 10, rspan = 10)       
                except:
                    self.addlabel(4,2,2,"No image recorded for this block", cspan = 10, rspan = 10)   
            elif lst[3][0]==1:
                self.addlabel(4,3,0,"Action state:")
                self.addentry(4,3,1,None,None,None,None,default=lst[3][1])
                self.addlabel(4,4,0,"Key pressed:")
                self.addentry(4,4,1,None,None,None,None,default=lst[3][2])
                self.addlabel(4,5,0,"Image name:")
                self.addentry(4,5,1,None,None,None,None,default=lst[3][3])
                self.addlabel(4,6,0,"Waiting time:")
                self.addentry(4,6,1,None,None,None,None,default=lst[3][-1])
                self.addlabel(4,1,2,"Screenshot:")
                try:
                    self.img = (PhotoImage(file = f"screenshot/{self.filename}/{lst[3][3]}.png"))    
                    self.addlabel(4,2,2,None,img=self.img, cspan = 10, rspan = 10)
                except:
                    self.addlabel(4,2,2,"No image recorded for this block", cspan = 10, rspan = 10)
            else:
                self.addlabel(4,3,0,"X position:")
                self.addentry(4,3,1,None,None,None,None,default=lst[3][1])
                self.addlabel(4,4,0,"Y position:")
                self.addentry(4,4,1,None,None,None,None,default=lst[3][2])
                self.addlabel(4,5,0,"Action state:")
                self.addentry(4,5,1,None,None,None,None,default=lst[3][3])
                self.addlabel(4,6,0,"Action type:")
                self.addentry(4,6,1,None,None,None,None,default=lst[3][0])
                self.addlabel(4,7,0,"Image name:")
                self.addentry(4,7,1,None,None,None,None,default=lst[3][4])
                self.addlabel(4,8,0,"Waiting time:")
                self.addentry(4,8,1,None,None,None,None,default=lst[3][-1])
                self.addlabel(4,1,2,"Screenshot:")
                try:
                    self.img = (PhotoImage(file = f"screenshot/{self.filename}/img_extraction_{lst[3][4]}.png"))
                    if self.img.width()>300 or self.img.height()>300:
                        self.img = self.img.subsample(max(self.img.width()//300, self.img.height()//300))
                    self.addlabel(4,2,2,None,img=self.img, cspan = 10, rspan = 10)
                except:
                    self.addlabel(4,2,2,"No image recorded for this block", cspan = 10, rspan = 10)
            self.addonepbutton(4,9,1,"Save block data",self.save_block_data, lst)
            self.addonepbutton(4,13,1,"restore default block value",self.restore_default_block_value,lst)

    def restore_default_block_value(self,lst,dimension = 0):
        """restore default block value in selected block (display block information)"""
        if dimension:
            lst[dimension-1][2]    = self.default_block_value[dimension-1][2]   
            lst[dimension-1][3][1] = self.default_block_value[dimension-1][3][1]
            lst[dimension-1][3][2] = self.default_block_value[dimension-1][3][2]
            lst[dimension-1][3][3] = self.default_block_value[dimension-1][3][3]
            lst[dimension-1][3][4] = self.default_block_value[dimension-1][3][4]
            if lst[dimension-1][3][0] == 0:
                lst[dimension-1][3][5] = self.default_block_value[dimension-1][3][5]
                lst[dimension-1][3][6] = self.default_block_value[dimension-1][3][6]
            elif lst[dimension-1][3][0] != 1:
                lst[dimension-1][3][5] = self.default_block_value[dimension-1][3][5]
        else:
            lst[2]    = self.default_block_value[2]   
            lst[3][1] = self.default_block_value[3][1]
            lst[3][2] = self.default_block_value[3][2]            
            lst[3][3] = self.default_block_value[3][3]     
            lst[3][4] = self.default_block_value[3][4] 
            if lst[3][0] == 0:
                lst[3][5] = self.default_block_value[3][5]
                lst[3][6] = self.default_block_value[3][6]
            elif lst[3][0] != 1:
                lst[3][5] = self.default_block_value[3][5]

        self.display_block_information(lst)
        self.refresh_listbox()

    def save_code(self,lst):
        """save editted code (logic)"""
        if type(lst[0]) == list:
            for index, code in enumerate(self.gridmap[3][1][0].get(1.0,END)[:-1].split("    \n    \n")):
                try:
                    lst[index][-1] = code + "\n\n"
                except:
                    pass         
        else:
            lst[5] = self.gridmap[3][1][0].get(1.0,END)[:-1]

    def restore_default_code(self,lst):
        """restore default code (logic)"""
        self.gridmap[3][1][0].delete(1.0,END)
        if type(lst[0]) == list:
            for index, block in enumerate(lst):
                self.gridmap[3][1][0].insert(END,block[-1])        
        else:
            self.gridmap[3][1][0].insert(END,lst[5])            

    def pick_logic(self, event):
        """selected logic (repeat) (logic)"""
        if self.gridmap[3][0][1].get() == "Add repeats":
            self.add_repeats()

    def add_repeats(self):
        """add repeat (logic)"""
        self.addlabel(3,1,1,"How many times do you want to repeat this action:")
        self.addentry(3,1,2,"<Return>",None,self.repeat,None,default=0)

    def repeat(self,event):
        """add repeat code(logic"""
        text = self.gridmap[3][1][0].get(1.0,END)[:-1]
        text = f"for count in range({self.gridmap[3][1][2].get()}):\n" + text 
        text = text.replace("\n","\n    ")
        self.addtext(3,1,0,rspan = 10)
        self.gridmap[3][1][0].insert(END,text) 

    def execute(self):
        """convert all blocks in main automation into python source code (mainmenu)"""
        tab = "    "
        with open(f"pyscript/{self.filename}.py","w") as f:
            if self.activation_hotkey:
                if not self.reusable:
                    f.write(
    f"""
class a:
    def __init__(self):
        import os
        import time
        filename = \"{self.filename}\"
        try:
            with open("manager.json","r") as f:
                pass
        except:
            path = os.getcwd()
            for i in range(len(path)):
                if path[-(i+1)] == "\\\\":
                    path = path[:-(i+1)]
                    break
            os.chdir(path)
        try:
            os.mkdir(f"img_extraction/{{filename}}")
        except:
            pass
        try:
            with open(f"text_extraction/{{filename}}.txt", 'w') as fp:
                pass
        except:
            pass
        import json
        with open("manager.json","r") as f:
            temp = json.load(f)
        temp["{self.filename}"] = 1
        with open("manager.json","w") as f:
            json.dump(temp,f,indent = 4)
        time.sleep({self.execution_timer})
        self.keypressed = set()
        self.failsafekey = {self.activation_hotkey}
        self.terminate = {set(self.failsafekey)}
        self.start()
        self.run()
        
    def start(self):
        from pynput import keyboard
        import json
        def on_press(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\\\\\",'\\\\')
            self.keypressed.add(k)
            with open("manager.json","r") as f:
                if self.keypressed == self.failsafekey or not json.load(f)["{self.filename}"]:
                    self.kl1.stop()
        def on_release(key):
            k = str(key).replace("Key.","").replace("'",'').replace("\\\\\\\\",'\\\\')
            self.keypressed.discard(k)
        self.kl1 = keyboard.Listener(on_press=on_press,on_release=on_release)
        self.kl1.start()
        self.kl1.join()
        
    def run(self):
        import time
        try:
            from pytesseract import pytesseract
        except:
            pass
        import pyautogui
        import json
        from pynput import keyboard
        import os
        path_to_tesseract = \"{self.p_path}\"
        """
                    )
                else:
                    f.write(
    f"""
class a:
    def __init__(self):
        import os
        import time
        filename = \"{self.filename}\"
        try:
            with open("manager.json","r") as f:
                pass
        except:
            path = os.getcwd()
            for i in range(len(path)):
                if path[-(i+1)] == "\\\\":
                    path = path[:-(i+1)]
                    break
            os.chdir(path)
        try:
            os.mkdir(f"img_extraction/{{filename}}")
        except:
            pass
        try:
            with open(f"text_extraction/{{filename}}.txt", 'w') as fp:
                pass
        except:
            pass
        import json
        with open("manager.json","r") as f:
            temp = json.load(f)
        temp["{self.filename}"] = 1
        with open("manager.json","w") as f:
            json.dump(temp,f,indent = 4)
        time.sleep({self.execution_timer})
        self.keypressed = set()
        self.failsafekey = {self.activation_hotkey}
        self.terminate = {set(self.failsafekey)}
        self.start()

    def start(self):
        from pynput import keyboard
        import json
        while True:
            with open("manager.json","r") as f:
                if not json.load(f)["{self.filename}"]:
                    return
            try:
                def on_press(key):
                    k = str(key).replace("Key.","").replace("'",'').replace("\\\\\\\\",'\\\\')
                    self.keypressed.add(k)
                    with open("manager.json","r") as f:
                        if self.keypressed == self.failsafekey or not json.load(f)["{self.filename}"]:
                            self.kl1.stop()
                def on_release(key):
                    k = str(key).replace("Key.","").replace("'",'').replace("\\\\\\\\",'\\\\')
                    self.keypressed.discard(k)
                self.kl1 = keyboard.Listener(on_press=on_press,on_release=on_release)
                self.kl1.start()
                self.kl1.join()
                self.run()
            except:
                pass

    def run(self):
        import time
        try:
            from pytesseract import pytesseract
        except:
            pass
        import pyautogui
        import json
        from pynput import keyboard
        import os
        path_to_tesseract = \"{self.p_path}\"
        """
                    )
            else:
                f.write(
f"""
class a:
    def __init__(self):
        import os
        import time
        filename = \"{self.filename}\"
        try:
            with open("manager.json","r") as f:
                pass
        except:
            path = os.getcwd()
            for i in range(len(path)):
                if path[-(i+1)] == "\\\\":
                    path = path[:-(i+1)]
                    break
            os.chdir(path)
        try:
            os.mkdir(f"img_extraction/{{filename}}")
        except:
            pass
        try:
            with open(f"text_extraction/{{filename}}.txt", 'w') as fp:
                pass
        except:
            pass
        import json
        with open("manager.json","r") as f:
            temp = json.load(f)
        temp["{self.filename}"] = 1
        with open("manager.json","w") as f:
            json.dump(temp,f,indent = 4)
        time.sleep({self.execution_timer})
        self.keypressed = set()
        self.run()

    def run(self):
        import time
        try:
            from pytesseract import pytesseract
        except:
            pass
        import pyautogui
        import json
        from pynput import keyboard
        import os
        path_to_tesseract = \"{self.p_path}\"
""" 
                )
            for index, block in enumerate(self.blockdata[0]):
                if type(block[0]) == list:
                    outer = block[0][5].count("for")
                    for id, command in enumerate(block):
                        inner = command[5].count("for")
                        f.write(f"#block {index}, substep {id}\n")
                        if id == 0:
                            f.write(f"""
        with open("manager.json","r") as f:
            if not json.load(f)["{self.filename}"]:
                return
        """)             
                        else:
                            f.write(f"""
        {tab*(outer+inner)}with open("manager.json","r") as f:
            {tab*(outer+inner)}if not json.load(f)["{self.filename}"]: 
                {tab*(outer+inner)}return
        """
                        )
                        a = copy.deepcopy(command[5])
                        a = a.replace("\n","\n        ")
                        f.write(a)
                else:
                    count = block[5].count("for")
                    f.write(f"#block {index}\n")
                    f.write(
                        f"""
        with open("manager.json","r") as f:
            if not json.load(f)["{self.filename}"]:
                return
        """
                    )
                    a = copy.deepcopy(block[5])
                    a = a.replace("\n","\n        ")
                    f.write(a)                  
            f.write(f"""\n
def execute():
    from concurrent import futures
    thread_pool_executor = futures.ThreadPoolExecutor(max_workers=10)
    return thread_pool_executor.submit(a)
    
if __name__ == "__main__":    
    execute()
    """)

if __name__ == '__main__':
    thread_pool_executor = futures.ThreadPoolExecutor(max_workers=10)
    root = customtkinter.CTk()
    window1 = Window(root,"Automation generator","1000x800")
    with open("status.json", "w") as f:
        json.dump({"status" : 0}, f, indent=4)

"""
Minor fixes:
N/A
"""

"""
Existing problems:
N/A
"""

"""
Functions to add:
replace_merge for listbox
"""

"""
Could be faster/cleaner:
load data
auto-merge blocks
"""

"""
Others:
MacOS & Linux platform test needed

"""

"""
Notes: 
Custom Tkinter pyinstaller issue
"""
