from tkinter import *
from tkinter import filedialog
import subprocess
import os

def fileselect():
    filename = filedialog.askopenfilename(initialdir = os.getenv("HOME"), title = "Select File",
    filetypes = (("mp3 files", "*.mp3"), ("all files", "*.*")))
    file_Select["text"] = filename

def startButton():
    origin_File_URL = file_Select.cget('text')
    save_Path_URL = str(savePath.get())
    start_Time = str(startTime.get())
    end_Time = str(endTime.get())
    try:
        subprocess.check_call(['ffmpeg', '-i', origin_File_URL, '-ss', start_Time, '-to',
        end_Time, '-y', save_Path_URL])
        resultBtn["text"] = "finish"
    except subprocess.CalledProcessError as e:
        resultBtn["text"] = "failed"

window = Tk()

window.title("MP3 FILE TIME CUT Program")
window.geometry("400x100")
window.resizable(False, False)
file_Select = Button(window, text = "MP3 FILE", command = fileselect, height = 1, width = 100)
file_Select.pack(side = TOP)
savePath = Entry(window, width = 100)
savePath.insert(0, os.getenv("HOME") + "/example.mp3")
savePath.pack(side = TOP)
startTime = Entry(window, width = 20)
startTime.insert(0, "00:00:00")
startTime.pack(side = LEFT)
endTime = Entry(window, width = 20)
endTime.insert(0, "00:04:20")
endTime.pack(side = LEFT)
startBtn = Button(window, text = "Start!", command = startButton)
startBtn.pack()
resultBtn = Button(window, text = "Not_Started")
resultBtn.pack()

window.mainloop()