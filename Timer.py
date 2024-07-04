import tkinter as tk
import winsound
import time
import html
from PIL import Image, ImageTk
 
workTime = 45 * 60
breakTime = 15 * 60
 
class Main:
    def __init__(self, root):
        self.workTime = workTime
        self.breakTime = breakTime
        self.work = False
        self.mins = ''
        self.sec = ''
        self.after_id = None
        self.frame = tk.Frame(root)

        self.btn_rem = tk.Button(self.frame, 
                        text="<",
                        font=("Arial",20),
                        command=self.on_btn_rem)    
        self.btn_add = tk.Button(self.frame, 
                        text=">",
                        font=("Arial",20),
                        command=self.on_btn_add)          

        self.btn_10 = tk.Button(self.frame, 
                        text="10",
                        font=("Arial",20),
                        command=self.on_btn_10)    
        self.btn_15 = tk.Button(self.frame, 
                        text="15",
                        font=("Arial",20),
                        command=self.on_btn_15)    
        self.btn_30 = tk.Button(self.frame, 
                        text="30",
                        font=("Arial",20),
                        command=self.on_btn_30)    
        self.btn_45 = tk.Button(self.frame, 
                        text="45",
                        font=("Arial",20),
                        command=self.on_btn_45)                            
 
        self.btn_start = tk.Button(self.frame, 
                                text="Start",
                                bg="green",
                                fg="white",
                                font=("Arial",20),
                                command=self.on_btn_start)        
        self.btn_stop = tk.Button(self.frame, 
                                text="Stop",
                                font=("Arial",20),
                                command=self.on_btn_stop)        
        self.btn_reset = tk.Button(self.frame, 
                                text="Reset",
                                font=("Arial",20),
                                command=self.on_btn_reset)
        self.btn_work = tk.Button(self.frame, 
                                text="Start Work",
                                bg="green",
                                fg="white",
                                font=("Arial",20),
                                command=self.on_btn_work)
        self.entry = tk.Entry(self.frame,
                              font=("Arial",24),
                              justify="center",
                              text="text")
        
        self.entry.grid(row=1,column=1,columnspan=4,ipady=25)
        self.entry.insert(0,time.strftime("%H:%M:%S", time.gmtime(self.workTime)))

        self.btn_rem.grid(row=2,column=1,columnspan=2,ipadx=70,ipady=0)
        self.btn_add.grid(row=2,column=3,columnspan=2,ipadx=70,ipady=0)

        self.btn_10.grid(row=3,column=1,ipadx=18,ipady=5)
        self.btn_15.grid(row=3,column=2,ipadx=18,ipady=5)
        self.btn_30.grid(row=3,column=3,ipadx=18,ipady=5)
        self.btn_45.grid(row=3,column=4,ipadx=18,ipady=5)

        self.btn_start.grid(row=4,column=1,ipadx=4,ipady=5)
        self.btn_stop.grid(row=4,column=2,ipadx=6,ipady=5)
        self.btn_reset.grid(row=4,column=3,columnspan=2,ipadx=42,ipady=5)
        self.btn_work.grid(row=5,column=1,columnspan=4,ipadx=102,ipady=5)
        self.frame.grid()   

    def on_btn_rem(self):
        self.workTime = self.workTime - 60
        self.display_counter(self.workTime)

    def on_btn_add(self):
        self.workTime = self.workTime + 60
        self.display_counter(self.workTime)        

    def on_btn_10(self):
        self.on_btn_stop()
        self.workTime = 10 * 60
        self.display_counter(self.workTime)
    
    def on_btn_15(self):
        self.on_btn_stop()
        self.workTime = 15 * 60
        self.display_counter(self.workTime)

    def on_btn_30(self):
        self.on_btn_stop()
        self.workTime = 30 * 60
        self.display_counter(self.workTime)

    def on_btn_45(self):
        self.on_btn_stop()
        self.workTime = 45 * 60
        self.display_counter(self.workTime)
 
    def on_btn_start(self):
        if not self.after_id:
            self.decrease_counter()
            self.btn_start.configure(bg="red")
 
    def on_btn_stop(self):
        if self.after_id:
            self.frame.after_cancel(self.after_id)
            self.after_id = None
            self.btn_start.configure(bg="green")
            self.btn_work.configure(bg="green")
 
    def on_btn_reset(self):
        self.on_btn_stop()
        self.workTime = workTime
        self.display_counter(self.workTime)
    
    def on_btn_work(self):
        if not self.after_id:
            self.work = True
            self.decrease_counter()
            self.btn_work.configure(bg="red")
            self.workTime = 1*30
            self.breakTime = 1*15
            self.display_counter(self.workTime)
 
    def decrease_counter(self):
        self.workTime -= 1
        self.display_counter(self.workTime)
        self.after_id = self.frame.after(1000, self.decrease_counter)        
        if self.workTime < 0:    
            if self.work:       
                self.workTime = self.breakTime
            else:
                self.beep()
                self.on_btn_reset()     
        if self.breakTime < 0:
            self.workTime = 1*30
            self.workTime -= 1
            self.display_counter(self.workTime)    
            self.breakTime = 1*15                
 
    def display_counter(self,data):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, time.strftime("%H:%M:%S", time.gmtime(data)))
 
    def beep(self):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        for x in range(0,3):
            winsound.Beep(frequency, duration)
            time.sleep(1) 

root = tk.Tk()
root.title("Timer "+html.unescape('&copy;')+"WW 11.2023")

main = Main(root)
root.mainloop()


