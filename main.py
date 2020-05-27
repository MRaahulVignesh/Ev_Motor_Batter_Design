
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import calculation

class Main:
    def __init__(self, master):
       

        self.master = master

        mainframe = tk.Frame(self.master, width=650, height=550, bg="#f8f8f8")
        mainframe.pack(fill=tk.BOTH)

        default_dir_label = tk.Label(mainframe, text="Electrical Vehicle Motor and Battery Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        default_dir_label.place(x=30, y=50)

        button_motor = tk.Button(mainframe, text="Motor Design", font="Arial 12 bold", width=25, height = 5, command = self.motor_design)
        button_motor.place(x=200, y=150)
        button_video = tk.Button(mainframe, text="Battery Design", font="Arial 12 bold", width=25, height = 5, command= self.battery_design)
        button_video.place(x=200, y=350)

    def motor_design(self):
        mtr_window = tk.Toplevel(self.master)
        mtr_window.title("Motor Design Tool") 
        mtr_window.geometry("650x550+300+250")  

        frame_1 = tk.Frame(mtr_window, width=650, height=550, bg="#f8f8f8")
        frame_1.pack(fill=tk.BOTH)

        title_label = tk.Label(frame_1, text="Electrical Vehicle Motor Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        title_label.place(x=100, y=20)

        label_1 = tk.Label(frame_1, text="Vehicle Weight :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_1.place(x=70, y=100)
        self.entry_1 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_1.place(x=200, y=100)

        label_2 = tk.Label(frame_1, text="Vehicle Area :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_2.place(x=70, y=150)
        self.entry_2 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_2.place(x=200, y=150)

        label_3 = tk.Label(frame_1, text="Slip :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_3.place(x=70, y=200)
        self.entry_3 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_3.place(x=200, y=200)

        label_4 = tk.Label(frame_1, text="Cd :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_4.place(x=70, y=250)
        self.entry_4 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_4.place(x=200, y=250)

        label_5 = tk.Label(frame_1, text="Crr :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_5.place(x=70, y=300)
        self.entry_5 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_5.place(x=200, y=300)

        label_6 = tk.Label(frame_1, text="Grade_percent :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_6.place(x=370, y=100)
        self.entry_6 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_6.place(x=500, y=100)

        label_7 = tk.Label(frame_1, text="Vehicle Speed :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_7.place(x=370, y=150)
        self.entry_7 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_7.place(x=500, y=150)

        label_8 = tk.Label(frame_1, text="Wind Speed :", font="Times 12", bg="#f8f8f8", fg="#101010")
        label_8.place(x=370, y=200)
        self.entry_8 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_8.place(x=500, y=200)

        label_9 = tk.Label(frame_1, text="Wheel Radius :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_9.place(x=370, y=250)
        self.entry_9 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_9.place(x=500, y=250)

        label_10 = tk.Label(frame_1, text="Gear Ratio :", font="Times 12 ", bg="#f8f8f8", fg="#101010")
        label_10.place(x=370, y=300)
        self.entry_10 = tk.Entry(frame_1, font="Times 15 bold", width=10)
        self.entry_10.place(x=500, y=300)

        button_cal = tk.Button(frame_1, text="Generate", font="Arial 12 bold", width=7, command=self.generate_motor)
        button_cal.place(x=270, y=375)

    def generate_motor(self):

    

        ## call the function here
        try:
            v_weight = float(self.entry_1.get())
            v_area = float(self.entry_2.get())
            slip = float(self.entry_3.get())
            Cd = float(self.entry_4.get())
            Crr = float(self.entry_5.get())
            grade_percent = float(self.entry_6.get())
            v_speed = float(self.entry_7.get())
            v_wind = float(self.entry_8.get())
            wheel_radius = float(self.entry_9.get())
            gear_ratio = float(self.entry_10.get())
            cal = calculation.Calculation(v_weight, v_area, slip, Cd, Crr, wheel_radius, gear_ratio, v_speed, grade_percent)
            answer = cal.motor(v_wind)
            message = "Motor Torque = " + str(answer)

        except Exception as e:
            message = "Error: Check the variables"
            print(e)

        pop_up = tk.Tk()
        pop_up.title("Motor Specification")
        w = 400     
        h = 200     
        sw = pop_up.winfo_screenwidth()
        sh = pop_up.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        pop_up.geometry('%dx%d+%d+%d' % (w, h, x, y))

        m = tk.Label(pop_up, text=message, font="Times 12", width=120, height=5)
        m.pack()
        b = tk.Button(pop_up, text="OK", command=pop_up.destroy, width=10)
        b.pack()
        tk.mainloop()


    def battery_design(self):
        bty_window = tk.Toplevel(self.master)
        bty_window.title("Battery Design Tool") 
        bty_window.geometry("650x550+300+250")  
        
        frame_1 = tk.Frame(bty_window, width=650, height=550, bg="#f8f8f8")
        frame_1.pack(fill=tk.BOTH)

        title_label = tk.Label(frame_1, text="Electrical Vehicle Battery Design Tool", font="Times 18 bold", bg="#f8f8f8", fg="#101010")
        title_label.place(x=100, y=50)

        
def main():
  
    root = tk.Tk()
    root.geometry("650x550+300+250")
    root.resizable(False, False)
    root.title("Video Splitter")
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()
