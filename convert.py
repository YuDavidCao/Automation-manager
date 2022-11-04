from tkinter import PhotoImage

def create_img(blockdata,filename,n):
    try:
        img = (PhotoImage(file = f"screenshot/{filename}/{n}.png"))
        img = img.subsample(3,3)
        blockdata.append(img)
    except:
        blockdata.append(None)

def process(command,filename,xylst):

    blockdata = [0]

    if command[0] == 0:

        z,x,y,tp,s,n,t = command
        create_img(blockdata,filename,n)
        blockdata.append([z,x,y,tp,s,n,t])
        blockdata.append(0)
        blockdata.append(
f"""
x,y = {x},{y}
gen = pyautogui.locateAllOnScreen(\"screenshot/{filename}/{n}.png\")
try:
    g = next(gen)
    x,y,c,d = g
    x = a+c//2
    y = b+d//2
    try:
        next(gen)
        x,y = {x},{y}
    except:
        pass
except:
    pass
pyautogui.moveTo(x,y)
"""
        )

        if type(tp) == str:

            if s:
                blockdata.insert(2,f"Pressed {tp} click")
            else:
                blockdata.insert(2,f"Released {tp} click")
            blockdata[5] += f"pyautogui.mouseDown(button = \"{tp}\")\n"

        else:
            if tp == 120:
                blockdata.insert(2,"Scroll up")
            else:
                blockdata.insert(2,"Scroll down")
            blockdata[5] += f"pyautogui.scroll({tp},{x},{y})\n"
        blockdata[5] += f"time.sleep({t})\n\n"

    elif command[0] == 1:

        z,s,k,n,t = command

        create_img(blockdata,filename,n)
        blockdata.append([z,s,k,n,t])
        blockdata.append(0)
        blockdata.append("")

        if s:
            blockdata.insert(2,f"Pressed {k}")
            blockdata[5] += f"pyautogui.keyDown(\"{k}\")\n"
        else:
            blockdata.insert(2,f"Released {k}")
            blockdata[5] += f"pyautogui.keyUp(\"{k}\")\n"
        blockdata[5] += f"time.sleep({t})\n"
        blockdata[5] += f"\n" 

    elif command[0] == 2:

        z,x,y,s,n,t = command

        if s == 1:
            blockdata = 0
            xylst[0] = x
            xylst[1] = y

        elif s == 2:
            try:
                img = (PhotoImage(file = f"screenshot/{filename}/img_extraction_{n}.png"))
                img = img.subsample(3,3) ###
                blockdata.append(img)
            except:
                blockdata.append(None)

            blockdata.append([z,x,y,s,n,t])
            blockdata.append(0)
            blockdata.insert(2,"img_extraction")
            blockdata.append(
f"""
try:
    os.mkdir(\"img_extraction/{filename}\")
except:
    pass
i = 0
while True:
    if f"{{i}}.png" not in os.listdir("img_extraction/{filename}"):
        break
    i+=1
pyautogui.screenshot(f\"img_extraction/{filename}/{{i}}.png\",region=({min(xylst[0],x)}, {min(xylst[1],y)}, {max(xylst[0],x)-min(xylst[0],x)}, {max(xylst[1],y)-min(xylst[1],y)}))
time.sleep({t})

"""
            )

    elif command[0] == 3:

        z,x,y,s,n,t = command

        if s == 1:
            blockdata = 0
            xylst[0] = x
            xylst[1] = y
        
        elif s == 2:
            try:
                img = (PhotoImage(file = f"screenshot/{filename}/text_extraction_{n}.png"))
                img = img.subsample(3,3) ###
                blockdata.append(img)
            except:
                blockdata.append(None)
            blockdata.append([z,x,y,s,n,t])
            blockdata.append(0)
            blockdata.insert(2,"text_extraction")
            blockdata.append(
f"""
img = pyautogui.screenshot(region = ({min(xylst[0],x)}, {min(xylst[1],y)}, {max(xylst[0],x)-min(xylst[0],x)}, {max(xylst[1],y)-min(xylst[1],y)}))
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
with open(f\"text_extraction/{filename}.txt\",\"a\") as f:
    f.write(text)
time.sleep({t})

"""
            )

    return blockdata

if __name__ == "__main__":
    a = process(    [
        0,
        805,
        507,
        -120,
        2,
        8,
        0.08033037185668945
    ], "record_1",[0,0])
    print(a)
